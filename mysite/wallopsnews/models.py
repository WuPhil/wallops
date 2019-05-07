from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length = 300)
    article_type = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    article_content = models.TextField()
    author = models.CharField(max_length = 300)
    image_name = models.CharField(max_length = 300)
    def __str__(self):
        return self.article_title
