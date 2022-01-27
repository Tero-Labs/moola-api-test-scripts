import requests
import json
from datetime import datetime


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


api_urls_with_parameters = json.load(open("../jsons/urls.json"))


def colored_status(status: str):
    if status == "OK":
        return Bcolors.OKGREEN + status + Bcolors.ENDC
    return Bcolors.FAIL + status + Bcolors.ENDC


def get_column_name(column: str):
    return Bcolors.OKCYAN + column + Bcolors.ENDC


def build_url(url: str, parameters: dict):
    return url + "?" + "&".join([f"{key}={value}" for key, value in parameters.items()])


now = datetime.now().strftime("%Y-%m-%d")
with open(f"../reports/api_urls-{now}.txt", "w") as f:
    for i, api_url_with_parameter in enumerate(api_urls_with_parameters):
        response = requests.get(
            api_url_with_parameter["url"], params=api_url_with_parameter["parameters"]
        )
        print(f"Serial No: {i+1}")
        if response.status_code < 400:
            status = colored_status("OK")
            response_json = response.json()
            response_status = response_json["status"]
            print(
                f"{get_column_name('url')}: {response.url}\n{get_column_name('status code')}: {response.status_code}\n{get_column_name('status')}: {colored_status(response_json['status'])}\n"
            )
            # f.write(
            #     f"{response.url} status code: {response.status_code} status: {response_status}\n {response_json}\n\n"
            # )
        else:
            print(
                f"{get_column_name('url')}: {response.url}\n{get_column_name('status code')}: {response.status_code}\nstatus: {colored_status('FAILED')}\n"
            )
            f.write(f"Serial No: {i+1}" + "\n")
            f.write(
                f"original url: {build_url(api_url_with_parameter['url'], api_url_with_parameter['parameters'])}\nrequest url: {response.url}\nstatus code: {response.status_code}\n\n"
            )
