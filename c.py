import os
import shutil

def shift_and_copy_images(directory, target_index):
    # ファイル名を取得し、数値部分でソート
    files = sorted(
        [f for f in os.listdir(directory) if f.startswith("dubai_") and f.endswith(".png")],
        key=lambda x: int(x.split("_")[1].split(".")[0])
    )
    
    # 対象インデックスの画像をコピー
    target_file = f"dubai_{target_index}.png"
    if target_file not in files:
        print(f"File {target_file} not found in the directory.")
        return
    
    # コピー先のファイル名
    copied_file = f"dubai_{target_index + 1}.png"
    shutil.copy(os.path.join(directory, target_file), os.path.join(directory, copied_file))
    print(f"Copied {target_file} to {copied_file}")
    
    # インデックスを繰り下げ（コピーしたファイル以降を処理）
    for i in range(len(files) - 1, target_index, -1):
        current_file = files[i]
        current_index = int(current_file.split("_")[1].split(".")[0])
        new_file = f"dubai_{current_index + 1}.png"
        
        # コピーしたファイルをスキップ
        if current_file == copied_file:
            continue
        
        os.rename(os.path.join(directory, current_file), os.path.join(directory, new_file))
        print(f"Renamed {current_file} to {new_file}")

# ディレクトリと対象インデックスを指定
directory = "/home/initial/dubai/b"
target_index = 1544  # コピーしたい画像のインデックス
shift_and_copy_images(directory, target_index)