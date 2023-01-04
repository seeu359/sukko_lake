from django.contrib import admin

from sukko_lake.models import Application, FakeFeedback, FakeUsers, MainPicture

admin.site.register(MainPicture)
admin.site.register(FakeUsers)


class ApplicationFilter(admin.ModelAdmin):
    list_display = ('client_name', 'id', 'created_at', 'status',)
    list_filter = ('status', )


class FakeFeedbackFilter(admin.ModelAdmin):
    list_display = ('title', 'user_id',)


admin.site.register(FakeFeedback, FakeFeedbackFilter)
admin.site.register(Application, ApplicationFilter)
