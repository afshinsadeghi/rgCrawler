Researchgate python crawler based on [Scrapy](http://Scrapy.org)
=========

A crawler for [ResearchGate](http://researchgate.net).

ResearchGate is a scientific social network that displays the publications, projects
and analysis of an author.
The crawler, given an author_name_string, produces set of authors and publications in the format of json

Installation:
---------
Requirments:
``pip,python2.7``.

1. make sure you have activated python virtual env:

2.cd project_folder
virtualenv venv
source venv/bin/activate
pip install git+git://github.com/sadeghiafshin/rgCrawler.git@master --process-dependency-links
```
source venv/bin/activate


**How can I run it?**  
The only thing you need to type is:
```bash
python -m rgcrawler --authorID <author_name_string>
```

**Where can I find the  author_name_string?**
When you look to one of your profile page, the author id is the string that
appears at the end and usually includes your name.



This code is inspired from by RGCrawler made by jaumebonet.
The code open source , you can take it and change and reuse it as your will.