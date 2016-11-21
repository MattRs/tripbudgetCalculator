""" Trip Budget Calculator """

def hotel_cost(nights):
    """ hotel costs $140 per night"""
    return 140 * nights

def plane_ride_cost(city):
    """ flight costs to 4 distinct locations """
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        print("need to pick a city")

def rental_car_cost(days):
    """ rental car costs per day used """
    rental_cost = 40 * days
    if days >= 7:
        rental_cost -= 50
    elif days >= 3:
        rental_cost -= 20
    else:
        rental_cost -= 0
    return rental_cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

""" Budget a trip to Los Angeles for 5 days with an extra $600 """
print(trip_cost("Los Angeles", 5, 600))