from flask import render_template, redirect
from werkzeug.exceptions import InternalServerError
import validators

from models.URL import URL

def index():
    return render_template('home.html', title='Make a short URL!')

def create(request):
    status_code = 200
    long_url = request.form['url']
    
    if not validators.url(long_url):
        return render_template('home.html', error='Invalid URL.', title='Make a short URL!'), 400

    url = URL.find_by_long(long_url)
    if not url:
        status_code = 201
        try:
            url = URL.create(long_url)
        except:
            raise InternalServerError('Could not create short URL.')

    return render_template(
        'result.html', 
        long_url=url.long, 
        short_url=url.short, 
        title='Your shortened URL'
    ), status_code

def redirect_to(id):
    url = URL.find_by_short(id)
    if url:
        return redirect(url.long)
    else:
        return redirect('/')
