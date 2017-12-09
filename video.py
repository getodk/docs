import os
import shutil
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

class video_node(nodes.General, nodes.Element): pass

def visit_video_node(self, node):

    if os.path.exists("./build/_videos"):
       pass
    else:   
       os.makedirs("./build/_videos/")

    vsrc = node["id"]
    spth = ".%s" % vsrc
    dpth = "./build/_videos/%s" %vsrc[vsrc.rfind('/')+1:]

    shutil.copyfile(spth, dpth)
        
    attrs = {
            "controls":"controls",
            "muted":"muted",
            "style": "max-width:100%",
        }

    src = "\"../_videos/%s\"" % vsrc[vsrc.rfind('/')+1:]
    
    self.body.append(self.starttag(node, "video", **attrs))
    self.body.append("<source src = %s>" % src)
    self.body.append("</video>")
  
def visit_video_other(self, node):
    pass

def depart_video_node(self, node):
    pass

class Video(Directive):

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        return [video_node(id = self.arguments[0])]

def setup(app):

    app.add_node(video_node, html = (visit_video_node, depart_video_node), 
    	                     latex = (visit_video_other, depart_video_node),
    	                     text = (visit_video_other, depart_video_node),
    	                     )
    app.add_directive("video", Video)
