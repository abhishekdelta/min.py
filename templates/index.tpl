<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <meta charset="utf-8">
    <title>%(page_title)s</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">       
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="description" content="min.py is a minimal python framework that just works!" />
	<meta name="keywords" content="min.py, python, framework" />
	<meta name="author" content="Abhishek Shrivastava [abhishekdelta] - i.abhi27 [at] gmail [dot] com">

    <!-- Le styles -->
    <link href="/public/css/bootstrap.min.css" rel="stylesheet">
    <link href="/public/css/custom.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; 
      }
    </style>
    <link href="/public/css/bootstrap-responsive.min.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="/favicon.ico">
        
    
    <script src="/public/js/jquery.js"></script>
    <script src="/public/js/bootstrap.min.js"></script>
  </head>

  <body>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="/">min.py</a>
            <ul class="nav pull-right">          
              <li><a class="pull-right" data-toggle="modal" href="#about">About</a></li>
              <li><a class="pull-right" data-toggle="modal" href="#contact">Contact</a></li>
            </ul>

          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

      %(page_html)s
		
    </div> <!-- /container -->

	<div class="modal hide" id="about">
	    <div class="modal-header">
	    <button type="button" class="close" data-dismiss="modal">×</button>
	    <h3>About min.py</h3>
	    </div>
	    
	    <div class="modal-body">
	    <p>min.py is minimal python framework that just works!</p>
	    </div>
	    
	    <div class="modal-footer">
	    <a href="#" class="btn" data-dismiss="modal">Close</a>
	    </div>
    </div>
	<div class="modal hide" id="contact">
	    <div class="modal-header">
	    <button type="button" class="close" data-dismiss="modal">×</button>
	    <h3>Contact</h3>
	    </div>
	    
	    <div class="modal-body">
	    <p>
	    <ul>
	    <li>Abhishek Shrivastava : i.abhi27 [at] gmail [dot] com</li>
	    </ul>
	    </p>
	    </div>
	    
	    <div class="modal-footer">
	    <a href="#" class="btn" data-dismiss="modal">Close</a>
	    </div>
    </div>    
   
  </body>
</html>