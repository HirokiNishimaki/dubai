import json
import os

# ファイルパスを指定
mapping_output_path = "/home/initial/dubai/mapping_output.json"
dubai_database_ocr_path = "/home/initial/dubai/dubai_database_ocr.json"
output_path = "/home/initial/dubai/matched_output.json"

# JSONファイルを読み込む
with open(mapping_output_path, "r") as f:
    mapping_output = json.load(f)

with open(dubai_database_ocr_path, "r") as f:
    dubai_database_ocr = json.load(f)

# マッチング処理
matched_data = []
for mapping_entry in mapping_output:
    original_path = mapping_entry["original_path"]
    raw_image_path = mapping_entry["raw_image"]
    raw_image = os.path.basename(original_path)  # ファイル名を取得
    data_image_path = os.path.join("data", "dubai", raw_image)

    # dubai_database_ocr で一致するエントリを探す
    for ocr_entry in dubai_database_ocr:
        if ocr_entry["image_path"] == data_image_path:
            matched_data.append({
                "raw_image": raw_image_path,
                "ocr_results": ocr_entry["ocr_results"]
            })
            break  # 一致が見つかったら次の mapping_entry に進む

# 結果を新しいJSONファイルに保存
with open(output_path, "w") as f:
    json.dump(matched_data, f, indent=4)

print(f"Matched data has been saved to {output_path}")