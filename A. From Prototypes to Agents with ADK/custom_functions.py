import requests

def get_crypto_price(coin_id: str, vs: str = "usd"):
    """
    Fetch the current price of a cryptocurrency from CoinGecko.

    Args:
        coin_id: The coin's ID on CoinGecko (e.g., "bitcoin", "ethereum").
        vs:      The quote currency (default: "usd", e.g., "eur", "jpy").

    Returns:
        A JSON dict like {"bitcoin": {"usd": 69000.0}} if successful,
        or None if the price could not be fetched.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": vs}

    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            return data if coin_id in data else None
        return None
    except requests.RequestException:
        return None
