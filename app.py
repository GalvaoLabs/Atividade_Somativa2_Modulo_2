from flask import Flask, request, render_template

app = Flask(__name__)

# Configurar para caracteres especiais (acentos)
app.config['JSON_AS_ASCII'] = False

# Página inicial explicando como usar
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    resultado = v1 + v2
    return {"resultado": resultado}
    return render_template('teste.html')

## Rota subtrair
@app.route("/subtrair")
def subtracao():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    resultado = v1 - v2
    return {"resultado": resultado}
    return render_template('teste.html')

## Rota Multiplicar
@app.route("/multiplicar")
def multiplicacao():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    resultado = v1 * v2
    return {"resultado": resultado}
    return render_template('teste.html')

## Rota Dividir
@app.route("/dividir")
def divisao():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    resultado = v1 / v2
    return {"resultado": resultado}
    return render_template('teste.html')

if __name__ == "__main__":
    app.run(debug=True)
