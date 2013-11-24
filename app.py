from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title="Doge As A Service") 

# Such wow
@app.route('/wow/<argument>')
def show_wow(argument):
  return 'wow such %s' % argument

if __name__ == '__main__':
  app.run(debug=True)
