from django.db import models
from django.contrib import admin

# Create your models here.

class BetaTester(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    desc  = models.CharField(max_length=250)
    url   = models.URLField(max_length=250, blank=True, null=True)

    def load_from_form(self, form):
        self.email = form.cleaned_data['email']
        self.desc  = form.cleaned_data['desc']
        self.url   = form.cleaned_data['url']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'beta_tester'

class BetaTesterAdmin(admin.ModelAdmin):
    pass

admin.site.register(BetaTester, BetaTesterAdmin)