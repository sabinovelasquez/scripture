from django.contrib import admin

from .models import Movie, Script

class ScriptAdmin(admin.ModelAdmin):
	fieldsets = [
		()
	]

admin.site.register(Movie, ScriptAdmin)