from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Horario(models.Model):
    dia_da_semana = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dia_da_semana} {self.hora_inicio}-{self.hora_fim} {self.materia.nome}'
