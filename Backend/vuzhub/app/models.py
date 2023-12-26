from django.db import models


class universities(models.Model):
    name = models.CharField(max_length=100, blank=False, primary_key=True)

    def __str__(self):
        return self.name


class specialties(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=100, blank=False)
    university = models.ForeignKey(universities, on_delete=models.CASCADE)
    score_22 = models.IntegerField(blank=False)
    score_23 = models.IntegerField(blank=False)
    subjects = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return (f'{self.code} {self.name} - {self.university}')
