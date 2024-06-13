from django.db import models
import uuid

class Mon(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()

    class Meta:
        db_table = 'mon'

    def __str__(self):
        return self.name
