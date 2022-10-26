from django.db import models
class RegistrationArticle(models.Model):
    reg_id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    article_name = models.CharField(max_length=1000, blank=True, null=True)
    abstract = models.CharField(max_length=1000, blank=True, null=True)
    thesis = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration_article'
