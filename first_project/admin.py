from django.contrib import admin
import models


@admin.register(models.Theory)
class TheoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name',)
    filter_horizontal = ('name', 'text')

