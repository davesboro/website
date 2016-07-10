from django.db import models
from django.core.urlresolvers import reverse


class Potato(models.Model):
    name = models.CharField(max_length=250)
    origin = models.CharField(max_length=500)
    pronounced = models.CharField(max_length=100)
    picture = models.FileField()

    def get_absolute_url(self):
        return reverse('spuds:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.origin + ' - ' + self.name


class Fact(models.Model):
    potato = models.ForeignKey(Potato, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    fact_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.fact_title