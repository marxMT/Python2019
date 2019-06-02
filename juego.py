import os
import string
import random

import PySimpleGUI as sg

def letra_random():
    alfabero = string.ascii_letters
    letra = random.choice(alfabero)
    return letra


def crear_boton():
    letra = [sg.Button(letra_random())]
    return letra


def create_grilla():


    grilla = []

    for n in range(10):
        fila = []
        for n in range(10):
            #letra = crear_boton()
            fila.append(sg.Button(letra_random()))
        grilla.append(fila)
    return grilla




layout = [
    [sg.Text('Sopa de letras', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Text('_' * 100, size=(70, 1))],
    [sg.Text('------------TABLAAA-------------', size=(35, 1))],
    [sg.Text('_' * 100, size=(70, 1))],
# [sg.Button('Customized', button_color=('white', 'green')),sg.Button('Customized', button_color=('white', 'green'))]
    [create_grilla()],
]

event, values = sg.Window('Everything bagel', layout, auto_size_text=True, default_element_size=(40, 1)).Read()
