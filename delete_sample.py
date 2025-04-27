import os
import shutil
import json

# 設定
delete_indices = [435, 455, 832, 833, 957, 958, 987, 1068, 1069, 1143, 1159, 1192, 1300, 1301, 1304, 1362, 1545]  # <- 複数に対応！
delete_indices = sorted(delete_indices)  # 念のため昇順にしておく

images_dir = "/home/initial/dubai/images"
txts_dir = "/home/initial/dubai/txts"

# 対象ファイルを削除
for idx in delete_indices:
    img_path = os.path.join(images_dir, f"dubai_{idx}.png")
    txt_path = os.path.join(txts_dir, f"dubai_{idx}.txt")
    if os.path.exists(img_path):
        os.remove(img_path)
    if os.path.exists(txt_path):
        os.remove(txt_path)

# ファイル一覧を取得
image_files = sorted(
    [f for f in os.listdir(images_dir) if f.startswith("dubai_") and f.endswith(".png")]
)
txt_files = sorted(
    [f for f in os.listdir(txts_dir) if f.startswith("dubai_") and f.endswith(".txt")]
)

# 繰り上げ処理
def get_shifted_index(idx, delete_indices):
    """与えられたidxに対して、何個分ずれるか計算する"""
    shift = sum(1 for d in delete_indices if d < idx)
    return idx - shift

for img_file in image_files:
    idx = int(img_file.split("_")[1].split(".")[0])
    if idx > delete_indices[0]:  # 最小の削除インデックスより大きいものだけ
        new_idx = get_shifted_index(idx, delete_indices)
        src = os.path.join(images_dir, img_file)
        dst = os.path.join(images_dir, f"dubai_{new_idx}.png")
        shutil.move(src, dst)

for txt_file in txt_files:
    idx = int(txt_file.split("_")[1].split(".")[0])
    if idx > delete_indices[0]:
        new_idx = get_shifted_index(idx, delete_indices)
        src = os.path.join(txts_dir, txt_file)
        dst = os.path.join(txts_dir, f"dubai_{new_idx}.txt")
        shutil.move(src, dst)

# JSONファイル読み込み
with open("mapping_output.json", "r") as f:
    data = json.load(f)

new_data = []
for item in data:
    path = item["bbox_image"]
    filename = os.path.basename(path)
    idx = int(filename.split("_")[1].split(".")[0])

    if idx in delete_indices:
        continue  # 削除対象はスキップ
    new_idx = get_shifted_index(idx, delete_indices)
    new_filename = f"dubai_{new_idx}.png"
    new_path = os.path.join(os.path.dirname(path), new_filename)
    item["bbox_image"] = new_path
    new_data.append(item)

# JSONファイル保存
with open("mapping1.json", "w") as f:
    json.dump(new_data, f, indent=2)
