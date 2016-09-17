<h1>Music Recommender System Using <a href = "http://django-recommends.readthedocs.io/en/latest/">Django Recommends</a></h1>

This is a simple recommendation system based on <strong>Item based Collaborative Filtering</strong> algorithm.

I used <a href="http://django-recommends.readthedocs.io/en/latest/">Django Recommends</a> for making recommendations,

<a href="http://sorl-thumbnail.readthedocs.io/en/latest/">Sorl-thumbnail</a> for creating thumbnail images,

<a href="http://rateyo.fundoocode.ninja/">RateYo!</a> for star rating module,

and 

<a href="http://materializecss.com/">Materialize</a> for front end.

<h2>Use</h2>

 $ python manage.py recommends_precompute # for precomputing item similarities matrix
 
 
 
 $ python manage.py meanstar # for computing each item's mean score of star ratings


You can also use <a href="http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html">celery</a> for periodic tasks.


<h2>Reference</h2>

<a href="http://shop.oreilly.com/product/9780596529321.do">Programming Collective Intelligence</a> <i>chap2. Making Recommendations</i>

<a href="http://yumere.tistory.com/72">Blog posting</a>

<a href="http://nbviewer.jupyter.org/github/dsksd/musicrecommender/blob/master/reference/Recommander%20System%28by%20dsksd%29.ipynb">My githubviwer</a>

<h2>Documentation</h2>

<h3>1. Django Recommends : <a href="http://nbviewer.jupyter.org/github/dsksd/musicrecommender/blob/master/reference/Django-Recommends.ipynb">here</a></h3>

<h3>2. Sorl-thumbnail : <a href="http://nbviewer.jupyter.org/github/dsksd/musicrecommender/blob/master/reference/sorl-thumbnail.ipynb">here</a></h3>

<h3>3. RateYo! : <a href="http://nbviewer.jupyter.org/github/dsksd/musicrecommender/blob/master/reference/RateYo.ipynb">here</a></h3>

<h2>Screenshot</h2>

<img src="https://github.com/DSKSD/musicrecommender/blob/master/reference/screenshot1.jpg"/>

<img src="https://github.com/DSKSD/musicrecommender/blob/master/reference/screenshot2.jpg"/>


<a href="https://github.com/DSKSD/">@DSKSD</a>