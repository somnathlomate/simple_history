from django.contrib import admin
from .models import StudentData, Poll, Choice
from simple_history.admin import SimpleHistoryAdmin


class PollHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "name", "status"]
    history_list_display = ["status"]
    search_fields = ['name', 'user__username']


admin.site.register(StudentData, SimpleHistoryAdmin)
admin.site.register(Poll, SimpleHistoryAdmin)
admin.site.register(Choice, SimpleHistoryAdmin)
