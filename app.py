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
    return urls.redirect_to(id)

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return render_template('errors/400.html', error=err, code=400, title='Bad Request'), 400

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html', error=err, code=404, title='Not Found'), 404

@app.errorhandler(exceptions.MethodNotAllowed)
def handle_405(err):
    return render_template('errors/405.html', error=err, code=405, title='Method Not Allowed'), 405

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html', error=err, code=500, title='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(debug=True)
