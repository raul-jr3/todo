from django.contrib import admin


from .models import Todo

class TodoAdmin(admin.ModelAdmin):
	list_display = ['title', 'created', 'priority']
	list_filter = ['created', 'priority']
	search_fields = ['priority']

admin.site.register(Todo, TodoAdmin)