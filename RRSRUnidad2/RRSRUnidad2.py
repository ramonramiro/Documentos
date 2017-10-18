from flask import Flask, render_template, request, redirect
from test_practice import formula, formula2

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Practica Unidad2')


@app.route('/formula', methods=['GET', 'POST'])
def execute() -> 'html':
    x = float (request.form['x'])
   # y = float(request.form('y'))
   # z = float(request.form('z'))
    title = 'This is the formula\'s result'
    result = formula(x)
    return render_template('result.html',
                           the_title=title,
                           the_x=x,
                           # the_y=y,
                           # the_z=z,
                           the_result=result,)


if __name__ == '__main__':
    app.run('localhost', 5002, debug=True)
