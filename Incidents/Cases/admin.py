from django.contrib import admin
from .models import Messages
from .models import Solutions
from .models import Participants
from .models import Responsible_officer
from .models import Incident_information

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    pass
def __str__(self):
    return str(self.name)

@admin.register(Solutions)
class SolutionsAdmin(admin.ModelAdmin):
    pass
def __str__(self):
    return str(self.name)

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    pass
def __str__(self):
    return str(self.name)

@admin.register(Responsible_officer)
class Responsible_officerAdmin(admin.ModelAdmin):
    pass
def __str__(self):
    return str(self.name)

@admin.register(Incident_information)
class Incident_informationAdmin(admin.ModelAdmin):
    pass
def __str__(self):
    return str(self.name)

