from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.exc import NoResultFound
from flask_sqlalchemy import SQLAlchemy
from models import Posts, Comment, Users
from db import get_session
from config import Config
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    with get_session() as session:
        username = session.query(Users).get(id)
    return username



def validate_name(val):
    return isinstance(val, str) and len(val) > 0


def validate_prep_time(val):
    return isinstance(val, int) and val > 0 and val < 999


def post_to_dict(post):
    return {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author,
        'created_at': post.created_at,
    }


def comments_data_to_dict(comments):
    return [{
        key: getattr(comment, key)
        for key in ('id', 'post_id', 'author', 'content', 'created_at')
    } for comment in comments]

REQUIRED_DIELDS = {
    'title': validate_name,
    'content': validate_name,
    'author': validate_name,
}

ORDERING_QUERY_KEY = 'ordering'
# @app.route('/api')
# def redirect_to_posts():
#     return redirect(url_for('posts'))
#
#
# @app.route('/api/posts', methods = ['GET', 'POST'])
# def posts():
#     if request.method == 'GET':
#         ordering = 'id'
#         if ORDERING_QUERY_KEY in request.args:
#             ordering = request.args[ORDERING_QUERY_KEY]
#
#         with get_session() as session:
#             posts = session.query(Posts)
#             post_data = [
#                 post_to_dict(post)
#                 for post in posts
#             ]
#         return post_data
#
#     elif request.method == 'POST':
#         for key in REQUIRED_DIELDS:
#             if key not in request.json:
#                 return {'error': f'{key} is required'}, 400
#             elif not REQUIRED_DIELDS[key](request.json[key]):
#                 return {'error': f'{key} is invalid'}, 400
#
#         with get_session() as session:
#             post = Posts(**request.json)
#             session.add(post)
#             session.commit()
#             return {'message': 'Post added successfully'}, 201
#
#
# @app.route('/api/posts/<int:post_id>/', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
# def post(post_id):
#     with get_session() as session:
#         post = session.query(Posts).filter_by(id=post_id).first()
#         if post is None:
#             return {'error': 'Post not found'}, 404
#
#         post_data = post_to_dict(post)
#
#         if request.method == "GET":
#             post_dict =post_to_dict(post)
#
#             comments = session.query(Comment).filter_by(post_id=post_id)
#
#             post_dict['comment'] = (
#                 comments_data_to_dict(comments)
#             )
#             return post_dict
#
#         elif request.method == 'PUT':
#             for key in REQUIRED_DIELDS:
#                 if key not in request.json:
#                     return {'error': f'{key} is required'}, 400
#                 elif not REQUIRED_DIELDS[key](request.json[key]):
#                     return {'error': f'{key} is invalid'}, 400
#
#             for key, value in request.json.items():
#                 setattr(post, key, value)
#             return {'message': 'Recipe update successfully'}, 200
#
#         elif request.method == 'PATCH':
#             for key in request.json:
#                 if key not in REQUIRED_DIELDS:
#                     return {'error': f'{key} is not allowed'},400
#                 elif not REQUIRED_DIELDS[key](request.json[key]):
#                     return {'error': f'{key} is invalid'},400
#
#             for key, value in request.json.items():
#                 setattr(post, key, value)
#             return {'message': 'Recipe update successfully'}, 200
#         elif request.method == 'DELETE':
#             session.delete(post)
#             return {'message': 'Post deleted successfully'}, 204


@app.route('/')
def index():

    with get_session() as session:
        posts = session.query(Posts).all()
        return render_template(
            'index.html',
            posts=posts,
        )


@app.route('/post/<int:post_id>/')

def post_detail(post_id):
    with get_session() as session:
        try:
            posts = session.query(Posts).filter_by(id=post_id).one()
        except NoResultFound:
            return render_template('404.html'), 404


        comments = session.query(Comment).filter_by(post_id=post_id)

        return render_template(
            'post_detail.html',
            posts=posts,
            comments=comments,
        )


@app.route('/post/add', methods=['GET', 'POST'])
@login_required
# def create_post():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         post = Posts(title=title, content=content, author=current_user)
#         db.session.add(post)
#         return redirect(url_for('index'))
#     return render_template('create_post.html')
def create_post():
    if request.method == 'GET':
        return render_template('create_post.html', post={})
    elif request.method == 'POST':
        if not request.form or not all(
            key in request.form for key in REQUIRED_DIELDS
        ):
            return {'error': 'All required fields are required'}, 400

        if not set(REQUIRED_DIELDS) - set(request.form):
            return render_template(
                'create_post',
                error='Something is wrong!',
                post=request.form,
            )

        for key in REQUIRED_DIELDS:
            if not REQUIRED_DIELDS[key](request.form[key]):
                return {'error': f'{key} is invalid'}, 400

        with get_session() as session:
            post = Posts(**request.form)
            session.add(post)
            session.commit()
            return redirect(
                url_for('create_post', post_id=post.id)
            )



@app.route('/post/<int:post_id>/comments', methods = ["POST"])
@login_required
def add_comments(post_id):
    if not request.form or 'content' not in request.form:
        return {'error': 'Content is required'}, 400
    comment = Comment(content=request.form['content'], post_id=post_id, author=current_user)
    print(comment)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


@app.route('/post/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        with get_session() as session:
            users = Users(
                username=request.form['username'],
                password_hash=request.form['password'],
            )

            existing_user = session.query(Users).filter_by(username=users.username).first()
            if existing_user:
                return 'Пользователь с таким именем уже существует', 409


            new_users = Users(
                username=request.form['username'],
                password_hash=request.form['password'],
            )
            new_users.set_password(new_users.password_hash)
            session.add(new_users)
            session.commit()

            return redirect(url_for('login'))
    else:

        return render_template('register.html')


@app.route('/post/login', methods=['GET', 'POST'])

def login():
    with get_session() as session:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = session.query(Users).filter_by(username=username).first()

            if user is None or not user.check_password(password):

                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('index'))
        return render_template('login.html', title='Вход')


@app.route('/post/logout')
def logout():

    with get_session() as session:
        logout_user()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    # from db import all_post, viewing_article1, viewing_article
    # breakpoint()