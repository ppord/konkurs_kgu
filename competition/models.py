from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'Имя')
    surname = models.CharField(max_length = 20, verbose_name = 'Фамилия')
    email = models.EmailField(verbose_name = 'E-mail')
    rating = models.FloatField()

    def __str__(self):
        return self.name


class TextIdea(models.Model):
    text = models.TextField(default = '')
    author = models.ForeignKey(Author)


class Picture(models.Model):
    img = models.ImageField()
    idea = models.ForeignKey(DesignIdea)


class DesignIdea(models.Model):
    author = models.ForeignKey(Author)
    rating = models.FloatField()

