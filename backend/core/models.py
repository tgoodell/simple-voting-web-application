from django.db import models


class Candidate(models.Model):
    CATEGORIES = (
        ('Amatuer', 'Amatuer'),
        ('Professional', 'Professional'),
    )
    title = models.CharField(max_length=120)
    picture = models.FileField()
    author = models.CharField(max_length=120)
    category = models.CharField(choices=CATEGORIES, max_length=12)
    votes = models.PositiveIntegerField()

    def __str_(self):
        return "Photo of {}".format(self.title)
