from flask import jsonify, render_template
from app import app

noticias = [
    {
        'id': 1,
        'titulo': 'Noticia 1',
        'autor': 'Anastacia',
        'data': '12/12/12',
        'img': 'img/default-img.png'
    },
    {
        'id': 2,
        'titulo': 'Noticia 2',
        'autor': 'Jubileu',
        'data': '10/12/12',
        'img': 'img/default-img.png'
    },

]

@app.route("/")
def index():
    return render_template('noticias.html', noticias=noticias)


@app.route("/<int:post_id>")
def view_noticia(post_id):
    return render_template('view_noticia.html')
