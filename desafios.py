import random

_desafios_originales = [
    {
        "texto": "Caminá o andá en bici por 30 minutos",
        "video": "https://www.youtube.com/embed/zO4DxRdOJyE"
    },
    {
        "texto": "Hacé una limpieza en una plaza, vereda o parque cercano",
        "video": "https://www.youtube.com/embed/ruN99c116Z4"
    },
    {
        "texto": "Separá todos los residuos de tu casa y organizalos",
        "video": "https://www.youtube.com/embed/GS_15jJwTLc"
    },
    {
        "texto": "Creá una compostera casera o activá la que ya tenés",
        "video": "https://www.youtube.com/embed/TEhnyfsWINA"
    },
    {
        "texto": "Mirá un documental ecológico y aplicalo a tus hábitos",
        "video": "https://www.youtube.com/embed/76uSdKCbsQQ"
    },
    {
        "texto": "Cuidá cualquier planta durante al menos 10 minutos",
        "video": "https://www.youtube.com/embed/Y1jTRsBRh3g"
    },
    {
        "texto": "Creá un ecobrick rellenando una botella con plásticos",
        "video": "https://www.youtube.com/embed/OAgGYOnmtG4"
    },
    {
        "texto": "Revisá los enchufes de tu casa y desconectá lo innecesario",
        "video": "https://www.youtube.com/embed/TbdMq5fpXX4"
    },
    {
        "texto": "Escribí una lista de hábitos que vas a aplicar esta semana",
        "video": "https://www.youtube.com/embed/0Cr5qWhvxXY"
    },
    {
        "texto": "Prepará una comida 100% vegetal y aprendé sobre su impacto",
        "video": "https://www.youtube.com/embed/BiBSZI8y1XQ"
    },
    {
        "texto": "Repará algo viejo en tu casa para darle un nuevo uso",
        "video": "https://www.youtube.com/embed/XyqP5qWuy-M"
    },
    {
        "texto": "Limpieza digital: eliminá correos y archivos que ya no usás",
        "video": "https://www.youtube.com/embed/Qc5Prj3tMn4"
    },
    {
        "texto": "Juntá materiales reciclables y lleválos a un punto verde",
        "video": "https://www.youtube.com/embed/kSQkC6zejtA"
    }
]

# Lista dinámica que se reinicia cuando se agota
desafios_restantes = _desafios_originales.copy()


def obtener_desafio():
    global desafios_restantes
    if not desafios_restantes:
        desafios_restantes = _desafios_originales.copy()
    desafio = random.choice(desafios_restantes)
    desafios_restantes.remove(desafio)
    return desafio
