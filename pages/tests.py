# SimpleTestCasxe becasue home page does not rely on database
from django.test import SimpleTestCase

# to test url and view
# the reverse function allows retreving url details through name value
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
