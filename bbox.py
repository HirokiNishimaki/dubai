import cv2
import numpy as np
import os
import json

# 画像が入ってるディレクトリ
image_dir = 'bbox'
# bboxを描画した画像を保存するディレクトリ
bbox_dir = 'b'
# 出力するjsonファイル名
output_json = 'bbox_data2.json'

# bboxディレクトリがなかったら作る
os.makedirs(bbox_dir, exist_ok=True)

# 書き込む内容をためるリスト
results = []

# 画像ファイル一覧を取得
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Warning: {image_path} could not be read, skipping.")
        continue

    # 純粋な緑 (#00FF00) だけを抽出
    lower_green = np.array([0, 0, 255])
    upper_green = np.array([0, 0, 255])
    mask = cv2.inRange(image, lower_green, upper_green)

    # 輪郭検出
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print(f"No bbox found in {image_file}")
        continue

    # 最大の輪郭を取る
    cnt = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cnt)
    x_min = int(x)
    y_min = int(y)
    x_max = int(x + w)
    y_max = int(y + h)

    # 1件分のデータを作る
    result = {
        "image_path": image_file,
        "bbox": [x_min, y_min, x_max, y_max]
    }
    results.append(result)

    # 元画像にbboxを描画
    image_with_bbox = image.copy()
    cv2.rectangle(image_with_bbox, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # bbox/ ディレクトリに保存
    save_path = os.path.join(bbox_dir, image_file)
    cv2.imwrite(save_path, image_with_bbox)

# 全部まとめてJSONファイルに保存
with open(output_json, 'w') as f:
    json.dump(results, f, indent=4)

print(f"Saved bbox info to {output_json}")
print(f"Saved images with bbox to {bbox_dir}/")
