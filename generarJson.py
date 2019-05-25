import json

data = []

data.append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})
data.append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount':9.19})
data.append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

print(data)
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)


# import json
# data = {}
# data['clients'] = []
# data['clients'].append({
#     'first_name': 'Sigrid',
#     'last_name': 'Mannock',
#     'age': 27,
#     'amount': 7.17})
# data['clients'].append({
#     'first_name': 'Joe',
#     'last_name': 'Hinners',
#     'age': 31,
#     'amount': [1.90, 5.50]})
# data['clients'].append({
#     'first_name': 'Theodoric',
#     'last_name': 'Rivers',
#     'age': 36,
#     'amount': 1.11})
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)
