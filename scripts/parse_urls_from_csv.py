import pandas
import json
from datetime import datetime


def parse_url(url: str):
    """
    Parse the url and return the hostname and the path
    """
    user_public_key = "dEdfe7c341ffcB43C26bdb17d6A59C2317907f36"
    split_url = url.split("?")
    root_url = split_url[0]
    parameters = None
    try:
        parameters = split_url[1].split("&")
    except IndexError:
        parameters = []
    json_url = {
        "url": root_url,
        "parameters": {
            parameter.split("=")[0]: parameter.split("=")[1] for parameter in parameters
        },
    }
    if json_url["parameters"].get("userPublicKey"):
        json_url["parameters"]["userPublicKey"] = user_public_key
    return json_url


url_csv_df = pandas.read_csv("../csvs/moola-api-2021-10-14_18:55:31.csv")

json_urls = []
for url in url_csv_df["Alfajores test"]:
    if isinstance(url, str):
        json_urls.append(parse_url(url))

now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
json.dump(json_urls, open(f"../jsons/urls-{now}.json", "w"))
