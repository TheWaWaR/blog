#coding: utf-8

# ==============================================================================
#  Markdown parser
# ==============================================================================
import os
import misaka
from misaka import HtmlRenderer, SmartyPants
from xml.sax.saxutils import escape
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create a custom renderer
class BleepRenderer(HtmlRenderer, SmartyPants):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % escape(text.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

    def image(self, link, title, alt):
        return '''<figure><img class="bordered-img" src="%(src)s">
        <figcaption>%(title)s</figcaption> </figure>''' % dict(src=link, title=alt, alt=alt)

        
# And use the renderer
renderer = BleepRenderer()
md = misaka.Markdown(renderer,
        extensions=misaka.EXT_FENCED_CODE | misaka.EXT_NO_INTRA_EMPHASIS)


# ==============================================================================
#  
# ==============================================================================
from .gvars import PAGES, POSTS, CATEGORIES

def parse_header(data):
    ''' header ~ meta '''
    meta = {}
    for line in data.splitlines():
        if line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            meta[key] = value
    return meta

    
def parse_md(path):
    data = None
    
    if os.path.exists(path):
        with open(path, 'r') as f:
            f_data = unicode(f.read(), encoding='utf8')
            header, body = f_data.split('**********', 1)
            data = parse_header(header)
            data['content'] = md.render(body)
            
    print 'get_content.path:', path
    # print 'get_content.content:', content
    return data

    
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
        post = parse_md(path)
        POSTS[name] = post
        category = post.get('category', 'default')
        if category in CATEGORIES:
            CATEGORIES[category].append(name)
        else:
            CATEGORIES[category] = [name]

    print '===================='
    print 'PAGES, POSTS, CATEGORIES:', PAGES, POSTS, CATEGORIES
    print '===================='
    
