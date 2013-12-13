from django.contrib import admin
from ac.models import AakashCentre, Coordinator
from ac.models import Project, TeamMember, Mentor
from ac.models import Contact, Faq

admin.site.register(AakashCentre)
admin.site.register(Coordinator)

admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Mentor)

admin.site.register(Contact)
admin.site.register(Faq)

