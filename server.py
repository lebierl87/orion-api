from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Orión está listo en Railway 🚀'

# Ruta para comandos JSON
@app.route('/comando', methods=['POST'])
def comando():
    return {'respuesta': 'Comando recibido correctamente'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
