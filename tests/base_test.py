import pytest

@pytest.mark.usefixtures("driver", "log_on_failure")
class BaseTest:
    pass