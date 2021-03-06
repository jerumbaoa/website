from django.contrib import admin

from website.models import Project, Team, Group, Benefit, Barrier, Collaborator
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from tagging.models import Tag

class GroupAdmin(admin.ModelAdmin):
    list_display = ('project','name')

class BenefitAdmin(admin.ModelAdmin):
    list_display = ('project','name')

class BarrierAdmin(admin.ModelAdmin):
    list_display = ('project','name')

class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('project','name')



class GroupInline(admin.TabularInline):
    model = Group

class BenefitInline(admin.TabularInline):
    model = Benefit

class BarrierInline(admin.TabularInline):
    model = Barrier

class CollaboratorInline(admin.TabularInline):
    model = Collaborator


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','slug','description','created','rating_likes','public_views','private_views','funding','goal','paypal','created','modified')
    inlines = [
        GroupInline,
        BenefitInline,
        BarrierInline,
        CollaboratorInline,
    ]


class TeamAdmin(admin.ModelAdmin):
    list_display = ('project','user','role','created','modified')




admin.site.unregister(User)
UserAdmin.list_display = ('id','username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Barrier, BarrierAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
