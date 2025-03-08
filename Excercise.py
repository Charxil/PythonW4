import pandas as pd
import requests

raw_url = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/latest/owid-covid-latest.json"
raw_data = requests.get(raw_url).json()

# single_country_df = pd.json_normalize(raw_data["AFG"])
# print(single_country_df.head())
# print(single_country_df.shape)

all_countries = pd.DataFrame()

for country_short_code in raw_data.keys():
    print(f"Getting data for this {country_short_code}")
    single_country_df = pd.json_normalize(raw_data[country_short_code])
    single_country_df['country_code'] = country_short_code

    all_countries = pd.concat([all_countries, single_country_df], ignore_index=True)
#     print(single_country_df.shape)
#     break
#     # print(single_country_df.head())
#     # print(single_country_df.columns)

print("==================================================")
print(all_countries.shape)
print("==================================================")
print(all_countries.columns)
print("==================================================")
print(all_countries.head())
#
# print(all_countries.to_csv("all_countries.csv"))

