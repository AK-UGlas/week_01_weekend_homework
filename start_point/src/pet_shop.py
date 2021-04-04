# functions to run a pet shop

# 1: get name of shop
def get_pet_shop_name(pet_shop_data):
    return pet_shop_data["name"]

# 2: get pet shop total cash
def get_total_cash(pet_shop_data):
    return pet_shop_data["admin"]["total_cash"]

# 3: add or remove cash from total
def add_or_remove_cash(pet_shop_data, amount):
    pet_shop_data["admin"]["total_cash"] += amount
