import os
import re

def detect_missing_numbers(directory):
    # ファイル名から数値部分を抽出
    numbers = []
    for file_name in os.listdir(directory):
        match = re.search(r'dubai_(\d+)\.txt', file_name)
        if match:
            numbers.append(int(match.group(1)))
    
    # 数値をソートして連番チェック
    numbers.sort()
    missing_numbers = []
    for i in range(numbers[0], numbers[-1] + 1):
        if i not in numbers:
            missing_numbers.append(i)
    
    if missing_numbers:
        print(f"Missing numbers: {missing_numbers}")
    else:
        print("All files are sequential.")

# imagesディレクトリのパスを指定
images_directory = "/home/initial/dubai/txts"
detect_missing_numbers(images_directory)