import PySimpleGUI as sg
import funcionesUtilizadas
import os

from funcionesUtilizadas import FileTooLargeError

elementosVentada = [
        [sg.Text('Carga y Transformacón de Archivos', size =(50,1), auto_size_text=False, justification='center')],
        [sg.InputText('Seleccione Archivo'), sg.FileBrowse()],
        [sg.ReadButton('Convertir'), sg.ReadButton('Ver Tabla')]
]
window = sg.Window(" Entergable 2").Layout(elementosVentada)


while True:
    evento, valores = window.Read()
    print(evento)
    print("------------------------")
    print(valores)
    flag = False
    tupla_archivo = os.path.splitext(valores[0])
    extension_archivo = tupla_archivo[1]
    if evento == 'Ver Tabla':
        if(extension_archivo == ".json"):
            try:
                if os.path.getsize(valores[0]) > 1024:
                    raise FileTooLargeError
                data = funcionesUtilizadas.leerJson(valores[0])
                column, row = funcionesUtilizadas.generarElementosTabla(data)
                flag = True
            except FileTooLargeError:
                print("El archivo es muy grande")

        elif extension_archivo == ".csv":
            try:
                if os.path.getsize(valores[0]) > 1024:
                    raise FileTooLargeError
                data = funcionesUtilizadas.leerCsv(valores[0])
                column, row = funcionesUtilizadas.generarElementosTabla(data)
                flag = True
            except FileTooLargeError:
                print("El archivo es muy grande")

        else:
            sg.Popup("Ingrese un archivo tipo Json o Csv")

        if flag:
            layout_tabla = [
                    [sg.Text('Contenido del Archivo', size =(50,1), auto_size_text=False, justification='center')],
                    [sg.Table(values= row, headings=column, justification='right', num_rows=20,key='_table_')]
            ]
            tabla = sg.Window("Tabla").Layout(layout_tabla)
            while True:
                e,v = tabla.Read()
                if e is None:
                    break
            tabla.Close()

    if(evento == 'Convertir'):
        if(extension_archivo == ".csv"):
            data = funcionesUtilizadas.leerCsv(valores[0])
            funcionesUtilizadas.convertirToJson(data)
            sg.Popup("Conversion exitosa")
        elif(extension_archivo == ".json"):
            data = funcionesUtilizadas.leerJson(valores[0])
            funcionesUtilizadas.convertirToCsv(data)
            sg.Popup("Conversion exitosa")
        else :
            sg.Popup("Ingrese un archivo tipo Json o Csv")

    if evento is None:
        break

window.Close()
