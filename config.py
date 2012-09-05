"""
@summary: List of global configurations which you want to use everywhere else. 
@author: Abhishek Shrivastava <i.abhi27 [at] gmail [dot] com>

"""

# Must add an entry here for every new page added to the site
VALID_PAGES = ['hello']

# Optional, but if you want to have some title for a page, put it here in a dict format. 
# Key is page name, value is the title.
PAGE_NAME_2_TITLE = {'error' : 'Error',
                     'hello' : 'Welcome to min.py!'}

# This is where any file uploads go.
UPLOAD_DIR = "/var/www/workspace/git/min.py/uploads/"

# Default page when nothing is in the URL
DEFAULT_PAGE = "hello"

# MySQL connection is created here once and for all
import MySQLdb
db = MySQLdb.connect("deshub.com", "root", "root", "deshub")



