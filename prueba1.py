import PySimpleGUI as sg
import consumiendoJson

elementosVentada = [
        [sg.Text('Carga y Transformacón de Archivos', size =(50,1), auto_size_text=False, justification='center')],
        [sg.InputText('Seleccione Archivo'), sg.FileBrowse()],
        [sg.ReadButton('Convertir'), sg.ReadButton('Ver Tabla')]
]
window = sg.Window(" Entergable 2").Layout(elementosVentada)


while True:
    evento, valores = window.Read()
    flag = False
    extension_archivo = valores[0][-4:]
    if evento == 'Ver Tabla':
        if( extension_archivo == "json"):
            data = consumiendoJson.leerJson(valores[0])
            column, row = consumiendoJson.generarElementosTabla(data)
            flag = True

        elif extension_archivo == ".csv":
            data = consumiendoJson.leerCsv(valores[0])
            colum, row = consumiendoJson.generarElementosTablaCsv(data)
            flag = True

        else:
            sg.Popup("Ingrese un archivo tipo Json o Csv")

        if flag:
            layout_tabla = [[sg.Text('Contenido del Archivo', size =(50,1), auto_size_text=False, justification='center')],[sg.Table(values= row, headings=column, justification='right', num_rows=20, alternating_row_color='lightblue',key='_table_')]]
            tabla = sg.Window("Tabla").Layout(layout_tabla)
            while True:
                e,v = tabla.Read()
                if e is None:
                    break
            tabla.Close()

    if(evento == 'Convertir'):
        if(extension_archivo == ".csv"):
            print("Tiene q convertir a JSON")
        elif(extension_archivo == "json"):
            data = consumiendoJson.leerJson(valores[0])
            consumiendoJson.convertirCsv(data)
        else :
            sg.Popup("Ingrese un archivo tipo Json o Csv")

    if evento is None:
        break

window.Close()
