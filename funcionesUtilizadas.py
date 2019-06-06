import json
import csv
import os
import string
import random

def leerJson(archivo):
    """
    value: obj Json
    return: python obj
    """
    try:
        with open(archivo) as f:
            data = json.load(f)
    except OSError as err:
        print("OS error: {0}".format(err))
    return data


def leerCsv(archivo):
    """
    value: Obj csv
    return: Python List
    """
    lista_csv = []
    try:
        with open(archivo, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for fila in reader:
                lista_csv.append(fila)
    except OSError as err:
        print("OS error: {0}".format(err))
    return lista_csv


def convertirToCsv(data_python):
    """
    Toma obj Python y genera un archivo csv
    """
    columns = list(data_python[0].keys())

    try:
        with open('data.csv', 'w') as archivoCsv:
            arch_csv = csv.DictWriter(archivoCsv, fieldnames=columns)
            arch_csv.writeheader()
            arch_csv.writerows(data_python)
    except OSError as err:
        print("OS error: {0}".format(err))


def convertirToJson(data_python):
    """
    Toma obj Python y genera un archivo Json
    """
    try:
        with open('dataJsonToCsv.json', 'w') as archivoJson:
            json.dump(data_python, archivoJson)
    except OSError as err:
        print("OS error: {0}".format(err))


def generarElementosTabla(data):
    """
    Retorna tupla con nombre de columna y
    valores para agregar a la tabla
    return: (cabezera, value)
    """
    rows = []
    header = list(data[0].keys())
    for d in data:
        rows.append(list(d.values()))
    return(header, rows)


class Error(Exception):
    """
    Clase base para otras excepciones
    """
    pass


class FileTooLargeError(Error):
    """
    Se lanza cuando el file.size es mayor a 1024 bytes
    """
    pass
