from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField('포스트 제목', max_length=100)
    content = models.TextField('포스트 내용')
    thumbnail = models.ImageField('썸네일이미지', upload_to='post', blank = True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #cascade는 종속으로 삭제시 연결된 내용 모두 삭제
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f'{self.post.title}의 댓글 ID : {self.id}'