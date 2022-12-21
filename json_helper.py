import requests
import json

#codes = [  "AS",  "AR", "AM", "AU", "BS", "BB",  "BY",  "BR",  "CV",  "CA",  "KY",  "CL",  "CN",  "CX",  "CC",  "CO",  "CR",  "CU",  "EG",  "SV",  "PF",  "HM",  "HN",  "HK",  "IN",  "ID",  "IR",  "IQ",  "IE",  "IT",  "Italy",  "JM",  "JP",  "KZ",  "KI",  "MY",  "MH",  "MX",  "FM",  "MN",  "MZ",  "NR",  "NI",  "NG",  "NF",  "KP",  "MP",  "PW",  "PA",  "PG",  "PE",  "PH",  "RU",  "KN",  "SC",  "SO",  "KR",  "ES",  "SR",  "TW",  "TH",  "TR",  "TV",  "UA",  "AE",  "UM",  "US",  "UY",  "UZ",  "VE",  "VN",  "VI"]
values = ["AM", "BS", "BB", "CV", "KY", "CN", "CX", "CC", "CU", "EG", "SV", "PF", "HM", "HN", "HK", "ID", "IR", "IQ", "JM", "KZ", "KI", "MN", "MZ", "NR", "NI", "NG", "NF", "KP", "PA", "PG", "KN", "SC", "SO", "SR", "TW", "TV", "AE", "UM", "UZ", "VE", "VN"]

for code in values:
    url = "https://www.gstatic.com/chrome/autofill/libaddressinput/chromium-i18n/ssl-address/data/" + code

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        key = data["key"]
        name = data["name"]
        #first_record = data["records"][0]
        #fields = first_record["fields"]
        #country_code = fields["country_code"]
        #postal_code_value = fields["postal_code"]
        #place_name_value = fields["place_name"]
        result = {
            "country": key,
            "postalCode": "",
            "city": name,
            "countryArea": ""
        }
        
        print(result)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
