import PySimpleGUI as sg
import consumiendoJson

v=[]
h=[]
elementosVentada = [
        [sg.Text('Carga y Transformacón de Archivos', size =(50,1), auto_size_text=False, justification='center')],
        [sg.InputText('Seleccione Archivo'), sg.FileBrowse()],
        [sg.Table(values= v, headings=h)],
        [sg.ReadButton('Convertir')]
]
window = sg.Window(" Entergable 2").Layout(elementosVentada)

while True:
    evento, valores = window.Read()
    extension_archivo = valores[0][-4:]
    if(evento == 'Convertir'):
        if(extension_archivo == ".csv"):
            print("Tiene q convertir a JSON")
        elif(extension_archivo == "json"):
            data = consumiendoJson.leerJson(valores[0])
            print(data)
            consumiendoJson.convertirCsv(data)
        else :
            print("Extension incorrecta")
    if(evento == 'None'):
        break
