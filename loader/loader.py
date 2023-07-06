from flask import Blueprint, request, render_template
from functions import load_posts, uploads_posts


loader_blueprint = Blueprint("loader",
                             __name__,
                             url_prefix='/post',
                             static_folder='static',
                             template_folder='templates')
extensions: list[str] = ['jpg', 'jpeg', 'png']


@loader_blueprint.route('/form/')
def form_main():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=["POST"])
def upload():
    try:
        picture = request.files['picture']
        content = request.values['content']
        filename = picture.filename

        if not (any([filename.endswith(x) for x in extensions])):
            return f"<h1> Недопустимое расширение файла {filename}"
    except FileNotFoundError:
        return "<h1>Файл не найден</h1>"
    except PermissionError:
        return "<h1>Файл не найден</h1>"
    else:
        posts = load_posts()
        posts.append({
            "picture": f"/uploads/images/{filename}",
            "content": content
        })
        picture.save(f'uploads/images/{filename}')
        uploads_posts(posts)

        return render_template("post_uploaded.html",
                               picture=f"/uploads/images/{filename}",
                               content=content)
