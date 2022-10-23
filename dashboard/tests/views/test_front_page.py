"""Test front page url and view elements."""
from django.urls import reverse, resolve

import dashboard.views as views


class TestFrontPage(object):
    """Test front page url and view elements."""

    def test_url(self):
        """Test url exists and works correctly."""
        assert reverse('front_page') == '/'
        assert resolve('/').view_name == 'front_page'

    def test_view_exists(self):
        """test view has correct class attribute."""
        assert hasattr(views, 'front_page')
