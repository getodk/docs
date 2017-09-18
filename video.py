def setup(app):
    app.add_config_value('video_include_videos', False, 'html')

    app.add_node(videolist)
    app.add_node(video,
                 html=(visit_video_node, depart_video_node),
                 latex=(visit_video_node, depart_todo_node),
                 text=(visit_video_node, depart_video_node))

    app.add_directive('video', VideoDirective)
    app.add_directive('vidolist', VideolistDirective)
    app.connect('doctree-resolved', process_video_nodes)
    app.connect('env-purge-doc', purge_videos)

    return {'version': '0.1'}

# from docutils import nodes
#
# class video(nodes.Admonition, nodes.Element):
#     pass
#
# class videolist(nodes.General, nodes.Element):
#
# def visit_video_node(self, node):
#     self.visit_admonition(node)
#
# def depart_video_node(self, node):
#     self.depart_admonition(node)
#
# from docutils.parsers.rst import Directive
#
# class VideoListDirective(Directive):
#
#     def run(self):
#         return [videolist('')]

# from sphinx.locale import _

# class VideoDirective(Directive):
#
#     has_content = False
#
#     def run(self):
#         env = self.state.document.settings.env
#
#         targetid = "video-%d" % env.new_serialno('video')
#         targetnode = nodes.target('', '', ids=[targetid])
#
#         video_node = video('\n'.join(self.content))
#         video_node += nodes.title(_('Video'), _('Video'))
#         self.state.nested_parse(self.content, self.content_offset, video_node)
#
#         if not hasattr(env, 'video_all_videos'):
#             env.video_all_videos = []
#         env.video_all_Videos.append({
#             'docname': env.docname,
#             'lineno': self.lineno,
#             'video': video_node.deepcopy(),
#             'target': targetnode,
#         })
#
#         return [targetnode, video_node]

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

def align(argument):
    return directives.choice(argument, ('left', 'center', 'right'))
class Video(directive):

    require_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.nonnegative_int,
                   'width': directives.nonnegative_int,
                   'scale': directives.nonnegative_int,
                   'align': align
                   }
    has_content = False

    def run(self):
        reference = directives.uri(self.arguments[0])
        self.options['uri'] = reference
        image_node = nodes.image(rawsource=self.block_text,
                                 **self.options)
        return [image_node]
# def purge_videos(app, env, docname):
#     if not hasattr(env, 'video_all_videos'):
#         return
#     env.video_all_videos = [video for video in env.video_all_videos
#                             if video['docname'] != docname]
#
# def process_video_nodes(app, doctree, fromdocname):
#     if not app.config.video_include_videos:
#         for node in doctree.traverse(video):
#             node.parent.remove(node)
#
#     env = app.builder.env
#
#     for node in doctree.transverse(videolist):
#         if not app.config.video_include_videos:
#             node.replace_self([])
#             continue
#
#         content = []
#
#         for video_info in env.video_all_videos:
#             para = nodes.paragraph()
#             filename = env.doc2path(video_infor['docname'], base=None)
#             description = (
#                 _('(The original entry is located in %s, line%d and can be found ') %
#                 (filename, video_info['lineno']))
#             para += nodes.Text(description, description)
#
#             newnode = nodes.reference('', '')
#             innernode = nodes.emphasis(_('here'), _('here'))
#             newnode['refdocname'] = video_info['docname']
#             newnode['refuri'] = app.builder.get_relative_uri(
#                 fromdocname, video_info['docname'])
#             newnode['refuri'] += '#' + video_infor['target']['refid']
#             newnode.append(innernode)
#             para += newnode
#             para += nodes.Text('.)', '.)')
#
#             content.append(video_info['video'])
#             content.append(para)
#
#         node.replace_self(content)
