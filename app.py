from flask import Flask, render_template
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
  return render_template('api.html', content = {'title': 'wow', 'main': main })

@app.route('/very/<arg>')
def show_very(arg):
  main = 'very %s. wow.' % arg
  return render_template('api.html', content={'title': 'very', 'main': main})

@app.route('/little/<arg>')
def show_little(arg):
  main = 'little %s. wow.' % arg
  return render_template('api.html', content={'title': 'little', 'main': main})

@app.route('/wat/<arg>')
def show_wat(arg):
  main = 'wat r u doin, %s.' % arg
  return render_template('api.html', content={'title': 'wat', 'main': main})

@app.route('/omg/<arg>')
def show_omg(arg):
  main = 'omg such %s. wow.' % arg
  return render_template('api.html', content={'title': 'omg', 'main': main})
  
# many variable
@app.route('/plz/<to>/<sender>')
def show_plz(to, sender):
  main = '%s plz' % to
  return render_template('api.html', content={'title': 'plz', 'main': main, 'optional': sender })

@app.route('/thx/<to>/<sender>')
def show_thx(to, sender):
  main = 'thx %s' % to
  return render_template('api.html', content={'title': 'to', 'main': main, 'optional': sender})

@app.route('/fuk/<to>/<sender>')
def show_fuk(to, sender):
  main = 'fuk u %s' % to
  return render_template('api.html', content={'title': 'fuk u', 'main': main, 'optional': sender }) 

if __name__ == '__main__':
  app.run(debug=True)
