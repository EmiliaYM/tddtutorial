from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):

	def Test_root_url_resolves_to_home_page(self):
		found = resolve('/')
		self.asertEqual(found.func, home_page)