#Importar Flask
from flask import Flask, redirect, render_template, request, redirect, url_for

# Instancia de Flask. Aplicación
app = Flask(__name__, template_folder='template')
lista = []
listaT = []

#Define la ruta principal
@app.route('/')
#Función para llamar a la página index.html
def index():
    return render_template ("index.html", lista = lista, listaT = listaT)

#Defino ruta para registrar
@app.route('/registrar', methods= ['POST'])

#Función registrar cuenta
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']
        nombreT = request.form['nombreT']
        telefonoT = request.form['telefonoT']
        estadoT = request.form['estadoT']
        lista.append({'nombre': nombre, 'telefono': telefono, 'estado': estado})
        listaT.append({'nombreT': nombreT, 'telefonoT': telefonoT, 'estadoT': estadoT})
        return redirect(url_for('index'))


#main del programa 
if __name__ == "__main__":
	# Iniciamos la apicación en modo debug
	app.run(debug=True)
