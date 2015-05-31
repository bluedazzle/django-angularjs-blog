#New RaPo Site#
A simple blog site powered by django and angularjs

Demo: [New RaPo Site][1]
---

##How to use?##

1、Download the zip package:

    wget https://github.com/bluedazzle/django-angularjs-blog.git

or cilick the button "Download ZIP" rightside.

2、Unzip the package, enter the folder which you unziped, then:

    pip install -r requirement.txt

3、Configure the database backend which you need in `NewRaPo/settings/dev.py` or create your own produce settings file in settings/  

4、Create database in database you choose, and run:

    python manage.py syncdb

5、run test:

    python manage.py test

6、run test server:

    python manage.py runserver

or configure your produce server software like uWSGI、apache.

##Feature##

The simple blog site include four parts:

1、`Blog`: Show your articles and comment your article.  
2、`Knowledge`: Something like a private "baidu zhidao", you can add any kinds of questions and answers.  
3、`Laboratory`: something interesting or new IT technologies you can have a try here.  
4、`About` : a static page you can edit anyting you want to show to others.  

[1]: http://www.rapospectre.com

