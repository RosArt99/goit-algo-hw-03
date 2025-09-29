import random

def get_numbers_ticket(min, max, quantity): #arguments are back to the function
    if min < 1 or max > 1000: 
        print("min can't be negative, max can't be higher than 1000")
        return []
    if quantity > ((max+1) - min):
        print("incorrect range")
        return []
    else: 
        random_list = random.sample(range(min, max+1), quantity)
        random_list.sort()
    return random_list

print(get_numbers_ticket(1, 59, 10))

