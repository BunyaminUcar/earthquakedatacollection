from urllib.parse import urlparse
import requests
import json
import pandas as pd


url_iller = "https://hasartespit.csb.gov.tr/query/cities"

response_iller = requests.get(url_iller)
data_iller = json.loads(response_iller.content)
cities = data_iller['items']

for city in cities:
    city_id = city['id']
    city_name = city['ad']
    url_ilce = f"https://hasartespit.csb.gov.tr/query/counties?cityId="+ str(city_id)

    response_ilce = requests.get(url_ilce)
    data_ilce = json.loads(response_ilce.content)
    counties = data_ilce['items']

    for county in counties:
        county_id = county['id']
        county_name = county['ad']
        url_mahalleler = f"https://hasartespit.csb.gov.tr/query/districts?countyId="+str(county_id)
        print(city_name,county_name)
        if city_name == "Kahramanmaraş" and county_name == "Karakoçan":
            pass
        else:
            response_mahalle = requests.get(url_mahalleler)
            data_mahalle = json.loads(response_mahalle.content)
            mahalleler = data_mahalle['items']

            for mahalle in mahalleler:
                mahalle_id = mahalle['mahalleId']
                mahalle_name = mahalle['ad']
                url_binalar = f"https://hasartespit.csb.gov.tr/query/AddressQuery?IlId="+str(city_id)+"&IlceId="+str(county_id)+"&MahalleId="+str(mahalle_id)

                response_bina = requests.get(url_binalar)
                data_bina = json.loads(response_bina.content)
                """print(f"City: {}, County: {county_name}, Mahalle: {mahalle_name}")"""
                
                

                null = "null"

                s = dict(data_bina[0])
                il = s['il']
                ilce = s['ilce']
                mahalle = s['mahalle']
                foto=s['fotograflar']
                uid=s['uid']
                yapi_kimlik_no=s['yapi_kimlik_no']
                dosya_adi = f"{il}-{ilce}-{mahalle}.xlsx"
                df = pd.DataFrame(data_bina)
                df.to_excel(dosya_adi, index=False)
                

                if foto:
                    for i, j in zip(foto, range(len(foto))):
                        parse=urlparse(i)
                        if parse.scheme in ['http', 'https'] and requests.get(i).status_code == 200:
                            dosya_adi1 = f"{il}-{ilce}-{mahalle}-{uid}-{yapi_kimlik_no}-{j}.jpg"
                            with open(dosya_adi1, "wb") as f:
                                f.write(requests.get(i).content)
                        else:
                            print("Fotoğraf Bulunamadı")



