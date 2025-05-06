import json
import os

def main(json_path, output_json_path, dubai_path):
    # mapping.jsonの読み込み
    with open(json_path, "r") as f:
        mapping_data = json.load(f)

    # filtered_output.jsonの読み込み
    with open(dubai_path, "r") as f:
        dubai_data = json.load(f)

    for i, item in enumerate(mapping_data):
        raw_image_path = item["raw_image"]
        file_name = os.path.basename(raw_image_path)
        index = int(file_name.split("_")[1].split(".")[0])
        dubai_image_path = dubai_data[index]["image_path"]
        mapping_data[i]["original_path"] = dubai_image_path

    with open(output_json_path, "w") as f:
        json.dump(mapping_data, f, indent=4, ensure_ascii=False)
    print(f"Output written to {output_json_path}")
    
    


if __name__ == "__main__":
    json_path = "/home/initial/dubai/mapping.json"
    output_json_path = "/home/initial/dubai/mapping_output.json"
    dubai_path = "/home/initial/detic_demo/Detic/filtered_output.json"
    main(json_path, output_json_path, dubai_path)