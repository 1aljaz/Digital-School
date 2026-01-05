#!/usr/bin/env python3
"""
Hell Maze Generator (full CLI version with difficulty selection)

Save this file as run.py

Usage:
    python run.py

This script generates a complex directory tree for student exercises. Features:
 - nested folders (configurable depth & branching)
 - real & fake target files
 - binary junk files
 - hidden files (dotfiles)
 - optional AES-encrypted ZIP whose password is built from keywords in real targets (requires pyzipper)
 - automatically encrypted teacher manifest containing the actual student ZIP password
 - prompts for difficulty level at startup
 - optional symlink loops and permission-locked folders for highest difficulty
"""

import os
import random
import shutil
import stat
from zipfile import ZipFile, ZIP_DEFLATED

try:
    import pyzipper
except Exception:
    pyzipper = None

# -------------------------
# Helper functions
# -------------------------

def write_text_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def write_binary_file(path, size=128):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(os.urandom(size))


def random_folder_name(words):
    return random.choice(words) + "_" + str(random.randint(0, 9999))

# -------------------------
# Maze building routines
# -------------------------

def create_level(current_path, depth_left, branch, words, text_range, bin_range, created_folders,
                 fake_chance=0.4, hidden_chance=0.15):
    created_folders.append(current_path)

    for i in range(random.randint(*text_range)):
        write_text_file(os.path.join(current_path, f"note_{i}.txt"),
                        f"Normal note in {os.path.basename(current_path)}.\n")

    for i in range(random.randint(*bin_range)):
        write_binary_file(os.path.join(current_path, f"junk_{i}.bin"), size=random.randint(16, 512))

    if random.random() < fake_chance:
        ext = random.choice([".log", ".dat", ".tmp"])
        write_text_file(os.path.join(current_path, f"misc_{random.randint(0,999)}{ext}"),
                        "useless noise\n" * random.randint(1, 3))

    if random.random() < hidden_chance:
        write_text_file(os.path.join(current_path, f".hidden_note_{random.randint(0,999)}"),
                        "shhh hidden note\n")

    if depth_left > 0:
        for _ in range(branch):
            folder_path = os.path.join(current_path, random_folder_name(words))
            os.makedirs(folder_path, exist_ok=True)
            create_level(folder_path, depth_left - 1, branch, words, text_range, bin_range, created_folders,
                         fake_chance=fake_chance, hidden_chance=hidden_chance)

# -------------------------
# Encrypted ZIP helper
# -------------------------

def create_encrypted_zip_aes(zip_folder, zip_filename, target_filepaths, keywords_map, password_join="", zip_entries=3):
    if pyzipper is None:
        raise RuntimeError("pyzipper is required for encrypted zips. Install: pip install pyzipper")

    def extract_index(fp):
        base = os.path.basename(fp)
        parts = base.split("_")
        for part in reversed(parts):
            try:
                return int(part.split(".")[0])
            except Exception:
                continue
        return 0

    ordered = sorted(target_filepaths, key=extract_index)
    keywords_in_order = [keywords_map.get(p, "") for p in ordered]

    password = password_join.join(keywords_in_order)

    zip_path = os.path.join(zip_folder, zip_filename)
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode('utf-8'))
        for i in range(zip_entries):
            arcname = f"zip_target_{i}.txt"
            data = f"✅ ZIP REAL TARGET #{i}\nHidden inside an AES-encrypted zip.\n"
            zf.writestr(arcname, data.encode('utf-8'))

    return zip_path, password, ordered

# -------------------------
# Encrypt teacher manifest
# -------------------------

def encrypt_teacher_manifest(manifest_path, password="P@ssword123!"):
    zip_path = manifest_path.replace(".txt", ".enc.zip")
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode('utf-8'))
        zf.write(manifest_path, arcname=os.path.basename(manifest_path))
    os.remove(manifest_path)
    return zip_path, password

# -------------------------
# Difficulty settings
# -------------------------

def get_difficulty_settings():
    print("Select difficulty level:")
    print("1 - Super Easy")
    print("2 - Easy")
    print("3 - Medium")
    print("4 - Hard")
    print("5 - Insanity")

    while True:
        try:
            choice = int(input("Enter difficulty number (1-5): "))
            if choice in range(1, 6):
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    settings_map = {
        1: {'depth': 2, 'branch': 2, 'real': 5, 'fake': 5, 'hidden': 1, 'symlinks': False, 'chmod000': False},
        2: {'depth': 3, 'branch': 3, 'real': 10, 'fake': 15, 'hidden': 2, 'symlinks': False, 'chmod000': False},
        3: {'depth': 4, 'branch': 4, 'real': 20, 'fake': 40, 'hidden': 4, 'symlinks': False, 'chmod000': False},
        4: {'depth': 5, 'branch': 5, 'real': 35, 'fake': 100, 'hidden': 6, 'symlinks': True, 'chmod000': False},
        5: {'depth': 6, 'branch': 6, 'real': 50, 'fake': 200, 'hidden': 8, 'symlinks': True, 'chmod000': True},
    }

    return settings_map[choice], choice

# -------------------------
# Main
# -------------------------

def main():
    diff_settings, diff_choice = get_difficulty_settings()

    base = "hell_maze"
    os.makedirs(base, exist_ok=True)
    created_folders = []

    random.seed(42)

    words = ["alpha","bravo","charlie","delta","omega","zeta","nova","kappa","tau","sigma",
             "luna","orion","pegasus","hydra","vortex","myst","ember","iron","cobalt","neon"]

    create_level(base, diff_settings['depth'], diff_settings['branch'], words,
                 text_range=(1,3), bin_range=(0,2), created_folders=created_folders)

    real_targets_paths = []
    real_target_keywords = {}
    possible_places = created_folders.copy()
    random.shuffle(possible_places)

    placed = 0
    idx = 0
    while placed < diff_settings['real'] and idx < len(possible_places):
        place = possible_places[idx]; idx += 1
        fname = f"target_REAL_{placed}.txt"
        fpath = os.path.join(place, fname)
        keyword = random.choice(words) + str(random.randint(0, 99))
        content = f"✅ REAL TARGET #{placed}\nSecret token: {random.getrandbits(56):x}\nKEYWORD: {keyword}\n"
        write_text_file(fpath, content)
        real_targets_paths.append(fpath)
        real_target_keywords[fpath] = keyword
        placed += 1

    hidden_count = min(diff_settings['hidden'], len(created_folders))
    random.shuffle(created_folders)
    for i in range(hidden_count):
        place = created_folders[i]
        fname = f".target_hidden_{i}.txt"
        fpath = os.path.join(place, fname)
        keyword = random.choice(words) + str(random.randint(0, 99))
        content = f"✅ HIDDEN REAL TARGET #{i}\nKEYWORD: {keyword}\n"
        write_text_file(fpath, content)
        real_targets_paths.append(fpath)
        real_target_keywords[fpath] = keyword

    for _ in range(diff_settings['fake']):
        place = random.choice(created_folders)
        fname = f"target_fake_{random.randint(0,999)}.txt"
        fpath = os.path.join(place, fname)
        write_text_file(fpath, "❌ FAKE TARGET — ignore me.\n")

    # Encrypted student ZIP in root
    if pyzipper is not None:
        available_real = [p for p in real_targets_paths if p in real_target_keywords]
        selected = random.sample(available_real, min(4, len(available_real)))
        zip_folder_enc = base
        zip_filename_enc = "archive_locked.zip"
        zip_path, zip_password, _ = create_encrypted_zip_aes(
            zip_folder_enc, zip_filename_enc, selected, real_target_keywords, password_join="", zip_entries=3
        )
    else:
        zip_password = None

    # Optional symlink loops and chmod 000 for Insanity
    if diff_choice == 5:
        if os.name == 'posix':
            for folder in created_folders[:5]:  # create some symlink loops
                try:
                    target = folder
                    link_name = os.path.join(folder, f"loop_link_{random.randint(0,99)}")
                    os.symlink(target, link_name)
                    os.chmod(folder, 0o000)
                except Exception:
                    pass

    # Teacher manifest
    manifest_path = "teacher_manifest.txt"
    with open(manifest_path, "w", encoding="utf-8") as mf:
        mf.write("Teacher Manifest — REAL targets\n\n")
        for p in real_targets_paths:
            mf.write(p + "\n")
        mf.write("\nReal target keywords:\n")
        for p, k in real_target_keywords.items():
            mf.write(f"{p}  KEYWORD: {k}\n")
        if zip_password:
            mf.write(f"\nSTUDENT ZIP PASSWORD: {zip_password}\n")

    if pyzipper is not None:
        zip_path_enc, password_enc = encrypt_teacher_manifest(manifest_path)
        print(f"[+] Teacher manifest encrypted at: {zip_path_enc}")
    else:
        print("[!] pyzipper not installed; teacher manifest is not encrypted.")

if __name__ == '__main__':
    main()