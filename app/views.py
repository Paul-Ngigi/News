from flask import render_template
from app import app
from request import get_sources, get_articles


@app.route('/')
def index():
    title = 'Home - Welcome to News Article'
    sports = get_sources('sports')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    general = get_sources('general')
    health = get_sources('health')
    science = get_sources('science')
    technology = get_sources('technology')

    return render_template('index.html',
                           sports=sports,
                           business=business,
                           technology=technology,
                           entertainment=entertainment,
                           general=general,
                           health=health,
                           science=science,)

    return render_template('index.html', title=title)
