"""
from django.db import models

class Info(models.Model):
   battery = models.CharField(max_length=30)
   color =  models.CharField(max_length=30)
   runtime = models.CharField(null=True, max_length=30)

   created_at = models.DateTimeField(auto_now=True)

   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f'[{self.pk}] bat : {self.battery}% / runtime : {self.runtime}ms'



# Create your models here.
"""


'''
def createform(request):
   std = Info()
   std.battery = request.GET['battery']
   std.color = request.GET['color']
   std.runtime = request.GET['runtime']
   std.save()

   return redirect('/#about')
'''