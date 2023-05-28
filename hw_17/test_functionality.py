import pytest


def setup():
    print('\nStart testing')


@pytest.mark.addtest
def test_add_picture(picture):
    picture.add_painting(1)
    assert picture.copies_number == 2


@pytest.mark.addtest
@pytest.mark.xfail(reason='Failed due to wrong arguments', condition=True)
def test_add_sculpture(sculpture):
    sculpture.add_painting(3)
    assert sculpture.copies_number == 6


@pytest.mark.selltest
@pytest.mark.parametrize(
    "sell_picture, expected_picture", [(1, 0,)], ids=['Was 1 picture, left 0']
)
def test_sell_picture(picture, sell_picture, expected_picture):
    picture.sell_painting(sell_picture)
    assert picture.copies_number == expected_picture


@pytest.mark.skip('Change title functionality is not implemented. ICOM-11111')
def test_change_author(sculpture, monkeypatch):
    monkeypatch.setattr(sculpture, 'title', 'Marfa')
    assert sculpture.title == 'Marfa'


def teardown():
    print('\nEnd testing')
