from flask import Flask, render_template, request
from sistema_especialista import REGRAS, TODOS_SINTOMAS, encadeamento_para_frente

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        fatos = {s for s in TODOS_SINTOMAS if request.form.get(s)}
        regras_disparadas = encadeamento_para_frente(fatos)

        if regras_disparadas:
            principal = regras_disparadas[0]
            alternativas = regras_disparadas[1:]
            conclusao = principal["conclusao"]
        else:
            principal = None
            alternativas = []
            fallback = next(r for r in REGRAS if not r["condicoes"])
            conclusao = fallback["conclusao"]

        resultado = {
            "fatos": sorted(fatos),
            "regras_disparadas": regras_disparadas,
            "principal": principal,
            "alternativas": alternativas,
            "conclusao": conclusao,
        }

    return render_template("index.html", sintomas=TODOS_SINTOMAS, resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
