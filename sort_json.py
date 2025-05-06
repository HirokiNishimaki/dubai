import json
import re

def sort_json_by_image_path(input_file, output_file):
    # JSONファイルの読み込み
    with open(input_file, "r") as f:
        data = json.load(f)
    
    # 数値部分を抽出してソート
    sorted_data = sorted(data, key=lambda x: int(re.search(r'\d+', x["image_path"]).group()))
    
    # ソートされたデータを新しいファイルに書き込み
    with open(output_file, "w") as f:
        json.dump(sorted_data, f, indent=4, ensure_ascii=False)

# 入力ファイルと出力ファイルのパスを指定
input_file = "bbox_data2.json"
output_file = "bbox_data2_sorted.json"
sort_json_by_image_path(input_file, output_file)