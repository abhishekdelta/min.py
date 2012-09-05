"""
@summary: A sample controller. 
@author: Abhishek Shrivastava <i.abhi27 [at] gmail [dot] com>

"""
from config import db
from render import error

cur = db.cursor()

KEY_NAME = 'name'
KEY_CITY = 'city'
KEY_AGE  = 'age'

def output(httpin): 
    """
    Every controller must have this output function atleast. This is the entry point.
    Input is a dict of POST/GET variables and any other extra keys added during URL parsing
    Output must be a dict of Key-Value pairs that would be substituted in template using YAPTU.
    
    """
    
    if KEY_NAME in httpin:
        name = httpin[KEY_NAME]
    else:
        name = 'Anonymous'
        
    if KEY_CITY in httpin:
        city = httpin[KEY_CITY]
    else:
        city = 'Hyderabad, India'
        
    if KEY_AGE in httpin:
        age = httpin[KEY_AGE]
    else:
        age = '22'   
                                          
    force = ('force' in httpin and httpin['force'] == '1')

    #rows = cur.execute("SELECT * FROM users WHERE name=%s", name).fetchall()
    rows = []
    
    if len(rows) == 0 and not force:
        error("Oops! You are not registered. You must be registered to see this page. Or try with <a href='./?force=1'>force</a>!")
    
    return {'USER' : name,
            'AGE'  : age, 
            'CITY' : city}

