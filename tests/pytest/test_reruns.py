import random
import pytest

PLATFORM = "Linux"

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns(chromium_page):
  assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
class TestReruns:
  def test_rerun_1(self):
    assert random.choice([True, False])

  def test_rerun_2(self):
    assert random.choice([True, False])