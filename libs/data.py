

def save_data(data):
    with open("data.json", "w") as f:
        f.write(json.dumps(data))
    return "Data saved successfully"