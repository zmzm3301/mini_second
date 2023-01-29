from django.db import models


class Info(models.Model):
   FIRMV_2_32 = 'r1m_v2.32'
   FIRMV_CHOICE = (
      (FIRMV_2_32, 'r1m_v2.32'),
   )

   battery = models.CharField(max_length=30)
   color =  models.CharField(max_length=30, default=0)
   runtime = models.CharField(null=True, max_length=30)
   firmV = models.CharField(choices=FIRMV_CHOICE, max_length=20,default=FIRMV_2_32)

   created_at = models.DateTimeField(auto_now=True)

   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f'[{self.pk}] bat : {self.battery}% / runtime : {self.runtime}ms'



