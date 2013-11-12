#!/usr/bin/env python
#coding: utf-8

import os
from flask import Flask
from blog.views import bp as bp_blog
from utils.markdown import parse_md
from utils.gvars import PAGES, POSTS

def init_pages_posts(root_path):
    pages_path = os.path.join(root_path, 'markdowns/pages')
    posts_path = os.path.join(root_path, 'markdowns/posts')
    
    for name in os.listdir(pages_path):
        if name[-3:] != '.md': continue
        path = os.path.join(pages_path, name)
        PAGES[name] = parse_md(path)

    for name in os.listdir(posts_path):
        if name[-3:] != '.md': continue
        path = os.path.join(posts_path, name)
        POSTS[name] = parse_md(path)

    print '===================='
    print 'PAGES, POSTS:', PAGES, POSTS
    print '===================='
    
        
def create_app():

    tApp = Flask(__name__)
    tApp.config.from_pyfile('settings.py')

    blueprints = [bp_blog]
    for bp in blueprints:
        tApp.register_blueprint(bp)

    init_pages_posts(tApp.root_path)
    ############################################################
    # Request management
    @tApp.before_request
    def before_request():
        pass

    # Error Handler
    @tApp.errorhandler(404)
    def error_404(e):
        return 'Not Found! There is nothing here......', 404

    return tApp


        
app = create_app()

if __name__ == '__main__':
    import sys
    try:
        port = int(sys.argv[1])
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception, e:
        print 'Usage: python webapp.py <port>'
        print e
