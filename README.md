min.py
======

A mini python MVC framework that 'just' works! Intended to work as a CGI application for blazing speed development (esp. during Hackathons).

Why this?
========
I wrote this framework in 4 hours because there was a hackathon going on and I didn't want to waste my crucial time downloading, installing and learning a new framework for building my app. All I needed was a few things from my framework:

* **URL handling** : Know which URL makes sense, which doesn't and how to deal with them in a graceful manner.
* **Controllers launching** : When to launch which controller to do the job the user is asking for.
* **Template engine** : Because I hate writing HTML code within Python code, or for any business logic code for that matter.
* **Output rendering** : Take care of the response data format - HTML, JSON, or whatever. And other HTTP header stuff like cache-control, etc
* **index.py** : Something that sums up all of this - Parse the URL, calls the controller, load the template, push the controller data into the template, and render to the user.

The framework doesn't have a Model wrapper around the database, so I should rather call this just a 'VC' framework. I apparently felt writing direct SQL queries was much faster during initial stages of your app.

Anyways, the good part is there's no installation required as it was intended to work as a CGI bin application so that you don't have to restart your Apache everytime you make a code change in the controller. Simply copy paste the code into you CGI-BIN folder, (assuming you have that enabled) and you can directly get to writing the business logic code in Python to quickly build your app.

PS : I am not allowed to share the source code of the App which I built using this framework, but I have added a sample Hello World page. :)

Didn't Work ?
=============

Well most probably there's only 1 and only 1 reason. Your python or apache configuration sucks.
To fix it:
* Make sure you install python on your system
* Add this into your apache config file to make cgi-bin work with python interpreter:

===
     <Directory "<Path to your code folder>">
          AllowOverride All
          Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
          Order allow,deny
          Allow from all
          AddHandler cgi-script .py # tell Apache to handle every file with .py suffix as a cgi program
          AddHandler default-handler .html .htm  # tell Apache to handle HTML files in regular way
     </Directory> 

