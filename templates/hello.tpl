<h1>Welcome, %(USER)s 
from %(CITY)s</h1>
<h2>Share, Like & Save Time</h2>

<div class="row">
<div class="well">
<h3>You are ... </h3><br/>
+ for age in range(1, int(AGE)):
	<a class="btn btn-primary topmar" style="height:%(12*age)spx">
	<i class="icon-heart icon-white"></i>
	</a>	
-
<a class='btn btn-primary topmar'>
<i class="icon-heart icon-white"></i>
%(age+1)s
 years old!</a>
</div>

Alternative URL for this page: <a href='/hello/%(USER)s
/%(AGE)s
/%(CITY)s?force=1'>here</a>