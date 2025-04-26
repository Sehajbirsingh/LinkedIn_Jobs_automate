import requests

API_KEY = ''
BRAVE_SEARCH_URL = ''

# List of top 10 traded NASDAQ stocks (as of 2024, can be updated)
TOP_10_NASDAQ = [
    'Apple', 'Microsoft', 'Amazon', 'NVIDIA', 'Meta Platforms',
    'Tesla', 'Alphabet', 'Advanced Micro Devices', 'Broadcom', 'Netflix'
]

headers = {
    'Accept': 'application/json',
    'X-Subscription-Token': API_KEY
}

def get_stock_price(stock_name, debug=False):
    query = f"{stock_name} stock price NASDAQ"
    params = {'q': query, 'count': 1}
    response = requests.get(BRAVE_SEARCH_URL, headers=headers, params=params)
    if debug:
        print(f"\nDEBUG: Full API response for {stock_name}:")
        print(response.text)
    if response.status_code == 200:
        data = response.json()
        # Try to extract price from snippet
        for result in data.get('web', {}).get('results', []):
            snippet = result.get('description', '')
            # Try to find a price pattern, e.g., $123.45
            import re
            match = re.search(r'\$([0-9,.]+)', snippet)
            if match:
                return match.group(0)
        return 'N/A'
    else:
        return 'N/A'

def main():
    print("Top 10 Traded NASDAQ Stocks - Latest Prices:")
    # Print debug info for the first stock only
    price = get_stock_price(TOP_10_NASDAQ[0], debug=True)
    print(f"{TOP_10_NASDAQ[0]}: {price}")
    # Continue with the rest
    for stock in TOP_10_NASDAQ[1:]:
        price = get_stock_price(stock)
        print(f"{stock}: {price}")

if __name__ == "__main__":
    main() 