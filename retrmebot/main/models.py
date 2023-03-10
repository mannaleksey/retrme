from django.db import models


class DataCase(models.Model):
    person = models.CharField('Id', max_length=64, default='', primary_key=True)
    response = models.TextField('Ответ retrme', default='')

    def __str__(self):
        return f'{self.person} - {self.response}'

    class Meta:
        verbose_name = "Бд"
        verbose_name_plural = "Бд"
