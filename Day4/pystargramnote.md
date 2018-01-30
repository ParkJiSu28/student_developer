#1.pystargram 기획.

***
**서버에  접근할 URL **

- 개별 사진 보기 : /photos/<사진 ID="">/
- 사진에 좋아요 누르기 : /photos/<사진 ID="">/like/
- 사진에 댓글 달기 : /photos/<사진 ID="">/comment/ 
  - 사진에 달린 댓글 가져오기 : /photos/<사진 ID="">/get_comments/
  - 사진에 달린 댓글 지우기 : /photos/<사진 ID="">/comment/<댓글 ID="">/delete/
- 사진에 태그 달기 : /photos/<사진 ID="">/tag/
***
  이렇게 URL에 직접 만들어 줄 수 있음.하지만 2.0이후로는 그렇게 사용하지 않음
  규칙을 따라 URL 작성.
  페이지 구성도가 중요함. 시작하기전에 먼저 잘 만들어놔야 나중에 헷갈리지 않음.





#2.기획하기.

***
**virtualenv 사용하기.**

`` 
python -m venv myvenv
``

``
 myvenv\Scripts\activate.bat
``

** django 설치하기**

``
pip install django
``

``
 python -m django --version
``
 (장고버전확인하기.)
 

Postman - REST Client는 HTTP 기반으로 동작하는 API를 편리하게 호출하는 클라이언트(client)입니다.postman은 개발에 용이한 클라이언트 인터페이스를 제공하는 도구.

**python**

들여 쓰기가 규칙 준수.


#3.Photo 앱과 모델 만들기 
***

**1.django Project와App**

python package는 python module을 묶어놓은 단위 
반드시 초기화 모듈인  __init__.py  가 필요.
djago는 Django Project단위로 만듬.

** Pystargram프로젝트로 만든다는 건Pystargram이라는 Python패키지를 만들고, Pystargram에 들어가는 기능은 Python모듈로 만든다는뜻**

``
django-admin startproject pystargram
``


pystagram/

├── manage.py

└── pystagram

        ├── __init__.py

        ├── settings.py

        ├── urls.py

        └── wsgi.py

프로젝트 서버가 구동되는지 확인하기.

``
python manage.py runserver
``

**데이터베이스와 동기화하기.**

``python manage.py migrate
``

``python manage.py createsuperuser
``
**최고 권한 이용자 만들기**

이렇게 수행한 데이터베이스 작업은 db.sqlite3에 저장.

##Django App 초기화.##

``
python manage.py startapp photos
``


photos packge가 Django App이다.  

admin.py는 관리자 영역에서 App을 다루는 코드를 담는 모듈이다.

models.py는 모델을 정의하는 모듈로서 모델은 데이터를 구성하는 항목자체(field)와 데이터를 다루는 행위를 포함 객체로 표현한다.

views.py는 특정주소에 접근하면 화면에 내용을 표시하는 Python함수를 호출하는 내용을 담고 있다.

MVC패턴에서는view가 표현물  Django에서는 Temlpate이 표현물
 Django에서 view는 데이터(model) 를 표현(Template) 하는 연결자이자 안내자 MVC패턴으로 보면 Controller와 유사하다. 


models.py를 고쳐보자.

class Photo(models.Model):

        image = models.ImageField()

        filtered_image = models.ImageField()

        content = models.TextField(max_length=500)
    
        created_at = models.DateTimeField(auto_now_add=True)

**데이터베이스에 반영(migration)**

setting.py INSTALLED_APPS 에 적용후.

``
python manage.py makemigration
``
에러가 나온다.

image와 filtered_image 모델 필드는 ImageField인데 처리하는 도구가 필요함.

``
pip install pillow
``
라는 도구가 필요 

한후에 다시 
``python mange.py makemigrations
``

``
python manage.py migrate
``

하면 0001_initial.py에 저장후 실제로 반영.















