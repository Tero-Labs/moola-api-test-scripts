# Moola test script

This repository contains automated test script for moola api endpoints.

## How to use

1. Clone the repository

   ```bash
    git clone https://github.com/Tero-Labs/moola-api-test-scripts.git
    ```

2. Create virtual environment and activate it

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Go to directory `scripts` and run `moola_api_test.py`

    ```bash
    cd scripts
    python test_apis.py
    ```

5. Any failing api will be printed to stdout and a report will be generated under `reports` directory for the failing apis
