from flask import Flask, render_template, request, jsonify, redirect
from werkzeug import exceptions
import random

from db_config import get_collection

app = Flask(__name__)

urls = []

def generate_short_url():
    possible_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    short_url = None

    # check for collisions
    while not short_url or next((url for url in urls if url['short'] == short_url), None):
        short_url = ''.join([random.choice(possible_chars) for _ in range(5)])
    
    return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['url']
        short_url = next((url['short'] for url in urls if url['long'] == long_url), None)
        if not short_url:
            short_url = generate_short_url()
            urls.append({ 'long': long_url, 'short': short_url })
        return render_template('result.html', long_url=long_url, short_url=short_url, title='Your shortened URL')
    else:
        return render_template('home.html', title='Make a short URL!')

@app.route('/<string:id>')
def redirect_to(id):
    long_url = next((url['long'] for url in urls if url['short'] == id), None)
    if long_url:
        return redirect(long_url)
    else:
        return redirect('/')

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return render_template('error.html', error=err, code=400, title='Bad Request')

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('error.html', error=err, code=404, title='Not Found')

@app.errorhandler(exceptions.MethodNotAllowed)
def handle_405(err):
    return render_template('error.html', error=err, code=405, title='Method Not Allowed')

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('error.html', error=err, code=500, title='Internal Server Error')

if __name__ == '__main__':
    app.run(debug=True)
