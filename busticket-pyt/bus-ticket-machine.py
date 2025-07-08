import datetime
import random

busstops = {} # List: [stop name, distance from origin, cost  to grt the next stop]
number_of_busstops = 0
boarding_stop = 0
destination_stop = 0
number_of_passenger = 0
age_mode_check = 0
number_of_adults = 0
number_of_underage = 0
total_cost = 0
sub_cost = 0


def select_mode():

  while True:

    temp_mode = input("Select the mode : Advance - a / manual - b : ")

    if temp_mode.lower() == 'a':
      return "adv"
    elif temp_mode.lower() == 'b':
      return "mnl"
    else:
      print("You answer is not valid, enter the a / b (Advance - a / Not advance - b)")


def age_analyzing( age_mode ):

  global number_of_passenger
  global number_of_adults
  global number_of_underage

  if age_mode == 1:
    number_of_adults = number_of_passenger
    if number_of_passenger != 1:
      print(f"{number_of_passenger} Passengers are adult")
    else:
      print("Passenger is an adult")

  if age_mode == 2:
    number_of_underage = number_of_passenger
    if number_of_passenger != 1:
      print(f"{number_of_passenger} Passengers are underage")
    else:
      print("Passenger is underage")

  if age_mode == 3:
    while True:

      temp_number_of_adults = input( "\nEnter the number of adults : " )

      try:
        number_of_adults = int(temp_number_of_adults)

        if not( 0 < number_of_adults < number_of_passenger ):
          print(f"{number_of_adults} is not valid\n")
          continue
        
        number_of_underage = number_of_passenger - number_of_adults
        break
      except ValueError:
        print(f"{temp_number_of_adults} Is not valid, enter a number\n")

    print(f"Number of adults {number_of_adults}")

    print(f"Number of underage {number_of_underage}")


def enter_busstop_details_mnl_mode():

  global busstops
  global number_of_busstops

  while True:

    temp_number_of_busstops = input("Enter the number of bus stops : ")

    try:
      number_of_busstops = int(temp_number_of_busstops)
      print()
      
      if number_of_busstops<0:
        print(f"{temp_number_of_busstops} Is not valid, enter a positive number\n")
        continue

      break
    except ValueError:
      print(f"{temp_number_of_busstops} Is not valid, enter a number\n")


  for i in  range(0,number_of_busstops):

    local_busstop_list = []

    temp_name = input(f"Enter the name of the {i+1} bus stop : ")
    local_busstop_list.append(temp_name)

    while True:
        
      temp_km = input(f"Enter the distance of the {local_busstop_list[0]} bus stop : ")

      try:
        temp_km = int(temp_km)

        if temp_km<0:
          print(f"{temp_km} Is not valid, enter a positive number\n")
          continue

        local_busstop_list.append(temp_km)
        break
      except ValueError:
        print(f"{temp_km} Is not valid, enter a number\n")

    while True:
            
      temp_amount = input(f"Enter the amount to get {local_busstop_list[0]} bus stop : ")

      try:
        temp_amount = int(temp_amount)

        if temp_amount<0:
          print(f"{temp_amount} Is not valid, enter a positive number\n")
          continue

        local_busstop_list.append(temp_amount)
        break
      except ValueError:
        print(f"{temp_amount} Is not valid, enter a number\n")

    busstops[i+1] = local_busstop_list
    print()
    

def enter_busstop_details_adv_mode():

  global busstops
  global number_of_busstops

  number_of_busstops = 5
  busstops = {1:['bus stop 1',10,10],
              2:['bus stop 2',20,20],
              3:['bus stop 3',30,30],
              4:['bus stop 4',40,40],
              5:['bus stop 5',50,50]}
  

def enter_ticket_details():

  global busstops
  global number_of_busstops
  global boarding_stop
  global destination_stop
  global number_of_passenger
  global age_mode_check

  print("__________________________________________________\n")
  print("These are the available bus stop :")
  
  for i in range(1,number_of_busstops + 1):
    print(f"{i} - {busstops[i][0]}")  

  while True:
    
    temp_boarding_stop = input("\nEnter the boarding stop : ")

    try:
      boarding_stop = int(temp_boarding_stop)
        
      if not(0 < boarding_stop <= number_of_busstops):
        print("Enter the correct bus stop number\n")
        continue
      break
    except ValueError:
      print("Enter the correct bus stop number\n")

  print(f"You board from {busstops[boarding_stop][0]}")
  while True:
    
    temp_destination_stop = input("\nEnter the destination stop : ")

    try:
      destination_stop = int(temp_destination_stop)
        
      if not(0 < destination_stop <= number_of_busstops):
        print("Enter the correct bus stop number\n")
        continue
      break
    except ValueError:
      print("Enter the correct bus stop number\n")

  while True:

    temp_number_of_passenger = input("\nEnter the number of passenger : ")

    try:
      number_of_passenger = int(temp_number_of_passenger)

      if number_of_passenger <= 0:
        print("Enter the correct number of passengers\n")
        continue
      break
    except ValueError:
      print("Enter the correct number of passsengers\n")

  print("\nSelect the correct option : ")
  print("All adults - 1")
  print("All underage - 2")
  print("Adult and underage - 3")
    
  while True:

    temp_age_mode_check = input("\nEnter the correct option : ")

    try:
      age_mode_check = int(temp_age_mode_check)

      if not(0<age_mode_check<4):
        print(f"{temp_age_mode_check} is not valid\n")
        continue
      break
    except ValueError:
      print("Enter a number mentioned in the option\n")   
  
  age_analyzing(age_mode_check)


def calculation():

  global busstops
  global boarding_stop
  global destination_stop
  global age_mode_check
  global number_of_adults
  global number_of_underage
  global total_cost
  global sub_cost

  total_cost = 0
  sub_cost = 0

  start = min(boarding_stop, destination_stop)
  end = max(boarding_stop, destination_stop)

  for i in range(start , end):
    sub_cost += busstops[i][2]

  if age_mode_check == 1:
    total_cost =  number_of_adults * ( sub_cost / 2 )
  if age_mode_check == 2:
    total_cost =  number_of_underage * sub_cost
  if age_mode_check == 3:
    total_cost = ( number_of_adults * sub_cost ) + (number_of_underage * ( sub_cost / 2 ) )

def print_ticket():

  global busstops
  global number_of_busstops
  global boarding_stop
  global destination_stop
  global number_of_passenger
  global age_mode_check
  global number_of_adults
  global number_of_underage
  global total_cost
  global sub_cost

  now = datetime.datetime.now()
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")  

  ticket_number = f"T{random.randint(10000000000,99999999999)}"


  print("__________________________________________________\n")
  print()
  print("    Pvt Bus, Alappuzha - KL XXXXXXX")
  print(ticket_number,"        ",formatted)
  print()
  print(f"      {busstops[boarding_stop][0]}   -    {busstops[destination_stop][0]}")
  print(f"ADULT:                  {sub_cost} x {number_of_adults} = RS {sub_cost * number_of_adults}")
  print(f"UNDERAGE:               {sub_cost} x {number_of_underage} = RS {sub_cost * number_of_underage}")

  print(f"            TOTAL: RS {total_cost}")

#----------------------MAIN----------------------------

mode = select_mode()

if mode == "adv":
  print()
  enter_busstop_details_adv_mode()
elif mode == "mnl":
  print()
  enter_busstop_details_mnl_mode()
else:
  pass

print("Logical view :",busstops)

enter_ticket_details()
calculation()
print_ticket()