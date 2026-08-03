from api.controllers import Total
from django_mock_queries.query import MockSet, MockModel


def test_SimpleTotal():
    # Arrange
    order = MockSet()
    order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
    order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
    order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
    delivery_fee = 2.5
    # Act
    total = Total.calculate(order, delivery_fee)
    # Assert
    assert total == 18.94


def test_ComplexTotal():
    # Arrange
    order = MockSet()
    order.add(MockModel(quantity=2, item=MockModel(price=3.5)))
    order.add(MockModel(quantity=1, item=MockModel(price=4.5)))
    delivery_fee = 4.0
    # Act
    total = Total.calculate(order, delivery_fee)
    # Assert
    assert total == 16.78


def test_EmptyTotal():
    # Arrange
    order = MockSet()
    delivery_fee = 0
    # Act
    total = Total.calculate(order, delivery_fee)
    # Assert
    assert total == 0
