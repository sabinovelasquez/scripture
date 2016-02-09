from django.conf.urls import url, include
from django.contrib import admin
from movies.models import Movie, Script
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script

class MovieSerializer(serializers.ModelSerializer):
    sequences = ScriptSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('name', 'director', 'writer', 'year', 'cover', 'sequences')
        
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


router = routers.DefaultRouter()
router.register(r'scripts', MovieViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^movies/', include('movies.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)