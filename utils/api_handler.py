import requests

def fetch_all_products():
    url = "https://dummyjson.com/products?limit=100"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("products", [])
    except Exception as e:
        print("API error:", e)
        return []


def create_product_mapping(products):
    mapping = {}
    for product in products:
        mapping[product["id"]] = {
            "category": product.get("category"),
            "brand": product.get("brand"),
            "rating": product.get("rating")
        }
    return mapping


def enrich_sales_data(transactions, product_mapping):
    enriched_transactions = []

    for t in transactions:
        try:
            product_id = t.get("ProductID", "")
            api_data = None

            if product_id.startswith("P"):
                pid = int(product_id.replace("P", ""))
                api_data = product_mapping.get(pid)

            t["API_Enriched"] = bool(api_data)

            if api_data:
                t["API_Category"] = api_data["category"]
                t["API_Brand"] = api_data["brand"]
                t["API_Rating"] = api_data["rating"]

            enriched_transactions.append(t)

        except Exception:
            enriched_transactions.append(t)

    return enriched_transactions
