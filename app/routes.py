from app import app
from flask import render_template
from app.forms import PostForm

@app.route('/')
@app.route('/index')
def index(methods=['GET', 'POST']):
        form = PostForm()
        if form.validate_on_submit():
            return redirect('/')
        return render_template('index.html', form=form)

