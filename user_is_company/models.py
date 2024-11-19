from django.db import models

class User_is_company(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    is_company = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Только для компаний


    def __str__(self):
        return self.user
