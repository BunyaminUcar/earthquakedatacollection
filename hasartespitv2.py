from urllib.parse import urlparse

import pandas as pd
import requests

data = "dd"
print(type(data))


for alt_liste in data:
  for json_verisi in alt_liste:
    # burada json_verisi üzerinde işlemler yapabilirsiniz
    il = json_verisi['il']
    ilce = json_verisi['ilce']
    mahalle = json_verisi['mahalle']
    sokak = json_verisi['sokak']
    binaNo = json_verisi['binaNo']
    foto = json_verisi['fotograflar']
    uid = json_verisi['uid']
    yapi_kimlik_no = json_verisi['yapi_kimlik_no']
    dosya_adi = f"{il}-{ilce}-{mahalle}.xlsx"
    df = pd.DataFrame(data)
    """df.to_excel(dosya_adi, index=False)"""

    if foto:
        for i, j in zip(foto, range(len(foto))):
            parse = urlparse(i)
            if parse.scheme in ['http', 'https'] and requests.get(i).status_code == 200:
                dosya_adi1 = f"{il}-{ilce}-{mahalle}-{uid}-{yapi_kimlik_no}-{j}.jpg"
                with open(dosya_adi1, "wb") as f:
                    f.write(requests.get(i).content)
            else:
                print("Fotoğraf Bulunamadı")