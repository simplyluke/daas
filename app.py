from flask import Flask, render_template, jsonify, request
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def index():
  return render_template('index.html', title="Doge As A Service") 

# Such wow
@app.route('/wow/<arg>')
def show_wow(arg):
  main = 'wow such %s.' % arg
  content = {'title': 'wow', 'main': main}
  return render_template('api.html', content=content)

@app.route('/very/<arg>')
def show_very(arg):
  main = 'very %s. wow.' % arg
  content={'title': 'very', 'main': main}
  return render_template('api.html', content=content)

@app.route('/little/<arg>')
def show_little(arg):
  main = 'little %s. wow.' % arg
  content={'title': 'little', 'main': main}
  return render_template('api.html', content=content)


@app.route('/wat/<arg>')
def show_wat(arg):
  main = 'wat r u doin, %s.' % arg
  content={'title': 'wat', 'main': main}
  return render_template('api.html', content=content)


@app.route('/omg/<arg>')
def show_omg(arg):
  main = 'omg such %s. wow.' % arg
  content={'title': 'omg', 'main': main}
  return render_template('api.html', content=content)
  
# many variable
@app.route('/plz/<to>/<sender>')
def show_plz(to, sender):
  main = '%s plz' % to
  content={'title': 'plz', 'main': main, 'optional': sender }
  return render_template('api.html', content=content)

@app.route('/thx/<to>/<sender>')
def show_thx(to, sender):
  main = 'thx %s' % to
  content={'title': 'to', 'main': main, 'optional': sender}
  return render_template('api.html', content=content)

@app.route('/fuk/<to>/<sender>')
def show_fuk(to, sender):
  main = 'fuk u %s' % to
  content = {'title': 'fuk u', 'main': main, 'optional': sender }
  return orender_template('api.html', content=content)

if __name__ == '__main__':
  app.run()
