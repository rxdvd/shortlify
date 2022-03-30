from flask import Flask, render_template, request
from werkzeug import exceptions

from controllers import urls

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return urls.create(request)
    else:
        return urls.index()

@app.route('/<string:id>')
def redirect_to(id):
    return urls.redirect(id)

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
