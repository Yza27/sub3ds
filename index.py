from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo ao Meu Aplicativo Web MVP!'

if __name__ == '__main__':
    app.run(debug=True)
