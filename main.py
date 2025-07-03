import requests

URL = "https://dummyjson.com/products"
params = {
    "limit": 200,
    "skip": 0
}

response = requests.get(url=URL, params=params)
products = response.json()["products"]

total_stock = 0
total_cost = 0

for product in products:
    # print(product.get("brand"))

    if "brand" in product:
        if product["brand"] == "Apple":
            total_stock += product["stock"]
            total_cost += product["price"] * product["stock"]

print(f"Total stock (всего на складе): {total_stock}")
print(f"Total total_cost (общая стоимость всех товаров): ${total_cost}")