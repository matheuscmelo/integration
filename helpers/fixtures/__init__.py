import pytest
import json
from helpers import get_job_payload

@pytest.fixture
def job_payload():
        return get_job_payload()

