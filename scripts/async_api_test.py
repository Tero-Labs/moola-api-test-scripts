import asyncio
import httpx

url = "http://v2-mooapi.herokuapp.com/get/getReserveData/total-activeUser-deposited-borrowed?currency=cEUR"

elapsed_time = []

async def send_requests():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        elapsed_time.append(response.elapsed.total_seconds())


async def main(num_of_requests):
    tasks = [asyncio.Task(send_requests()) for _ in range(num_of_requests)]
    await asyncio.gather(*tasks)
    average_time = sum(elapsed_time) / len(elapsed_time)
    print(f"API {url}\n# of requests {num_of_requests} took avg. {average_time} seconds\nMaximum time {max(elapsed_time)} seconds\nMinimum time {min(elapsed_time)} seconds")



asyncio.run(main(100))