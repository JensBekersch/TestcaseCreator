"""Test Dashboard App Configuration."""
from dashboard.apps import DashboardConfig


class TestDashboardApp(object):
    """Test Dashboard App Module Configuration."""

    def test_if_module_name_is_defined(self):
        """Test if attribute name exists in config class."""
        assert hasattr(DashboardConfig, 'name')
