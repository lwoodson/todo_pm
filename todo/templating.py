import os
from todo import TodoException

try:
    os.environ["TODO_TEMPLATE_DIR"]
except KeyError:
    raise TodoException("TODO_TEMPLATE_DIR is not set!")

def read(tmpl_name):
    tmpl_path = os.path.join(os.environ["TODO_TEMPLATE_DIR"], tmpl_name)
    if not os.path.exists(tmpl_path):
        raise TodoException("%s template does not exist at %s" % (tmpl_name, tmpl_path))
    file = open(tmpl_path, 'r')
    try:
        return file.read()
    finally:
        file.close()

    
