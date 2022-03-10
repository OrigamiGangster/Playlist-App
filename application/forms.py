from flask_wtf import FlaskForm
from wtforms import StringField


class AlbumForm(FlaskForm):
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')