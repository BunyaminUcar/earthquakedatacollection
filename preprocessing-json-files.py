import os

folder_path = "C:/Users/UCAR/Desktop/Osmaniye/"

for root, dirs, files in os.walk(folder_path):
    print(folder_path)
    for file in files:
        if file.startswith(".") or not file.isdigit():
            continue
        file_path = os.path.join(root, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
        content = content[content.index("["):]
        new_file_path = os.path.splitext(file_path)[0] + ".json"
        with open(new_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        os.remove(file_path)
