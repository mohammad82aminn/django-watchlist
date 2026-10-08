from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MoviesListViewTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="SAMPLE MOVIE",
            year=1987,
            rating="7.5",
            review="A short sample review.",
        )

    def test_movies_list_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_movies_list_view_url_by_name(self):
        response = self.client.get(reverse("movie:list"))
        self.assertEqual(response.status_code, 200)

    def test_movies_list_view_content(self):
        response = self.client.get(reverse("movie:list"))
        self.assertContains(response, self.movie.title)
        self.assertContains(response, self.movie.year)
        self.assertContains(response, str(self.movie.rating))

        