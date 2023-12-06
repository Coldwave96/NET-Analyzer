import os
import pandas as pd

import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

def read_csv_files_from_folder(folder_path):
    file_list = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    combined_df = pd.DataFrame()

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    return combined_df

def count_labels(combined_df, label_str):
    label_counts = combined_df[label_str].value_counts()
    total_data_count = len(combined_df)

    return label_counts, total_data_count

def encode_labels(combined_df, label_str):
    label_mapping = {}
    converted_labels = []

    for _, row in combined_df.iterrows():
        original_label = row[label_str]

        if original_label not in label_mapping:
            label_mapping[original_label] = len(label_mapping)
    
        converted_label = label_mapping[original_label]
        converted_labels.append(converted_label)

    combined_df = combined_df.drop(labels=[label_str], axis=1)
    combined_df[label_str] = converted_labels

    inverted_mapping = {v: k for k, v in label_mapping.items()}

    return combined_df, inverted_mapping

def create_dataloader(features_df, labels_df, test_size, batch_size):
    X_train, X_test, y_train, y_test = train_test_split(features_df, labels_df, test_size=test_size, random_state=42)

    X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)
    X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.long)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader

class BiLSTM(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(BiLSTM, self).__init__()
        self.bilstm = torch.nn.LSTM(
            input_size = input_size,
            hidden_size = 32,
            num_layers = 2,          
            batch_first = True,
            bidirectional = True
        )
        self.fc = torch.nn.Linear(64, output_size)

    def forward(self, x):
        x, _ = self.bilstm(x)
        x = self.fc(x)

        return x
