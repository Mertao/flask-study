from flask import Blueprint, request, render_template
from functions import load_posts


main_blueprint = Blueprint("main_blueprint",
                           __name__,
                           template_folder='templates',
                           static_folder='static')


@main_blueprint.route('/', )
def main():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search():
    search_by = request.args['s']
    if search_by:
        posts = [x for x in load_posts()
                 if search_by.lower() in x['content'].lower()]
        return render_template('post_list.html',
                               search_by=search_by,
                               posts=posts)
    return "<h2>Вы ничего не ввели</h2>"
