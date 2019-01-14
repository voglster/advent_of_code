def load_day_data(day_number):
    with open(f"d{day_number}_data") as f:
        data = f.readlines()
    return data
