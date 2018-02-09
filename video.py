import os
import shutil
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

def yes_no(name, arg):

    if arg == 'yes' or arg == 'true':
       return name
    elif arg == 'no' or arg == 'false':
       return None
    else:
       raise Exception("Value for {} attribute can only be a boolean" .format(name))

def preload_choice(arg):

    if arg == 'auto' or arg == 'metadata' or arg == 'none':
       return arg
    else:
       raise Exception("Value for preload attribute can only be auto, metadata or none")

class video_node(nodes.General, nodes.Element): pass

def visit_video_html(self, node):

    if os.path.exists("./build/_videos"):
       pass
    else:   
       os.makedirs("./build/_videos/")

    vsrc = node["uri"]
    spth = "./src%s" % vsrc
    dpth = "./build/_videos/%s" %vsrc[vsrc.rfind('/')+1:]

    shutil.copyfile(spth, dpth)

    src = "../_videos/%s" % vsrc[vsrc.rfind('/')+1:]
        
    attrs = {
            "src":"%s" %src,
            "style":"max-width:100%",
        }

    if node["poster"] is not None:
       psrc = node["poster"]
       p_spth = "./src%s" % psrc
       p_dpth = "./build/_videos/%s" %psrc[psrc.rfind('/')+1:]

       shutil.copyfile(p_spth, p_dpth)

       psrc = "../_videos/%s" % psrc[psrc.rfind('/')+1:]
       attrs["poster"] = "%s" % psrc    
   
    if node["autoplay"] == "autoplay":
       attrs["autoplay"] = "autoplay"

    if node["controls"] == "controls":
       attrs["controls"] = "controls"

    if node["loop"] == "loop":
       attrs["loop"] = "loop" 

    if node["muted"] == "muted":
       attrs["muted"] = "muted"

    if node["preload"] is not None:
       attrs["preload"] = "%s" % node["preload"]

    if node["cl"] is not None:
       attrs["class"] = "%s" % node["cl"]
                                                                                                                                
    self.body.append(self.starttag(node, "video", **attrs))

def depart_video_html(self, node):
    self.body.append("</video>")    
  
def visit_video_nonhtml(self, node):
    pass
    
def depart_video_nonhtml(self,node):
    pass

class Video(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = { 
                'autoplay' : directives.unchanged,
                'controls' : directives.unchanged,
                'loop' : directives.unchanged,
                'muted' : directives.unchanged,
                'poster' : directives.unchanged,
                'preload' : directives.unchanged,
                'class' : directives.unchanged,
        }


    def run(self):

        autoplay = None
        controls = "controls"
        loop = None
        muted = "muted"
        poster = None
        preload = None
        cl = None

        if "autoplay" in self.options:
            autoplay = yes_no("autoplay",self.options["autoplay"])

        if "controls" in self.options:
            controls = yes_no("controls",self.options["controls"])
            
        if "loop" in self.options:
            loop = yes_no("loop",self.options["loop"])
            
        if "muted" in self.options:
            muted = yes_no("muted",self.options["muted"])
            
        if "poster" in self.options:
            poster = directives.uri(self.options["poster"])                
           
        if "preload" in self.options:
            preload = preload_choice(self.options["preload"])

        if "class" in self.options:
            cl = self.options["class"]    

        uri = directives.uri(self.arguments[0])

        vid = video_node(uri = uri, autoplay = autoplay, controls = controls, 
            loop = loop, muted = muted, poster = poster, 
            preload = preload, cl = cl)        
        
        self.state.nested_parse(self.content, self.content_offset, vid)
         
        return [vid]

def setup(app):

    app.add_node(video_node, html = (visit_video_html, depart_video_html), 
    	                     latex = (visit_video_nonhtml, depart_video_nonhtml),
                             epub = (visit_video_nonhtml, depart_video_nonhtml),
                             text = (visit_video_nonhtml, depart_video_nonhtml),
    	                     )
    app.add_directive("video", Video)

