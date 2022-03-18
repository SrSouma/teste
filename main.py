from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/about')
def about():
    return render.template('about.html')

@app.route('/pokemon/<name>')
def pokemon(name):
    return render_template(
      'pokemon.html' ,
      name=name
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')