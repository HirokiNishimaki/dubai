import json

def compare_json_files(file1, file2):
    # JSONファイルを読み込み
    with open(file1, "r") as f1, open(file2, "r") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    # 比較結果を格納するリスト
    differences = []

    # 再帰的に辞書を比較する関数
    def compare_dicts(d1, d2, path=""):
        for key in d1.keys():
            if key not in d2:
                differences.append(f"Key '{path + key}' is missing in the second JSON.")
            elif d1[key] != d2[key]:
                if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    compare_dicts(d1[key], d2[key], path + key + ".")
                else:
                    differences.append(f"Value of '{path + key}' differs: {d1[key]} != {d2[key]}")
        for key in d2.keys():
            if key not in d1:
                differences.append(f"Key '{path + key}' is missing in the first JSON.")

    # 比較を開始
    if isinstance(data1, dict) and isinstance(data2, dict):
        compare_dicts(data1, data2)
    elif isinstance(data1, list) and isinstance(data2, list):
        for i, (item1, item2) in enumerate(zip(data1, data2)):
            if item1 != item2:
                differences.append(f"Difference in list at index {i}: {item1} != {item2}")
        if len(data1) != len(data2):
            differences.append(f"List lengths differ: {len(data1)} != {len(data2)}")
    else:
        differences.append(f"Root types differ: {type(data1)} != {type(data2)}")

    # 結果を出力
    if differences:
        print("Differences found:")
        for diff in differences:
            print(diff)

    else:
        print("The two JSON files are identical.")

# ファイルパスを指定
file1 = "/home/initial/dubai/mapping.json"
file2 = "/home/initial/dubai/mapping_output.json"

compare_json_files(file1, file2)