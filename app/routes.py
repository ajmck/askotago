from app import app, db
from flask import render_template, redirect, request
from app.forms import PostForm
from app.models import Post


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    returned_posts = Post.query.all()

    if form.validate_on_submit():
        p = Post()
        p.body = request.form["postbody"]
        print(p)
        db.session.add(p)
        db.session.commit()
        print("Added {} to db".format(p))
        return redirect('/')
    return render_template('index.html', form=form, returned_posts=returned_posts)
