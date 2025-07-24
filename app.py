from flask import Flask, render_template, request
from desafios import obtener_desafio

app = Flask(__name__)
progreso = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    global progreso
    desafio = obtener_desafio()
    mensaje = ""
    mensaje_final = ""

    if request.method == 'POST':
        if "realizado" in request.form:
            progreso = min(progreso + 10, 100)
            if progreso == 100:
                mensaje_final = "¡Desafío completo! Eres un Guardián Ecológico"
            else:
                mensaje = "¡Muy bien! ¡Gracias por hacer tu parte hoy!"
        elif "otro" in request.form:
            desafio = obtener_desafio()

    return render_template(
        "index.html",
        desafio_texto=desafio["texto"],
        video_url=desafio["video"],
        mensaje=mensaje,
        mensaje_final=mensaje_final,
        progreso=progreso
    )


if __name__ == '__main__':
    app.run(debug=True)
