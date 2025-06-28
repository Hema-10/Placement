import json

data = {"name": "Alice", "age": 25, "city": "Wonderland"}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
