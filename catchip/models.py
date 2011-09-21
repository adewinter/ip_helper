from django.db import models

# Create your models here.

class IPLog(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    ip = models.CharField(max_length=16,null=False,blank=False)
    last_hit = models.DateTimeField(auto_now=True,auto_now_add=True)

    class Meta:
        ordering = ['-last_hit']

    def __unicode__(self):
        return "IP Address info for: %s.  IP: %s - Last Update: %s" % (self.name, self.ip, self.last_hit)
