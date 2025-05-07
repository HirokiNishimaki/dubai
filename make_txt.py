import json
import os

mapping_json = "/home/initial/detic_demo/Detic/mappping2.json"
output_dir = "txts2"

with open(mapping_json, "r") as f:
    mapping_data = json.load(f)


for i, mapping_entry in enumerate(mapping_data):
    if i < 1860:
        continue
    bbox_image = mapping_entry["bbox_image"].split("/")[-1]
    raw_image_path = mapping_entry["raw_image"]
    
    for entry in mapping_data:
        if entry["raw_image"] == raw_image_path:
            output_txt_file = bbox_image.replace(".png", ".txt")
            same_txt_file = entry["bbox_image"].split("/")[-1].replace(".png", ".txt")
            print(output_txt_file)
            print(same_txt_file)
            with open(os.path.join(output_dir, same_txt_file), "r") as f:
                lines = f.readlines()
            
            with open(os.path.join(output_dir, output_txt_file), "w") as f:
                f.writelines(lines)
            break
            
            # with open(os.path.join(output_dir, f"{raw_image_path}.txt"), "r") as f:
                