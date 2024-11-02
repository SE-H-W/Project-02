from django.urls import path
from info.views import place_photo
from info.views import addTofav
urlpatterns = [
    path("place/photo", place_photo, name="place_photo"),
    path("api/addToFav/", addTofav, name="addToFav"),
]
