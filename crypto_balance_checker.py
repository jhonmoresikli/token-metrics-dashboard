#!/usr/bin/env python3
import requests
import sys

API_URL = "https://api.blockcypher.com/v1/btc/main/addrs/"

def get_balance(address: str) -> float:
    """Получает баланс BTC-адреса через BlockCypher API"""
    try:
        response = requests.get(API_URL + address)
        data = response.json()
        balance_btc = data.get("final_balance", 0) / 1e8
        return balance_btc
    except Exception as e:
        print("Ошибка при запросе API:", e)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python crypto_balance_checker.py <BTC_ADDRESS>")
        sys.exit(1)

    btc_address = sys.argv[1]
    balance = get_balance(btc_address)
    if balance is not None:
        print(f"Баланс {btc_address}: {balance:.8f} BTC")
    else:
        print("Не удалось получить баланс.")
