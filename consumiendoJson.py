import json
import csv
# import os

def leerJson(archivo):
    with open(archivo) as f:
        data = json.load(f)
    return data

# def leerCsv(archivo):
#     lista_csv=[]
#     with open('people.csv', 'r') as csvFile:
#         reader = csv.reader(csvFile)
#         for fila in reader:
#             lista_csv.append(fila)
#     return lista_csv


def convertirCsv(data_python):

    columns = list(data_python[0].keys())

    with open('data.csv', 'w') as archivoCsv:
        arch_csv = csv.DictWriter(archivoCsv, fieldnames=columns)
        arch_csv.writeheader()
        arch_csv.writerows(data_python)
    # print("Finalizo exitoso")

def convertirJson(data_python):
    pass

# with open('data.csv', 'r') as csvFile:
#     lis=[]
#     reader = csv.reader(csvFile)
#     for fila in reader:
#         lis.append(fila)

def generarElementosTabla(data_json):
    """ Retorna tupla con nombre de columna y valores para agregar a la tabla"""
    rows = []
    header = list(data_json[0].keys())
    for data in data_json:
        rows.append(list(data.values()))
    return(header, rows

# def generarElementosTablaCsv(lista):
#     """ Retorna tupla """
#
#     header = lista[0]
#     rows = lista[1:]
#     return(header, rows)

# l_python = [{'first_name': 'Sigrid', 'last_name': 'Mannock', 'age': 27, 'amount': 7.17}, {'first_name': 'Joe', 'last_name': 'Hinners', 'age': 31, 'amount': 9.19},
# {'first_name': 'Theodoric', 'last_name': 'Rivers', 'age': 36, 'amount': 1.11}]
#
# r = generarElementosTabla(l_python)
# print(r)
