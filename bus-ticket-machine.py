import datetime
import random

busstops = {}  # List: [stop name, distance from origin, cost to get to the next stop]
number_of_busstops = 0
boarding_stop = 0
destination_stop = 0
number_of_passenger = 0
age_mode_check = 0
number_of_adults = 0
number_of_underage = 0
total_cost = 0
sub_cost = 0
_continue_ = True
_exit_ = False


def select_mode():
  while True:
    temp_mode = input("Select mode (Advance - a / Manual - b): ")

    if temp_mode.lower() == 'a':
      return "adv"
    elif temp_mode.lower() == 'b':
      return "mnl"
    else:
      print("Invalid input. Please enter 'a' or 'b'.\n")


def age_analyzing(age_mode):
  global number_of_passenger
  global number_of_adults
  global number_of_underage

  if age_mode == 1:
    number_of_adults = number_of_passenger
    print(f"{number_of_passenger} passenger(s) are adults.")
  elif age_mode == 2:
    number_of_underage = number_of_passenger
    print(f"{number_of_passenger} passenger(s) are underage.")
  elif age_mode == 3:
    while True:
      temp_number_of_adults = input("\nEnter the number of adults: ")
      try:
        number_of_adults = int(temp_number_of_adults)

        if not (0 <= number_of_adults <= number_of_passenger):
          print(f"{number_of_adults} is not valid.\n")
          continue

        number_of_underage = number_of_passenger - number_of_adults
        break
      except ValueError:
        print(f"{temp_number_of_adults} is not valid. Please enter a number.\n")

    if number_of_adults == 0:
      print("All passengers are underage.")
    elif number_of_underage == 0:
      print("All passengers are adults.")
    else:
      print(f"Number of adults: {number_of_adults}")
      print(f"Number of underage: {number_of_underage}")


def enter_busstop_details_mnl_mode():
  global busstops
  global number_of_busstops

  while True:
    temp_number_of_busstops = input("Enter the number of bus stops: ")
    try:
      number_of_busstops = int(temp_number_of_busstops)
      print()

      if number_of_busstops < 0:
        print(f"{temp_number_of_busstops} is not valid. Enter a positive number.\n")
        continue
      break
    except ValueError:
      print(f"{temp_number_of_busstops} is not valid. Please enter a number.\n")

  for i in range(number_of_busstops):
    local_busstop_list = []

    temp_name = input(f"Enter name of bus stop {i+1}: ")
    local_busstop_list.append(temp_name)

    while True:
      temp_km = input(f"Enter the distance (in km) of {temp_name} from origin: ")
      try:
        temp_km = int(temp_km)
        if temp_km < 0:
          print(f"{temp_km} is not valid. Enter a positive number.\n")
          continue
        local_busstop_list.append(temp_km)
        break
      except ValueError:
        print(f"{temp_km} is not valid. Please enter a number.\n")

    while True:
      temp_amount = input(f"Enter ticket cost to reach {temp_name}: ")
      try:
        temp_amount = int(temp_amount)
        if temp_amount < 0:
          print(f"{temp_amount} is not valid. Enter a positive number.\n")
          continue
        local_busstop_list.append(temp_amount)
        break
      except ValueError:
        print(f"{temp_amount} is not valid. Please enter a number.\n")

    busstops[i + 1] = local_busstop_list
    print()


def enter_busstop_details_adv_mode():
  global busstops
  global number_of_busstops

  number_of_busstops = 5
  busstops = {
    1: ['bus stop 1', 10, 10],
    2: ['bus stop 2', 20, 20],
    3: ['bus stop 3', 30, 30],
    4: ['bus stop 4', 40, 40],
    5: ['bus stop 5', 50, 50]
  }


def enter_ticket_details():
  global busstops
  global number_of_busstops
  global boarding_stop
  global destination_stop
  global number_of_passenger
  global age_mode_check

  print("__________________________________________________\n")
  print("Available Bus Stops:\n")
  for i in range(1, number_of_busstops + 1):
    print(f"{i} - {busstops[i][0]}")

  while True:
    temp_boarding_stop = input("\nEnter the boarding stop number: ")
    try:
      boarding_stop = int(temp_boarding_stop)
      if not (0 < boarding_stop <= number_of_busstops):
        print("Invalid bus stop number.\n")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.\n")

  print(f"You will board from: {busstops[boarding_stop][0]}")

  while True:
    temp_destination_stop = input("\nEnter the destination stop number: ")
    try:
      destination_stop = int(temp_destination_stop)
      if not (0 < destination_stop <= number_of_busstops):
        print("Invalid bus stop number.\n")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.\n")

  while True:
    temp_number_of_passenger = input("\nEnter number of passengers: ")
    try:
      number_of_passenger = int(temp_number_of_passenger)
      if number_of_passenger <= 0:
        print("Please enter a number greater than 0.\n")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.\n")

  print("\nPassenger type:")
  print("1 - All adults")
  print("2 - All underage")
  print("3 - Mix of adult and underage")

  while True:
    temp_age_mode_check = input("\nSelect passenger type (1 / 2 / 3): ")
    try:
      age_mode_check = int(temp_age_mode_check)
      if not (0 < age_mode_check < 4):
        print("Invalid selection.\n")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter 1, 2, or 3.\n")

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

  for i in range(start, end):
    sub_cost += busstops[i][2]

  if age_mode_check == 1:
    total_cost = number_of_adults * sub_cost
  elif age_mode_check == 2:
    total_cost = number_of_underage * (sub_cost / 2)
  elif age_mode_check == 3:
    total_cost = (number_of_adults * sub_cost) + (number_of_underage * (sub_cost / 2))


def print_ticket():
  global busstops
  global boarding_stop
  global destination_stop
  global number_of_adults
  global number_of_underage
  global total_cost
  global sub_cost

  now = datetime.datetime.now()
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")
  ticket_number = f"T{random.randint(10000000000,99999999999)}"

  print("\n__________________________________________________\n")
  print("              Pvt Bus - City AA XXXXXXX")
  print(f"     Ticket No: {ticket_number}     {formatted}\n")
  print(f"          Route: {busstops[boarding_stop][0]} to {busstops[destination_stop][0]}")
  print(f"      Adult Ticket Cost:        {sub_cost} x {number_of_adults} = ₹ {sub_cost * number_of_adults}")
  print(f"      Underage Ticket Cost:     {sub_cost / 2} x {number_of_underage} = ₹ {sub_cost / 2 * number_of_underage}")
  print(f"\n            TOTAL TICKET COST: ₹ {total_cost:.2f}")
  print("__________________________________________________\n")


def start_over_check():
  global _exit_

  while True:
    print("\nWhat would you like to do next?")
    print("  a - Start Over (change bus stop data)")
    print("  b - Book a New Ticket (same bus stops)")
    print("  c - Exit the Ticketing System")

    temp_start_over = input("Enter your choice (a / b / c): ").strip().lower()

    if temp_start_over == 'a':
      return False
    elif temp_start_over == 'b':
      return True
    elif temp_start_over == 'c':
      _exit_ = True
      return False
    else:
      print("Invalid input. Please enter 'a', 'b', or 'c'.")


#----------------------MAIN----------------------------
while True:
  _continue_ = True
  _exit_ = False

  print("\nWelcome to the Bus Ticketing System")
  mode = select_mode()

  if mode == "adv":
    print("\nLoading default bus stop data...\n")
    enter_busstop_details_adv_mode()
  elif mode == "mnl":
    print("\nManual Entry Mode: Please input your bus stop details.\n")
    enter_busstop_details_mnl_mode()
  else:
    pass

  while _continue_ and not _exit_:
    print("\nCurrent Bus Stop Details:", busstops)

    enter_ticket_details()
    calculation()
    print_ticket()
    _continue_ = start_over_check()

  if _exit_:
    print("\nThank you for using the Bus Ticketing System. Goodbye!\n")
    break