from urllib.parse import urlparse
import os
import json
import pandas as pd
import requests

data = ""

ilce_json_yolu = "C:/Users/UCAR/Desktop/adiyaman-diyarbakır-il-ilçeler-json/adıyaman-json/adıyaman-samsat.json"
image_folder = "C:/Users/UCAR/Desktop/Adıyaman/Samsat"

with open(ilce_json_yolu, "r", encoding="utf-8") as f:
    data = json.load(f)

for json_verisi in data:
  # burada json_verisi üzerinde işlemler yapabilirsiniz
  askiKodu = json_verisi['askiKodu']
  yapi_kimlik_no = json_verisi['yapi_kimlik_no']
  il = json_verisi['il']
  ilce = json_verisi['ilce']
  mahalle = json_verisi['mahalle']
  aciklama = json_verisi['aciklama']
  foto = json_verisi['fotograflar']

  df = pd.DataFrame(data)

  if foto:
      for i, j in zip(foto, range(len(foto))):
          parse = urlparse(i)
          print(foto)
          if parse.scheme in ['http', 'https'] and requests.get(i).status_code == 200:
              dosya_adi1 = f"{askiKodu}-{yapi_kimlik_no}-{il}-{ilce}-{mahalle}-{aciklama}-{j}.jpg"
              dosya_yolu = os.path.join(image_folder, dosya_adi1)

              with open(dosya_yolu, "wb") as f:
                  f.write(requests.get(i).content)
          else:
              print("Fotoğraf Bulunamadı")