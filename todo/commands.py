import os, sys
from todo import TodoException
from todo import templating

def initialize(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_path = os.path.join(dir, 'TODO') 
    if os.path.exists(file_path):
        raise TodoException("%s already exists!  Remove and try again\n" % file_path)

    try:
        file = open(file_path, 'w')
        try:
            file.write(templating.read('TODO.tmpl'))
            sys.stdout.write("created %s\n" % file_path)
        finally:
            file.close()
    except IOError, e:
        raise TodoException("Could not create %s: %s" % (file_path, e))

