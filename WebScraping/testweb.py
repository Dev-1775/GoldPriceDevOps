from flask import Flask, Response
import requests
from bs4 import BeautifulSoup
import re
import os

app = Flask(__name__)

def extract_digits(currency_string):
    digits = re.findall(r'\d+\.?\d*', currency_string)
    return ''.join(digits) if digits else None

def fetch_gold_prices():
    currencies = []
    countries = []
    url = 'https://pricegold.net/world/'
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find('div', class_='table-responsive').find('table')
        rows = table.find_all('tr')[1:]

        for row in rows:
            columns = row.find_all('td')
            country = columns[0].text.strip()
            rate = columns[4].text.strip()
            countries.append(country)
            currencies.append(rate)
    return countries, currencies

@app.route('/metrics', methods=['GET'])
def metrics():
    countries, currencies = fetch_gold_prices()
    metric_output = "# HELP gold_price Price of gold in various countries\n"
    for country, currency in zip(countries, currencies):
        price = extract_digits(currency)
        if price:
            metric_output += f"gold_price{{country=\"{country}\"}} {price}\n"
    return Response(metric_output, mimetype="text/plain")

def save_data_to_file(data, file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass

    existing_data = {}

    # Read existing data
    with open(file_path, 'r') as file:
        for line in file:
            country, prices = line.strip().split(":")
            existing_data[country] = prices

    # Append new prices
    with open(file_path, 'w') as file:  # Overwrite mode
        for country, price in data.items():
            if country in existing_data:
                updated_prices = f"{existing_data[country]},{price}"
            else:
                updated_prices = str(price)
            file.write(f"{country}: {updated_prices}\n")

@app.route('/run', methods=['POST'])
def run_scraper():
    countries, currencies = fetch_gold_prices()
    final_dict = dict(zip(countries, [extract_digits(c) for c in currencies]))
    save_data_to_file(final_dict, '/data/output.txt')
    return "Data saved successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Changed port to 5000
