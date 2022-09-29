from flask import Flask, render_template

# Crear instancia de Flask
app = Flask(__name__)

# Definir el route
@app.route('/')
def render():
    # Retornar la plantilla "ejemplo.html"
	return render_template("ejemplo.html")