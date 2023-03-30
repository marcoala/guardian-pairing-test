import pytest

from script import calculate_score, Game


@pytest.mark.parametrize(
    "input,output",
    [
        ("GUARDIAN", 10),
        ("", 0),
        # TODO: add more test cases
    ],
)
def test_calculate_score(input, output):
    assert calculate_score(input) == output


@pytest.mark.parametrize(
    "letter,occurence",
    [
        ("A", 9),
        ("L", 4),
        ("V", 2),
        ("X", 1),
        # TODO: add more test cases
    ],
)
def test_bag(letter, occurence):
    seed = 17
    game = Game(seed)
    assert game.bag.count(letter) == occurence


def test_extract():
    seed = 17
    game = Game(seed)
    expected_extractions = ["U", "T", "N", "R"]
    for letter in expected_extractions:
        assert game.extract() == letter


def test_remaining_letters():
    game = Game()
    assert game.remaining_letters() == 98
    game.extract()
    assert game.remaining_letters() == 97


def test_get_rack():
    seed = 17
    game = Game(seed)
    assert len(game.get_rack(7)) == 7


def test_score():
    game = Game()
    assert game.check_score([letter for letter in "NGUARDIA"]) == 10
