import pytest
from math_fun_app import Sum, Product

# Test the Sum function

def test_sum():
  assert Sum(3, 5) == 8 # 3 + 5 = 8
  assert Sum(-1, 1) == 0 # -1 + 1 = 0
  assert Sum(0, 0) == 0 # 0 + 0 = 0
  assert Sum(10.5, 4.5) == 15.0 # 10.5 + 4.5 = 15.0

# Test the Product function

def test_product():
  assert Product(3, 5) == 15 # 3 * 5 = 15
  assert Product(-1, 1) == -1 # -1 * 1 = -1
  assert Product(0, 5) == 0 # 0 * 5 = 0
  assert Product(10.5, 4) == 42.0 # 10.5 * 4 = 42.0


# Optional: Adding a test to check non-numeric inputs (if needed)
def test_invalid_inputs():
  with pytest.raises(TypeError):
    Sum("a", 5) # This should raise a TypeError
  with pytest.raises(TypeError):
    Product(5, "b") # This should raise a TypeError