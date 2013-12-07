from flask import Flask, render_template, jsonify, request
from werkzeug.contrib.fixers import ProxyFix
from flaskmimerender import mimerender

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

def render_html(**args):
  return render_template('api.html', content=args)
render_json = jsonify
render_txt = lambda main: main

@app.route('/')
def index():
  return render_template('index.html') 

# Such wow
@app.route('/wow/<arg>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_wow(arg):
  main = 'wow such %s.' % arg
  content = {'main': main}
  if request.method == 'GET':
    return content

@app.route('/very/<arg>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_very(arg):
  main = 'very %s. wow.' % arg
  content={'main': main}
  if request.method == 'GET':
    return content

@app.route('/little/<arg>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_little(arg):
  main = 'little %s. wow.' % arg
  content={'main': main}
  if request.method == 'GET':
    return content


@app.route('/wat/<arg>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_wat(arg):
  main = 'wat r u doin, %s.' % arg
  content={'main': main}
  if request.method == 'GET':
    return content


@app.route('/omg/<arg>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_omg(arg):
  main = 'omg such %s. wow.' % arg
  content={'main': main}
  if request.method == 'GET':
    return content
  
# many variable
@app.route('/plz/<to>/<sender>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_plz(to, sender):
  main = '%s plz' % to
  content={'main': main, 'optional': sender }
  if request.method == 'GET':
    return content

@app.route('/plz/<to>')
@mimerender(
    default = 'html',
    html = render_html,
    json = render_json,
    txt = render_txt
)
def show_plz_no_sender(to):
    main = "%s plz" % to
    content = {'main': main}
    if request.method == 'GET':
        return content

@app.route('/thx/<to>/<sender>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_thx(to, sender):
  main = 'thx %s' % to
  content={'main': main, 'optional': sender}
  if request.method == 'GET':
    return content

@app.route('/thx/<to>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_anon_thx(to):
  main = 'thx %s' % to
  content={'main': main}
  if request.method == 'GET':
    return content

@app.route('/fuk/<to>/<sender>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_fuk(to, sender):
  main = 'fuk u %s' % to
  content = {'main': main, 'optional': sender }
  if request.method == 'GET':
    return content

@app.route('/fuk/<to>')
@mimerender (
  default = 'html',
  html = render_html,
  json = render_json,
  txt = render_txt
)
def show_anon_fuk(to):
  main = 'fuk u %s' % to
  content = {'main': main} 
  if request.method == 'GET':
    return content

if __name__ == '__main__':
  app.run(debug=True)
