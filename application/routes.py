from flask import render_template, request
from application import app
from application.forms import AlbumForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = AlbumForm(request.form)
    if request.method == 'POST':
        if request.form.get('action1') == 'AddAlbum':
            return render_template('new_album.html', form=form)
    
    return render_template("home.html")

@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    form = AlbumForm(request.form)
    return render_template('new_album.html', form=form)