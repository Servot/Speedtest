import subprocess
import datetime
from pathlib import Path

def append_to_log(timestamp, data):
    log_file_path = Path(__file__).parent / "speedtest_log.csv"
    if not log_file_path.exists():
        with log_file_path.open("a") as log_file:
            log_file.write('timestamp, ping, download_speed, upload_speed\n')
    ping, download, upload = data.splitlines()
    ping = float(ping.split(':')[1].replace(' ms', ''))
    download = float(download.split(':')[1].replace(' Mbit/s', ''))
    upload = float(upload.split(':')[1].replace(' Mbit/s', ''))
            
    with log_file_path.open("a") as log_file:
        log_file.write(f"{timestamp}, {ping}, {download}, {upload}\n")
        

def main():
    try:
        result = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        append_to_log(now, result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")
        with open("error_log.txt", "a") as error_log:
            error_log.write(f"{now} - {e}\n")
    
    


if __name__ == "__main__":
    main()
