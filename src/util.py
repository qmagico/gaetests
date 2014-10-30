import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/template'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def write_template(handler, tmpl, data):
    template = JINJA_ENVIRONMENT.get_template(tmpl)
    handler.response.write(template.render(data))
