import multiprocessing
from moola_api_test import run_test_script

if __name__ == "__main__":
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=run_test_script, args = [])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()