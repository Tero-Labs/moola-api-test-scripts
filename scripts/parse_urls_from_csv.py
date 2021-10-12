import pandas
import json


def parse_url(url: str):
    """
    Parse the url and return the hostname and the path
    """
    user_public_key = "f6ededceff0bc515506a55cbb487c900ac19cbfb"
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


url_csv_df = pandas.read_csv("../csvs/Moola V2 mainnet API Testing - Moola-Api.csv")

json_urls = []
for url in url_csv_df["Mainnet test"]:
    if isinstance(url, str):
        json_urls.append(parse_url(url))

json.dump(json_urls, open("../jsons/urls.json", "w"))
