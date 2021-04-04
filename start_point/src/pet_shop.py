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

# 4: get the number of animals sold
def get_pets_sold(pet_shop_data):
    return pet_shop_data["admin"]["pets_sold"]

# 5: increase the number of pets sold
def increase_pets_sold(pet_shop_data, num_pets_sold):
    pet_shop_data["admin"]["pets_sold"] += num_pets_sold

# 6: get stock count
def get_stock_count(pet_shop_data):
    return len(pet_shop_data["pets"])

# 7: get pets by breed
def get_pets_by_breed(pet_shop_data, breed):
    return [pet for pet in pet_shop_data["pets"] 
            if pet["breed"] == breed]

# 8: 
