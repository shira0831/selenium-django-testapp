from django.db import models


class Lancers(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True,default='')
    contributor = models.CharField(max_length=255,blank=True,null=True,default='')
    url = models.URLField(blank=True,null=True,default='')
    url2 = models.URLField(blank=True,null=True,default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lancers'
        verbose_name_plural = 'lancers'
        ordering =  ['-created_at']