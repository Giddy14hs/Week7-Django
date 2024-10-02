import pytest 
@pytest.fixture
def cake():
  return {"Flavour": "vanilla", "sugar": "medium"}
def test_cake_flavour(cake):
  assert cake["Flavour"] == "vanilla",  "vanilla cake expected!"
  