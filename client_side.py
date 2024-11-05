from SshToServer import SshToServer
import os 
import pandas as pd
import json

def requestDataFromServer():
    my_ssh = SshToServer(r"D:\Coding\HighTech-Course\Cloud-tech\my-key-pair.pem", "54.91.18.97", "ubuntu")
    stdout, stderr = my_ssh.runRemoteCommand("python3 /home/ubuntu/Linux-Final-Project/server_side.py")
    return stdoutToDict(stdout)


def stdoutToDict(output_string):
    json_string = output_string.replace("'", '"')
    response_dict = json.loads(json_string)
    return response_dict


def addDataToCsv(file_path, new_data_dict):
    new_data_df = pd.DataFrame([new_data_dict])
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_data_df], ignore_index=True)
        df.to_csv(file_path, index=False)
    else:
        new_data_df.to_csv(file_path, index=False)
    

CSV_PATH = r"D:\Coding\HighTech-Course\Cloud-tech\Linux-Final-Project\stats.csv"
res_from_server = requestDataFromServer()
addDataToCsv(CSV_PATH, res_from_server)
