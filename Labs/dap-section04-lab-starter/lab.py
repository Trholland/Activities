import sys, json

with open(f"{sys.argv[1]}.json", 'r') as file:
    desserts = json.load(file)

# print(desserts)

# def assignScore(dessert):
#     print(f'Now sorting {dessert['summary']}')
#     return dessert['summary']

# desserts.sort(key=assignScore)

categories = set()

def assignScore(dessert):
    categories.add(dessert['category'])
    score = 0
    if dessert['category'] == 'Ice Cream':
        score = score + 200
    if dessert['category'] == 'Pastry':
        score = score + 100
    if 'cookies' in dessert['flavors']:
        score = score + 100
    if 'cream' in dessert['flavors']:
        score = score + 100
    if 'cream cheese' in dessert['flavors']:
        score = score + 100
    if 'vanilla' in dessert['flavors']:
        score = score + 90
    if 'strawberry' in dessert['flavors']:
        score = score + 80
    if 'apple' in dessert['flavors']:
        score = score + 70
    if 'honey' in dessert['flavors']:
        score = score + 25
    if 'coffee' in dessert['flavors']:
        score = score + 6
    if 'chocolate' in dessert['flavors']:
        score = score + 5
    if 'mango' in dessert['flavors']:
        score = score + 4
    if 'mint' in dessert['flavors']:
        score = score + 3
    if 'coconut' in dessert['flavors']:
        score = score + 2
    if 'peanut butter' in dessert['flavors']:
        score = score - 100
    if 'almond' in dessert['flavors']:
        score = score - 100
    if 'pistachio' in dessert['flavors']:
        score = score - 100
    print(f'Now sorting {dessert['summary']}\nFlavor(s): {dessert['flavors']}\nScore: {score}')
    return score

# try:
#     if 'coffee' in dessert['test']:
#         score = score + 6
# except KeyError:
#     print('error')

desserts.sort(key=assignScore, reverse=True)

print(f"Sorted {len(desserts)} desserts:")
print() # breathing room

for dessert in desserts:
    print(dessert["summary"])