import requests
import json

codes = [  "AS",  "AR", "AM", "AU", "BS", "BB",  "BY",  "BR",  "CV",  "CA",  "KY",  "CL",  "CN",  "CX",  "CC",  "CO",  "CR",  "CU",  "EG",  "SV",  "PF",  "HM",  "HN",  "HK",  "IN",  "ID",  "IR",  "IQ",  "IE",  "IT",  "Italy",  "JM",  "JP",  "KZ",  "KI",  "MY",  "MH",  "MX",  "FM",  "MN",  "MZ",  "NR",  "NI",  "NG",  "NF",  "KP",  "MP",  "PW",  "PA",  "PG",  "PE",  "PH",  "RU",  "KN",  "SC",  "SO",  "KR",  "ES",  "SR",  "TW",  "TH",  "TR",  "TV",  "UA",  "AE",  "UM",  "US",  "UY",  "UZ",  "VE",  "VN",  "VI"]

for code in codes:
    url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=geonames-postal-code%40public&q=&facet=country_code&facet=admin_name1&facet=admin_code1&facet=admin_name2&refine.country_code=" + code

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "records" in data and data["records"]:
            first_record = data["records"][0]
            fields = first_record["fields"]
            country_code = fields["country_code"]
            postal_code_value = fields["postal_code"]
            place_name_value = fields["place_name"]
            result = {
                "country": country_code,
                "postalCode": postal_code_value,
                "city": place_name_value,
                "countryArea": ""
            }

            #print(result)
        else: print(code)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
