"""
@summary: Has all the necessary functions needed to render a page to HTML. 
@author: Abhishek Shrivastava <i.abhi27 [at] gmail [dot] com>

"""
import re
import sys
from config import PAGE_NAME_2_TITLE
from yaptu  import copier

def render(page_name, value_dict):
    """
    Pass the name of the controller's template file and the dict of values to substitute.
    Returns ready-to-be-pushed HTML.
    
    """
    page_tpl = open('templates/'+page_name+'.tpl','r').read()
    render_tpl = open('templates/index.tpl','r').read()
    
    page_html = templatify(page_tpl, value_dict)      
    
    return templatify(render_tpl, {'page_html' : page_html, 
                                   'page_title' : PAGE_NAME_2_TITLE[page_name] })
    
def push_html(html):
    """
    Pushes the HTML to browser and quits.
    
    """
    print "Content-Type: text/html"
    print
    print html
    sys.exit(1)
    
def push_zip(filename, length, data):
    """
    Pushes the ZIP file to browser and quits. User gets to see a 'Save As' option.
    
    """
    print "Content-type: application/zip"
    print "Content-Disposition: attachment; filename=%s" % filename
    print "Content-Title: %s" % filename
    print "Content-Length: %i" % length
    print
    print data
    sys.exit(1)
    
def error(error_msg):
    """
    Throws the error message in a rendered HTML way and quits.
    
    """
    error_html = render('error',{'error' : error_msg})
    push_html(error_html)

def templatify(tpl, values):
    """
    Custom wrapper around the YAPTU template engine. Does the usual job.
    
    """
    class DecoyFile:
    
        def __init__(self):
            self.data = []
            
        def write(self, line):
            self.data.append(line)
        
        def read(self):
            return "".join(self.data)
    
    rex=re.compile('%([^@]+)s')
    rbe=re.compile('\+')
    ren=re.compile('-')
    rco=re.compile('= ')
    decoy = DecoyFile()    
    cop = copier(rex, values, rbe, ren, rco, ouf=decoy)
    lines_block = [line+'\n' for line in tpl.split('\n')]
    cop.copy(lines_block)
    return decoy.read()