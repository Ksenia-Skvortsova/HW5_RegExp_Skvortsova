import re
import os 


def to_salce_lan(text, consonant="c"):
    """translate from Russian to salty language"""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = ""

    for char in text:
        result += char
        if char in vowels:
            result += consonant + char.lower()
    
    return result 


def extract_chords(file_path):
    """Extract all chords from songs file"""
    chords = set()
    pattern = r'\b[A-G][a-zbm#]*\b'

    with open(file_path, 'r') as file:
        for line in file:
            found = re.findall(pattern, line)
            for chord in found:
                chords.add(chord)
    return chords


def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    """Copy and rename files"""
    if sample_names is None:
        sample_names = {}

    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)

        if not os.path.isfile(filepath):
            continue

        if not re.search(pattern, filename):
            continue

        new_filename = filename

        if new_pattern is not None:
            new_filename = re.sub(pattern, new_pattern, new_filename) 

        for old, new in sample_names.items():
            new_filename = new_filename.replace(old, new)

        if filename == new_filename:
            continue

        new_filepath = os.path.join(dir, new_filename)

        if to_replace:
            os.rename(filepath, new_filepath)
        else:
            with open(filepath, 'rb') as f1, open(new_filepath, 'wb') as f2:
                f2.write(f1.read())