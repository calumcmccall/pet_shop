# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_sales):
    pet_shop["admin"]["pets_sold"] += new_sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)

    return pets_by_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if (get_customer_cash(customer) - new_pet["price"]) >= 0:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):

    if (pet is not None) and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)

        add_or_remove_cash(pet_shop, pet["price"])
        remove_customer_cash(customer, pet["price"])

        increase_pets_sold(pet_shop, 1)
