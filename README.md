# NET-Analyzer

BiLSTM model for Network Intrusion Detection System (NIDS).

## Datasets

### CIC-IDS2017

[CICIDS2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html) contains benign and the most up-to-date common attacks, which resembles the true real-world data (PCAPs). It also includes the results of the network traffic analysis using CICFlowMeter with labeled flows based on the time stamp, source, and destination IPs, source and destination ports, protocols and attack (CSV files).

Generating realistic background traffic was our top priority in building this dataset. We have used our proposed B-Profile system (Sharafaldin, et al. 2016) to profile the abstract behavior of human interactions and generates naturalistic benign background traffic. For this dataset, we built the abstract behaviour of 25 users based on the HTTP, HTTPS, FTP, SSH, and email protocols.

The data capturing period started at 9 a.m., Monday, July 3, 2017 and ended at 5 p.m. on Friday July 7, 2017, for a total of 5 days. Monday is the normal day and only includes the benign traffic. The implemented attacks include Brute Force FTP, Brute Force SSH, DoS, Heartbleed, Web Attack, Infiltration, Botnet and DDoS. They have been executed both morning and afternoon on Tuesday, Wednesday, Thursday and Friday.

### CIC-IDS2018

In [CSE-CIC-IDS2018 dataset](https://www.unb.ca/cic/datasets/ids-2018.html), we use the notion of profiles to generate datasets in a systematic manner, which will contain detailed descriptions of intrusions and abstract distribution models for applications, protocols, or lower level network entities. These profiles can be used by agents or human operators to generate events on the network. Due to the abstract nature of the generated profiles, we can apply them to a diverse range of network protocols with different topologies. Profiles can be used together to generate a dataset for specific needs.

##  List of extracted traffic features by [CICFlowMeter-V3](https://www.unb.ca/cic/research/applications.html#CICFlowMeter)

|Feature Name|Description|
|-|-|
|fl_dur|Flow duration|
|tot_fw_pk|Total packets in the forward direction|
|tot_bw_pk|Total packets in the backward direction|
|tot_l_fw_pkt|Total size of packet in forward direction|
|fw_pkt_l_max|Maximum size of packet in forward direction|
|fw_pkt_l_min|Minimum size of packet in forward direction|
|fw_pkt_l_avg|Average size of packet in forward direction|
|fw_pkt_l_std|Standard deviation size of packet in forward direction|
|Bw_pkt_l_max|Maximum size of packet in backward direction|
|Bw_pkt_l_min|Minimum size of packet in backward direction|
|Bw_pkt_l_avg|Mean size of packet in backward direction|
|Bw_pkt_l_std|Standard deviation size of packet in backward direction|
|fl_byt_s|flow byte rate that is number of packets transferred per second|
|fl_pkt_s|flow packets rate that is number of packets transferred per second|
|fl_iat_avg|Average time between two flows|
|fl_iat_std|Standard deviation time two flows|
|fl_iat_max|Maximum time between two flows|
|fl_iat_min|Minimum time between two flows|
|fw_iat_tot|Total time between two packets sent in the forward direction|
|fw_iat_avg|Mean time between two packets sent in the forward direction|
|fw_iat_std|Standard deviation time between two packets sent in the forward direction|
|fw_iat_max|Maximum time between two packets sent in the forward direction|
|fw_iat_min|Minimum time between two packets sent in the forward direction|
|bw_iat_tot|Total time between two packets sent in the backward direction|
|bw_iat_avg|Mean time between two packets sent in the backward direction|
|bw_iat_std|Standard deviation time between two packets sent in the backward direction|
|bw_iat_max|Maximum time between two packets sent in the backward direction|
|bw_iat_min|Minimum time between two packets sent in the backward direction|
|fw_psh_flag|Number of times the PSH flag was set in packets travelling in the forward direction (0 for UDP)|
|bw_psh_flag|Number of times the PSH flag was set in packets travelling in the backward direction (0 for UDP)|
|fw_urg_flag|Number of times the URG flag was set in packets travelling in the forward direction (0 for UDP)|
|bw_urg_flag|Number of times the URG flag was set in packets travelling in the backward direction (0 for UDP)|
|fw_hdr_len|Total bytes used for headers in the forward direction|
|bw_hdr_len|Total bytes used for headers in the forward direction|
|fw_pkt_s|Number of forward packets per second|
|bw_pkt_s|Number of backward packets per second|
|pkt_len_min|Minimum length of a flow|
|pkt_len_max|Maximum length of a flow|
|pkt_len_avg|Mean length of a flow|
|pkt_len_std|Standard deviation length of a flow|
|pkt_len_va|Minimum inter-arrival time of packet|
|fin_cnt|Number of packets with FIN|
|syn_cnt|Number of packets with SYN|
|rst_cnt|Number of packets with RST|
|pst_cnt|Number of packets with PUSH|
|ack_cnt|Number of packets with ACK|
|urg_cnt|Number of packets with URG|
|cwe_cnt|Number of packets with CWE|
|ece_cnt|Number of packets with ECE|
|down_up_ratio|	Download and upload ratio|
|pkt_size_avg|Average size of packet|
|fw_seg_avg|Average size observed in the forward direction|
|bw_seg_avg|Average size observed in the backward direction|
|fw_byt_blk_avg|Average number of bytes bulk rate in the forward direction|
|fw_pkt_blk_avg|Average number of packets bulk rate in the forward direction|
|fw_blk_rate_avg|Average number of bulk rate in the forward direction|
|bw_byt_blk_avg|Average number of bytes bulk rate in the backward direction|
|bw_pkt_blk_avg|Average number of packets bulk rate in the backward direction|
|bw_blk_rate_avg|Average number of bulk rate in the backward direction|
|subfl_fw_pk|The average number of packets in a sub flow in the forward direction|
|subfl_fw_byt|The average number of bytes in a sub flow in the forward direction|
|subfl_bw_pkt|The average number of packets in a sub flow in the backward direction|
|subfl_bw_byt|The average number of bytes in a sub flow in the backward direction|
|fw_win_byt|Number of bytes sent in initial window in the forward direction|
|bw_win_byt|# of bytes sent in initial window in the backward direction|
|Fw_act_pkt|# of packets with at least 1 byte of TCP data payload in the forward direction|
|fw_seg_min|Minimum segment size observed in the forward direction|
|atv_avg|Mean time a flow was active before becoming idle|
|atv_std|Standard deviation time a flow was active before becoming idle|
|atv_max|Maximum time a flow was active before becoming idle|
|atv_min|Minimum time a flow was active before becoming idle|
|idl_avg|Mean time a flow was idle before becoming active|
|idl_std|Standard deviation time a flow was idle before becoming active|
|idl_max|Maximum time a flow was idle before becoming active|
|idl_min|Minimum time a flow was idle before becoming active|
