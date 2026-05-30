from flask import Flask

app = Flask(__name__)

<h1>CI/CD funcionando correctamente</h1>

@app.route('/')
def home():
    return """
    <h1>Proyecto DevOps</h1>
    <h2>Sistemas Operativos II</h2>
    <p>Docker + AWS + CI/CD funcionando</p>
    """

app.run(host='0.0.0.0', port=5000)