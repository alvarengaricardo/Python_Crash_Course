from django.db import models

class Topic(models.Model):
    """Disciplina de estudo do usuário - ex: Álgebra Linear"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text

class Entry(models.Model):
    """Especificação de um assunto - ex: Operações com Matrizes"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo, limitado a 50 caracteres"""
        return self.text[:50] + "..."


