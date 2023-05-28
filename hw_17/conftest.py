import pytest
from hw_13_dynik import Painting, Picture, Sculpture


@pytest.fixture()
def picture():
    print('Create picture')
    yield Picture('Malevich', 'Black Square', 20000000, 1915, 1)


@pytest.fixture()
def sculpture():
    print('Create sculpture')
    yield Sculpture('Michelangelo Buonarroti', 'David', 'Not for sale', 1504, 5)
