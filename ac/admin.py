from django.contrib import admin
from ac.models import AakashCenter, Coordinator
from ac.models import Project, TeamMember, Mentor
from ac.models import Contact

admin.site.register(AakashCenter)
admin.site.register(Coordinator)

admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Mentor)

admin.site.register(Contact)

