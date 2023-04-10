from docutils import nodes
from sphinx.environment.adapters.toctree import TocTree
from sphinx.addnodes import compact_paragraph

def add_google_link(app, doctree, docname):
    """Append a link to Google.com to the end of the table of contents."""

    # if docname == 'index':
        # Create a new list item node with a link to Google.com
    link_text = 'Google'
    link_node = nodes.reference('', link_text, refuri='https://www.google.com', internal='false')
    cp_node = compact_paragraph('', '', link_node, classes='toctree-l1')
    item_node = nodes.list_item('', cp_node)

    # Find the table of contents node and append the new list item
    toc_tree = TocTree(app.env)
    raw_tree = toc_tree.get_toctree_for(
            docname, app.builder, True, maxdepth=-1
        )
    
    if raw_tree:
        raw_tree.children[2].append(item_node)

    print(raw_tree)
    print(type(raw_tree))
    
    for child_node in raw_tree.children:
        print(child_node.astext())


def add_rapid_docs_js(app, pagename, templatename, context, doctree):
    if pagename == 'central-api':        
        context["script_files"].append('_static/js/rapidoc-min.js')
        # context["toc"] = '<ul><li><a class="reference internal" href="#">The API</a></li><ul>'ß
        # print(context)
        # this is not working
        # app.add_js_file('js/rapidoc-min.js')

#def add_custom_link(app, doctree, docname):
    #if docname == 'index':
    #    node = doctree.traverse(addnodes.toctree)[0]
    #    toc = app.env.resolve_toctree(docname, app.builder, node)
    #    print(toc)

def setup(app):
    app.connect('html-page-context', add_rapid_docs_js) 
    # app.connect('doctree-resolved', add_google_link)