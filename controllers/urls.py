from flask import render_template, redirect
import random

urls = []

def index():
    return render_template('home.html', title='Make a short URL!')

def create(request):
    long_url = request.form['url']
    short_url = next((url['short'] for url in urls if url['long'] == long_url), None)
    if not short_url:
        short_url = generate_short_url()
        urls.append({ 'long': long_url, 'short': short_url })
    return render_template('result.html', long_url=long_url, short_url=short_url, title='Your shortened URL')

def redirect(id):
    long_url = next((url['long'] for url in urls if url['short'] == id), None)
    if long_url:
        return redirect(long_url)
    else:
        return redirect('/')

def generate_short_url():
    possible_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    short_url = None

    # check for collisions
    while not short_url or next((url for url in urls if url['short'] == short_url), None):
        short_url = ''.join([random.choice(possible_chars) for _ in range(5)])
    
    return short_url
