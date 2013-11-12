#coding: utf-8

from flask import Blueprint, abort, render_template
from utils.gvars import PAGES, POSTS

bp = Blueprint('blog', __name__)
CONTENTS = {}

        

@bp.route('/')
def home():
    ''' Home '''
    titles = []
    for _, post in POSTS.iteritems():
        titles.append(post['title'])
    return '\n'.join(titles)

    
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
    
    data = POSTS.get(name, None)
    if data is None:
        abort(404)
        
    return render_template('post.html', data=data)

