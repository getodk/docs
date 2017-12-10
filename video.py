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

    vsrc = node["uri"]
    spth = ".%s" % vsrc
    dpth = "./build/_videos/%s" %vsrc[vsrc.rfind('/')+1:]

    shutil.copyfile(spth, dpth)

    src = "../_videos/%s" % vsrc[vsrc.rfind('/')+1:]
        
    attrs = {
            "src":"%s" %src,
            "controls":"controls",
            "muted":"muted",
            "style":"max-width:100%",
        }
   
    
    alt = node["alt"]
                                                                                                                                
    self.body.append(self.starttag(node, "video", **attrs))
    self.body.append("<p> %s </p>" %alt)
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
    option_spec = { 'alt': directives.unchanged,
    }

    def run(self):

        alt = "Video cannot be played."

        if "alt" in self.options:
            alt = self.options["alt"]

        uri = directives.uri(self.arguments[0])

        return [video_node(uri = uri, alt = alt)]

def setup(app):

    app.add_node(video_node, html = (visit_video_node, depart_video_node), 
    	                     latex = (visit_video_other, depart_video_node),
    	                     text = (visit_video_other, depart_video_node),
    	                     )
    app.add_directive("video", Video)
