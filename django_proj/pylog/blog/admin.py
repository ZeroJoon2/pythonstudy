from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'thumbnail']


@admin.register(Comment)
class PoastComment(admin.ModelAdmin):
    pass


'''
@admin.register(Post) 데코레이터와 함께 PostAdmin 클래스를 정의하는 이유는 Django 관리자(admin) 사이트에서 해당 모델(Post)을 관리하기 위함입니다. 이 설정을 통해 Django 관리자 페이지에서 Post 모델의 데이터를 생성, 수정, 삭제할 수 있게 됩니다.

역할과 장점
1. 모델 등록:
@admin.register(Post)는 Django 관리자 페이지에 Post 모델을 등록하여, 이 모델의 데이터를 관리할 수 있도록 합니다.
등록하지 않으면 관리자 페이지에서 Post 모델을 볼 수 없으며, 데이터를 관리할 수 없습니다.

2. 관리자 인터페이스 커스터마이징:
PostAdmin 클래스에서 admin.ModelAdmin을 상속받으면, Post 모델의 관리 인터페이스를 커스터마이징할 수 있습니다.
예를 들어, 목록에서 보여줄 필드 설정, 검색 필드 지정, 필터 기능 추가 등이 가능합니다.

3. 장고 관리자 페이지의 효율적인 사용:
Django는 admin 사이트를 통해 코드 작성 없이 데이터 관리를 제공하므로, 빠르게 데이터를 추가/수정/삭제하는 데 유용합니다.
관리자 페이지에서 Post 모델 데이터를 확인하고 관리할 수 있어, 초기에 데이터베이스 작업을 손쉽게 할 수 있습니다.
'''