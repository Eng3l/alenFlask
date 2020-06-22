
from flask import ( Flask, render_template, jsonify )

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/hola/<string:nombre>')
def get_json(nombre):
    return jsonify(hola=nombre)

app.run(debug=True)