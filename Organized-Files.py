import os
import shutil

# përcaktoni drejtoritë e burimit dhe destinacionit
src_dir = input("Vendosni lokacionin ku ndodhen të dhënat:  ")
dest_dir = input("Vendosni lokacionin ku doni t'i zhvendosni:  ")

# krijoni drejtoritë e destinacionit për lloje të ndryshme skedarësh
os.makedirs(os.path.join(dest_dir, "Images"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "Videos"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "Audios"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "Documents"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "Software"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "Other"), exist_ok=True)

# iterate mbi skedarët në drejtorinë burimore
for file_name in os.listdir(src_dir):
    # merrni shtegun e plotë të skedarit
    src_file_path = os.path.join(src_dir, file_name)
    # kontrolloni llojin e skedarit dhe zhvendoseni në drejtorinë përkatëse të destinacionit
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        shutil.move(src_file_path, os.path.join(dest_dir, "Images"))
    elif file_name.endswith(".mp4") or file_name.endswith(".avi"):
        shutil.move(src_file_path, os.path.join(dest_dir, "Videos"))
    elif file_name.endswith(".mp3") or file_name.endswith(".wav"):
        shutil.move(src_file_path, os.path.join(dest_dir, "Audios"))
    elif file_name.endswith(".doc") or file_name.endswith(".pdf"):
        shutil.move(src_file_path, os.path.join(dest_dir, "Documents"))
    elif file_name.endswith(".exe") or file_name.endswith(".msi"):
        shutil.move(src_file_path, os.path.join(dest_dir, "Software"))
    else:
        shutil.move(src_file_path, os.path.join(dest_dir, "Other"))

print("Skendarët-(Files) u zhvendosën me sukses !")
