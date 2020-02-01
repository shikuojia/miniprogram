from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flask.db import get_db

bp = Blueprint('blog',__name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'select p.id,title,body,created,author_id,username'
        ' from post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html',posts=posts)

@bp.route('/create',methods=('GET','POST'))
@login_required
def create():
    if request.method =="POST":
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = '请填写文章名称'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'insert into post (title,body,author_id)'
                ' values (?,?,?)',(title,body,g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


def get_post(id,check_author=True):
    post = get_db().execute(
        'select p.id,title,body,created,author_id,username'
        ' from post p JOIN user u ON p.author_id = u.id'
        ' where p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404,'Post id {0} doesn\'t exist.'.format(id))
    if check_author and post['author_id'] != g.user['id']:
        abort(403)
    return post