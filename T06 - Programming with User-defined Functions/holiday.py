#   This file will calculate the user's total holiday cost
#   which includes plane cost, hotel cost, car-rental cost


#Pre-defined city list
city_list=["Barcelona", "Paris", "London", "Hong Kong", "Miami"]

#User inputs
city_flight=input("Please select the city you are flying into: [Barcelona, Paris, London, Hong Kong, Miami] \n")

#While loop to check the user input is correct
while city_flight not in city_list:
    city_flight=input("Wrong destination selected. Please select the city you are flying into: [Barcelona, Paris, London, Hong Kong, Miami] \n")

num_nights=int(input("Please let us know how many nights you will be staying at the hotel? \n"))

rental_days=int(input("Please let us know how many days you will be renting a car? \n"))


#Functions to calculate the various costs
def hotel_costs(num_nights):
    hotel_price=50  #50 usd per night
    
    return hotel_price*num_nights

def plane_cost(city_flight):
    if city_flight=="Barcelona":
        plane_cost=150   #50 USD
    elif city_flight=="Paris":
        plane_cost=175   #40 USD
    elif city_flight=="London":
        plane_cost=200   #45 USD
    elif city_flight=="Hong Kong":
        plane_cost=1000  #1000 USD
    elif city_flight=="Miami":
        plane_cost=900  #900 USD
    return plane_cost

def car_rental(rental_days):
    car_cost=50 #50 USD per day
    return car_cost*rental_days


#Main function to call up all the costs with x,y,z as the parameters
def holiday_cost(x,y,z):
    print("The hotel cost is: $" + str(hotel_costs(x)))
    print("The plane cost is: $" + str(plane_cost(y)))
    print("The car rental cost is: $" + str(car_rental(z)))

    return hotel_costs(x)+plane_cost(y)+car_rental(z)

#Assigning the result of the called function to variable "total_costs"
#Using the arguments previously defined by the user.
total_costs=holiday_cost(num_nights,city_flight,rental_days)

#Printing the total holiday cost
print("Your total holiday cost is: $" + str(total_costs))
