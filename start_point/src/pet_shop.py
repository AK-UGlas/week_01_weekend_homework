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

# 8: uses above

# 9: get pet by name
def find_pet_by_name(pet_shop_data, pet_name):
    for pet in pet_shop_data["pets"]:
        if pet["name"] == pet_name:
            return pet

    return None

# 10: remove pet by name
def remove_pet_by_name(pet_shop_data, pet_name):
    pet = find_pet_by_name(pet_shop_data, pet_name)

    if pet != None:
        pet_shop_data["pets"].remove(pet)


# 11: add a new pet
def add_pet_to_stock(pet_shop_data, new_pet):
    pet_shop_data["pets"].append(new_pet)

# 12: get how much cash a customer has
def get_customer_cash(customer):
    return customer["cash"]

# 13: remove customer cash
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# 14: get number of pets customer has
def get_customer_pet_count(customer):
    return len(customer["pets"])

# 15: add pet to a customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    