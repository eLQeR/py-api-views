from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet, GenreDetail, GenreList,
                          CinemaHallViewSet, ActorList, ActorDetail)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("", include(router.urls), name="movies"),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
]


app_name = "cinema"
