from flask import Flask, Response
import os

app = Flask(__name__)

def read_prices_file(file_path):
    """Reads prices.txt file and returns it in Prometheus metrics format."""
    if not os.path.exists(file_path):
        return ""

    result = []
    with open(file_path, 'r') as file:
        for line in file:
            country, prices = line.strip().split(":")
            prices_list = prices.split(",")
            # Using only the latest price
            latest_price = prices_list[-1].strip()
            result.append(f'currency_price{{country="{country.strip()}"}} {latest_price}')
    return "\n".join(result)

@app.route('/metrics')
def metrics():
    prices_data = read_prices_file('/data/prices.txt')
    return Response(prices_data, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
