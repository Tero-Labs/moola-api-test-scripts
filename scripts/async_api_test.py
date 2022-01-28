import asyncio
import httpx
from multiprocessing import Pool, cpu_count
import requests

DO_SERVER = "http://moola-v2-py-api.universalmachine.io"
HEROKU_SERVER = "https://v2-mooapi.herokuapp.com"

# url = f"{HEROKU_SERVER}/get/getReserveData/total-activeUser-deposited-borrowed?currency=cUSD"
url = f"{DO_SERVER}/get/getReserveData/total-activeUser-deposited-borrowed?currency=cUSD"

elapsed_time = []

async def send_requests():
    async with httpx.AsyncClient(timeout=50) as client:
        response = await client.get(url)
        elapsed_time.append(response.elapsed.total_seconds())


async def main(num_of_requests):
    tasks = [asyncio.Task(send_requests()) for _ in range(num_of_requests)]
    await asyncio.gather(*tasks)
    average_time = sum(elapsed_time) / len(elapsed_time)
    print(f"[ASYNC] API {url}\n# of requests {num_of_requests} took avg. {average_time} seconds\nMaximum time {max(elapsed_time)} seconds\nMinimum time {min(elapsed_time)} seconds")


asyncio.run(main(2000))

# number_of_requests = 1

# for _ in range(number_of_requests):
#     response = requests.get(url)
#     elapsed_time.append(response.elapsed.total_seconds())

# average_time = sum(elapsed_time) / len(elapsed_time)

# print(f"[SYNC] API {url}\n# of requests {number_of_requests} took avg. {average_time} seconds\nMaximum time {max(elapsed_time)} seconds\nMinimum time {min(elapsed_time)} seconds")