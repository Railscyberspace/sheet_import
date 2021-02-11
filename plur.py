import random
c = 5
while c != 1:
    print(c)
    c -= 1

while True:
    response = input('Responses: ')
    if int(response) % 7 == 0:
        break


Name = 'Ruby'
Child = 'Baby'
Attitude = 'less troublesome.'
my_baby = '{} {} is now {} '
print(my_baby.format(Name, Child, Attitude))

for i in range(3):
    print(random.randint(10, 20))


Favourite_Kids = ["Ruby", "Nazrein", "Jason"]
Close_to_my_Heart = random.choice(Favourite_Kids)
print(Close_to_my_Heart)
