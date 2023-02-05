from flask import Flask, render_template
import os
from forms import MainForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/')
def hello_world():
    form = MainForm()
    if form.is_submitted():
        pass
    return render_template('main.html', title='Main Page', form=form)

if __name__ == '__main__':
    app.run()
