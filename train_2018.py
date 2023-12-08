import torch
from tqdm import tqdm

import utils

folder_path = "Datasets/CIC-IDS2018"
label_str = "Label"

combined_df = utils.read_csv_files_from_folder(folder_path)
label_counts, total_data_count = utils.count_labels(combined_df, label_str)
combined_df, inverted_mapping = utils.encode_labels(combined_df, label_str)

combined_df.drop(['Bwd PSH Flags'], axis=1, inplace=True)
combined_df.drop(['Bwd URG Flags'], axis=1, inplace=True)
combined_df.drop(['Timestamp'], axis=1, inplace=True)

print("[*] Datasets Info")
print(label_counts)
print(f"Total data count: {total_data_count}")

features_df = combined_df.iloc[:, :-1]
labels_df = combined_df.iloc[:, -1]

train_loader, test_loader = utils.create_dataloader(features_df, labels_df, 0.2, 64)

input_size = features_df.shape[0]
output_size = len(inverted_mapping)
model = utils.BiLSTM(input_size, output_size)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print("\n[*] Training & Testing")
num_epochs = 10
for epoch in tqdm(range(num_epochs), desc="Epochs"):
    model.train()
    train_loss = 0.0
    for inputs, labels in tqdm(train_loader, desc="Training", leave=False):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in tqdm(test_loader, desc="Testing", leave=False):
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Epoch {epoch + 1}/{num_epochs}")
    print(f"Training Loss: {train_loss / len(train_loader)}")
    print(f"Testing Loss: {test_loss / len(test_loader)}")
    print(f"Testing Accuracy: {(correct / total) * 100:.2f}%")
