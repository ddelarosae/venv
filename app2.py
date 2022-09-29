from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<string:nombre>')
@app.route('/<string:nombre>/<int:edad>')
def hola(nombre=None, edad=None):
    if nombre and edad:
        return "Hola, {} tienes {} años".format(nombre,edad)
    elif nombre:
        return "Saludos {}".format(nombre)
    else:
        return render_template('prueba.html')