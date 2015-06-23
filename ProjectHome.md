It Works !
  * test it on http://goflow.alwaysdata.net/chat/
  * browse posts on http://goflow.alwaysdata.net/chat/browse/chat/post/

  * provides a chat client to embed in the pages of a django site

## Demo specifications ##
  * users of a same django group can chat together
  * an authentication backend allows any user to log in with a password that corresponds to a chat room (_room1_, _room2_, _room3_)
  * user12 (password "u") has the two groups _room1_ and _room2_
  * technos: Ajax (Dojo) and dojango
## Setup ##
  * unzip django-chat archive or checkout it
  * install dojango (http://dojango.googlecode.com/files/dojango-0.3.tar.gz) in the python path
  * create database (python manage.py syncdb --noinput), the superuser is "admin" password "chat"
  * python manage.py runserver
    * url of the test page: http://localhost:8000/chat
    * url of the admin page: http://localhost:8000/chat/admin
## Screenshots ##
![http://djangodev.free.fr/django-chat/chat-screenshot.png](http://djangodev.free.fr/django-chat/chat-screenshot.png)