from django.db import models

class Article(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=1000,  blank=True)
    article_name = models.CharField(max_length=1000,  blank=True)
    abstract = models.CharField(max_length=1000,  blank=True)
    thesis = models.CharField(max_length=1000,  blank=True)

    class Meta:
        managed = False
        db_table = 'article'
