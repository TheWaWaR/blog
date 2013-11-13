#coding: utf-8

from flask import (Blueprint, abort, redirect, url_for,
                   render_template, current_app)
from utils.gvars import PAGES, POSTS, CATEGORIES
from utils.markdown import init_pages_posts

bp = Blueprint('blog', __name__)
CONTENTS = {}

        

@bp.route('/')
def home():
    ''' Home '''
    return render_template('home.html',
                           pages=PAGES,
                           posts=POSTS.values(),
                           categories=CATEGORIES)

    
@bp.route('/category/<name>')
def category(name):
    return render_template('category.html',
                           name=name,
                           pages=PAGES,
                           posts=CATEGORIES[name],
                           categories=CATEGORIES)

    
@bp.route('/page/<name>')
def page(name):
    ''' Some page (such as about-me) '''
    data = PAGES.get(name, None)
    if data is None:
        abort(404)
        
    return render_template('page.html', data=data)

    
@bp.route('/post/<name>')
def post(name):
    ''' Some post '''
    
    post = POSTS.get(name, None)
    if post is None:
        abort(404)
        
    return render_template('post.html', post=post)


@bp.route('/rebuild')
def rebuild():
    PAGES.clear()
    POSTS.clear()
    CATEGORIES.clear()
    init_pages_posts(current_app.root_path)
    return redirect(url_for('blog.home'))
