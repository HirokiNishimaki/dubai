import json
import os

def change_paths(input_file, output_file, raw_base_path, bbox_base_path):
    # JSONファイルの読み込み
    with open(input_file, "r") as f:
        data = json.load(f)
    
    # パスを変更
    for item in data:
        # raw_imageのパスを変更
        raw_filename = os.path.basename(item["raw_image"])
        item["raw_image"] = os.path.join(raw_base_path, raw_filename)
        
        # bbox_imageのパスを変更
        bbox_filename = os.path.basename(item["bbox_image"])
        item["bbox_image"] = os.path.join(bbox_base_path, bbox_filename)
    
    # 変更後のデータを新しいファイルに書き込み
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 入力ファイルと出力ファイルのパスを指定
input_file = "/home/initial/dubai/mapping_output.json"
output_file = "/home/initial/dubai/mapping_output2.json"

# 新しいベースパスを指定
raw_base_path = "/home/initial/dubai/raw"
bbox_base_path = "/home/initial/dubai/images"

change_paths(input_file, output_file, raw_base_path, bbox_base_path)