import json

# ファイルパスを指定
input_file = "/home/initial/dubai/matched_output.json"
output_file = "/home/initial/dubai/unique_matched_output.json"

# JSONファイルを読み込む
with open(input_file, "r") as f:
    data = json.load(f)

# raw_image をキーにしてユニークなデータを保持
unique_data = {}
for entry in data:
    raw_image = entry["raw_image"]
    if raw_image not in unique_data:
        unique_data[raw_image] = entry

# ユニークなデータをリストに変換
unique_data_list = list(unique_data.values())

# 結果を新しいJSONファイルに保存
with open(output_file, "w") as f:
    json.dump(unique_data_list, f, indent=4)

print(f"Unique data has been saved to {output_file}")