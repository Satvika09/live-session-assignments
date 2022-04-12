car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print('new car :',car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print('coping the car:',x)
  
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del car["model"]
print('after deleting values left:',car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print('after poping model left values in car:',car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print('after popitem left car values:',car)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print('oringinal car:',x) #before the change
car["color"] = "white"
print('after modifying car:',x) #after the change

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car["brand"])

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('items in car:')
for x, y in car.items():
 print(x, y)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print('getting the model value:',x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print('default value:',x)
print('new car:',car)


