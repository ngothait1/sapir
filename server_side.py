import subprocess
import json

def runLocalCommand(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr}")


def statisticSyslogFile():
    search_words = ["ERROR", "WARN", "INFO"]
    response_to_client = {}
    response_to_client["timestamp"] = runLocalCommand(f"date +%s")[0].strip()
    for word in search_words:
        response = runLocalCommand(f'grep  "{word}" /var/log/syslog | wc -l')
        response_to_client[word] = response[0].strip()
    return response_to_client


statisticSyslogFile()