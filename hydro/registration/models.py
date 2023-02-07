from django.db import models

type_of_report_choices =(
    ("1", "Устный доклад"),
    ("2", "Постерный доклад"),
    ("3", "Без доклада"),
)

class Article(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=1000,  blank=True)
    article_name = models.CharField(max_length=1000,  blank=True)
    abstract = models.CharField(max_length=1000,  blank=True)
    type_of_report = models.CharField(max_length=1000, blank=True)
    organisation = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'article'

class Accommodation(models.Model):
    reg_fio = models.CharField(max_length=100)
    pers_num = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    comments = models.CharField(max_length=1000)
    reg_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'accommodation'

