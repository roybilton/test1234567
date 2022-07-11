from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.data
   tesqt =  request.headers.get("X-Sift-Science-Signature")

   if name:
       print('Request for hello page received with name=%s' % name)
       print('xxxxxx for hello page received with name=%s' % tesqt)
       return render_template('hello.html', name = name)
   else:
       print(name)
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
