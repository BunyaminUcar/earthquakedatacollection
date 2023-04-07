#Tüm şehri birleştirme   
import os
import json

folder_path = "C:/Users/UCAR/Desktop/Osmaniye"  # Klasör yolunu belirtin
result = []

# Tüm alt klasörleri dolaşarak JSON dosyalarını bulun ve birleştirin
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.json'):  # Sadece JSON dosyalarını seçin
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = json.load(f)
                result.extend(data)

# Tüm JSON dosyalarını birleştirin
with open('merged_data.json', 'w') as f:
    json.dump(result, f)
    
    
    
    
    
    
    
#Tüm ilçeyi birleştirme
#Sadece tek bir klasör seçilmeli !!!!!!
import os
import json

# Klasör yolunu belirtin
folder_path = "C:/Users/UCAR/Desktop/Osmaniye"

# Birleştirilecek sonuç verisini tutmak için boş bir liste oluşturun
result = []

# Klasördeki tüm dosyaları tarayın
for file_name in os.listdir(folder_path):
    # Dosyanın JSON olup olmadığını kontrol edin
    if file_name.endswith(".json"):
        # JSON dosyasını okuyun
        with open(os.path.join(folder_path, file_name), "rb") as f:
            data = json.load(f)
            # Verileri sonuç listesine ekleyin
            result.extend(data)

# Sonuç verilerini tek bir JSON dosyasına yazın
with open("merged.json", "w") as f:
    json.dump(result, f)
