from django.contrib import admin

from .models import Movie, Script

class ScriptInline(admin.StackedInline):
	model = Script
	extra = 1

	def get_extra (self, request, obj=None, **kwargs):
		if obj:
			return 7
		return self.extra

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
		( 'Movie', {'fields': ['name', 'cover', 'director', 'writer', 'year', 'pub_date']}),
	]
	inlines = [ScriptInline]

admin.site.register(Movie, MovieAdmin)
