Researchgate crawler
=========

A crawler for [ResearchGate](http://researchgate.net).

ResearchGate is a scientific social network that displays the publications, ciations
and statistics of a given author.  
This crawler is prepared to create, given an author ID, a set of authors and publications [JSON files](http://www.json.org) that can be easily exported into any programming language to further analyse.  

Questions
---------
**How can I install it?**  
You'll need ``python2.7``.

Install it over python virtual env:
```bash
cd project_folder
virtualenv venv
source venv/bin/activate
pip install git+git://github.com/jaumebonet/RGcrawler.git@master --process-dependency-links --allow-all-external --trusted-host github.com
```
This should do the trick. Remember that you'll need to call
```bash 
source venv/bin/activate
```
every time before running the script and 
```bash
deactivate
```
after finishing it...

**How can I run it?**  
The only thing you need to type is:
```bash
python -m rgcrawler --authorID <author_id>
```

**Where can I find the autor id?**  
When you look to one of your profile page, the author id is the string that
appears at the end and usually includes your name.

**Would this work with multiple authors?**  
Yes, you can create a script that queries multiple authors calling the program multiple times. If a called author is co-author with a previous called one, some of the data will be retrieved from the files and not requested online.

**Why some authors are not recognised when I can see them in my browser?**
Well. Some authors have they profile configured in such a way that you can't actually see their profile unless you are logged to ResearchGate. I'm sure the identification cookies can be loaded so that it will look like you are connected, but I´m not going to get into this right now. But... you know... feel free to fork and build upon this!!

