cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
  print(x)

cars.append("Honda")

cars.pop(1)
print(cars)

cars.append("Volvo")

cars.remove("Volvo")
print(cars)
