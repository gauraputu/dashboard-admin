from django.db import models

class Sidebar(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='#')
    icon = models.CharField(max_length=100, null=True, blank=True)
    parent_menu = models.ForeignKey('self', related_name='child_menu', null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        db_table = 'sidebar'
