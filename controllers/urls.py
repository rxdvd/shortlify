from flask import render_template, redirect

from models.URL import URL

urls = []

def index():
    return render_template('home.html', title='Make a short URL!')

def create(request):
    status_code = 200
    long_url = request.form['url']
    url = URL.find_by_long(long_url)
    if not url:
        status_code = 201
        url = URL.create(long_url)

    return render_template(
        'newurl.html', 
        long_url=url.long, 
        short_url=url.short, 
        title='Your shortened URL'
    ), status_code

def redirect(id):
    url = URL.find_by_short(id)
    if url:
        return redirect(url.long)
    else:
        return redirect('/')
