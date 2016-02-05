from django.contrib import admin

from .models import Movie, Script

class ScriptInline(admin.StackedInline):
	model = Script
	extra = 8

	def get_extra (self, request, obj=None, **kwargs):
		if obj:
			return 0
		return self.extra

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
		( 'Movie', {'fields': ['name', 'director', 'writer', 'year', 'pub_date']}),
	]
	inlines = [ScriptInline]

admin.site.register(Movie, MovieAdmin)
