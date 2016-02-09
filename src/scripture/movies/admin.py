from django.contrib import admin

from .models import Movie, Script

class ScriptInline(admin.StackedInline):
	model = Script
	extra = 1

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
		( 'Movie', {'fields': ['name', 'cover', 'genre', 'director', 'writer', 'year', 'pub_date']}),
	]
	inlines = [ScriptInline]

admin.site.register(Movie, MovieAdmin)
