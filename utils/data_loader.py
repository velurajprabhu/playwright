import json

def load_test_data():
    with open(f"test_data/users.json") as f:
        return json.load(f)