##1.pystargram 기획.

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





##2.기획하기.

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


