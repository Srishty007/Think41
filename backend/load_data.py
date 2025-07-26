import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["conversational_ai_db"]


def load_csv_to_mongo(file_name, collection_name):
    try:
        df = pd.read_csv(file_name)
        records = df.to_dict("records")
        db[collection_name].insert_many(records)
        print(f"Loaded {len(records)} records into '{collection_name}' collection.")
    except Exception as e:
        print(f"Failed to load {file_name}: {e}")

csv_collections = {
    "inventory_items.csv": "inventory_items",
    "users.csv": "users",
    "distribution_centers.csv": "distribution_centers",
    "order_items.csv": "order_items",
    "products.csv": "products",
    "orders.csv": "orders"
}

for file, collection in csv_collections.items():
    load_csv_to_mongo(file, collection)

print(" All CSVs have been loaded into MongoDB!")