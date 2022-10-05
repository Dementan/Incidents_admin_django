from django.db import models
from django.db.models import AutoField


class Messages(models.Model):
    when = models.DateTimeField(verbose_name="Дата происшествия")
    incident_type = models.CharField(max_length=15,verbose_name="Тип происшествия")
    message_sourse = models.CharField(max_length=15,verbose_name="Кто сообщил")
    def __str__(self):
        return self.incident_type

class Solutions(models.Model):
    number = models.IntegerField()
    result = models.CharField(max_length=15,verbose_name="Решение по делу")
    def __str__(self):
        return self.result


class Participants(models.Model):
    name = models.CharField(max_length=20,verbose_name="Участник происшествия")
    address = models.CharField(max_length=30,verbose_name="Адрес участника происшествия")
    criminal_record = models.IntegerField(verbose_name="Количество судимостей участника")
    finger_prints = models.CharField(max_length=5,verbose_name="Наличие в базе отпечатков пальцев")
    status = models.CharField(max_length=15,verbose_name="Статус участника")
    def __str__(self):
        return self.status+self.name


class Responsible_officer(models.Model):
    certificate_number = models.IntegerField(verbose_name="Номер удостоверения")
    rank = models.CharField(max_length=20,verbose_name="Звание")
    full_name = models.CharField(max_length=20,verbose_name="ФИО ответственного лица")
    officer_address = models.CharField(max_length=30,verbose_name="Адрес ответственного лица")
    family_composition = models.CharField(max_length=25,verbose_name="Семейное положение ответственного лица")
    def __str__(self):
        return self.full_name

class Incident_information(models.Model):
    incident_scene = models.TextField(verbose_name="адрес места происшествия")
    description = models.TextField(verbose_name="описание случившегося")
    def __str__(self):
        return self.incident_scene+self.description

class Meta:
    verbose_Messages="Сообщение"
    verbose_Messages_plural = "Сообщения"

    verbose_Solutions = "Решение"
    verbose_Solutions_plural = "Решения"

    verbose_Participants = "Участник"
    verbose_Participants_plural = "Участники"

    verbose_Responsible_officer = "Ответственный сотрудник"
    verbose_Responsible_officer_plural = "Ответственные сотрудники"

    verbose_Incident_information = "Информация по происшествию"
    verbose_Incident_information_plural = "Информация по происшествию"
