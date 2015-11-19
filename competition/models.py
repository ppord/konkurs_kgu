from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'Имя')
    surname = models.CharField(max_length = 20, verbose_name = 'Фамилия')
    email = models.EmailField(verbose_name = 'E-mail')

    def __str__(self):
        return '{name} {surname}'.format(name = self.name, surname = self.surname)


class TextIdea(models.Model):
    date = models.DateTimeField(auto_now = True)
    text = models.TextField(default = '')
    author = models.ForeignKey(Author)
    rating = models.FloatField(default = 0)

    def __str__(self):
        return '{author} {date}'.format(author = self.author, date = self.date)


class DesignIdea(models.Model):
    author = models.ForeignKey(Author)
    rating = models.FloatField(default = 0)
    date = models.DateTimeField(auto_now = True)


class Picture(models.Model):
    img = models.ImageField()
    idea = models.ForeignKey(DesignIdea)



