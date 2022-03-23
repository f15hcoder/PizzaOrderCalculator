total_cost = 0.00
print("Which pizza crust do you prefer? Thick crust or thin crust?")
crust = input().lower()
print("Pick a pizza size from 8, 10, 12, 14 or 18 inches.")
size = int(input())
print("Would you like cheese?")
cheese = input().lower()
print("Which pizza type would you like? Margherita, Vegetable, Vegan, Hawaiian or Meat Feast?")
type = input().lower()
if crust == "thick":
  total_cost = total_cost + 8.00
else:
  total_cost = 10.00
if size > 10:
  total_cost = total_cost + 2.00
else:
  total_cost = total_cost + 0.00
if cheese != "yes":
  total_cost = total_cost - 0.50
if type == "margarita":
  total_cost = total_cost + 0.00
if type in ["vegetable","vegan"]:
  total_cost = total_cost + 1.00
if type in ["hawaiian","meat feast"]:
  total_cost = total_cost + 2.00
if size == 18:
  print("Do you have a voucher code?")
  voucher = input().lower()
  if voucher != "no":
    print("Please enter the voucher code")
    voucher_code = input()
    if voucher_code == "FunFriday":
      total_cost = total_cost - 2.00
    else:
      print("Wrong Code")
  else:
    print(f"You ordered a {size} inch {crust} {type} pizza with {cheese} cheese.")
    print(f"your pizza will cost: ${total_cost}")
