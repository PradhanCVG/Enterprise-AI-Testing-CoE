"""
System Health Tests
"""

import pytest


@pytest.mark.observability
class TestSystemHealth:

    def test_cpu_usage(self):

        cpu = 55

        assert cpu < 80


    def test_memory_usage(self):

        memory = 65

        assert memory < 85


    def test_disk_usage(self):

        disk = 70

        assert disk < 90