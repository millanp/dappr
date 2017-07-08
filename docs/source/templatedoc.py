from docutils import nodes
from docutils.parsers.rst import Directive

class templatedoc(nodes.General, nodes.Element):
    pass

class TemplatedocDirective(Directive):
    def run(self):
        return [templatedoc('')]

def visit_templatedoc_html(self, node):
    return 'haw haw'

def depart_templatedoc_html(self, node):
    return 'hee hee'

def setup(app):
    app.add_node(templatedoc,
                 html=(visit_templatedoc_html, depart_templatedoc_html))
