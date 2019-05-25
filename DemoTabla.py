import PySimpleGUI as sg

l = []
l_python = [{'first_name': 'Sigrid', 'last_name': 'Mannock', 'age': 27, 'amount': 7.17}, {'first_name': 'Joe', 'last_name': 'Hinners', 'age': 31, 'amount': 9.19},
{'first_name': 'Theodoric', 'last_name': 'Rivers', 'age': 36, 'amount': 1.11}]
h = list(l_python[0].keys())
for data  in l_python:
    l.append(list(data.values()))

print(l)

layout= [
        [sg.Table(values=l, headings=h)]
]

ventada = sg.Window("DemoTabla").Layout(layout)
eventos = ventada.Read()
print(eventos)
