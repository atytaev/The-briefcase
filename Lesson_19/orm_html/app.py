from flask import Flask, render_template, request, redirect, url_for
from models import Posts, Comment
from db import get_session

app = Flask(__name__, template_folder='templates')

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
@app.route('/')
def redirect_to_posts():
    return redirect(url_for('posts'))

@app.route('/posts', methods = ['GET', 'POST'])
def posts():
    if request.method == 'GET':
        ordering = 'id'
        if ORDERING_QUERY_KEY in request.args:
            ordering = request.args[ORDERING_QUERY_KEY]

        with get_session() as session:
            posts = session.query(Posts)
            post_data = [
                post_to_dict(post)
                for post in posts
            ]
        return post_data

    elif request.method == 'POST':
        for key in REQUIRED_DIELDS:
            if key not in request.json:
                return {'error': f'{key} is required'}, 400
            elif not REQUIRED_DIELDS[key](request.json[key]):
                return {'error': f'{key} is invalid'}, 400

        with get_session() as session:
            post = Posts(**request.json)
            session.add(post)
            session.commit()
            return {'message': 'Post added successfully'}, 201


@app.route('/posts/<int:post_id>/', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def post(post_id):
    with get_session() as session:
        post = session.query(Posts).filter_by(id=post_id).first()
        if post is None:
            return {'error': 'Post not found'}, 404

        post_data = post_to_dict(post)

        if request.method == "GET":
            post_dict =post_to_dict(post)

            comments = session.query(Comment).filter_by(post_id=post_id)

            post_dict['comment'] = (
                comments_data_to_dict(comments)
            )
            return post_dict

        elif request.method == 'PUT':
            for key in REQUIRED_DIELDS:
                if key not in request.json:
                    return {'error': f'{key} is required'}, 400
                elif not REQUIRED_DIELDS[key](request.json[key]):
                    return {'error': f'{key} is invalid'}, 400

            for key, value in request.json.items():
                setattr(post, key, value)
            return {'message': 'Recipe update successfully'}, 200

        elif request.method == 'PATCH':
            for key in request.json:
                if key not in REQUIRED_DIELDS:
                    return {'error': f'{key} is not allowed'},400
                elif not REQUIRED_DIELDS[key](request.json[key]):
                    return {'error': f'{key} is invalid'},400

            for key, value in request.json.items():
                setattr(post, key, value)
            return {'message': 'Recipe update successfully'}, 200
        elif request.method == 'DELETE':
            session.delete(post)
            return {'message': 'Post deleted successfully'}, 204




if __name__ == '__main__':
    app.run(debug=True)
    # from db import all_post, viewing_article1, viewing_article
    # breakpoint()