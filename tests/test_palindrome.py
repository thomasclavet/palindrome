import pytest
from palindrome import is_palindrome


@pytest.mark.parametrize("input,expected", [("Kayak", True), ("343", True), ("Was it a car or a cat I saw?", True)])
def test_is_palindrome_when_word_is_a_palindrome(input, expected):
	assert is_palindrome(input) == expected


@pytest.mark.parametrize("input,expected", [("346", False), ("Random", False), ("This is not a palindrome", False)])
def test_is_palindrome_when_word_is_not_a_palindrome(input, expected):
	assert is_palindrome(input) == expected


def test_is_palindrome_raises_when_word_is_not_a_string():
	with pytest.raises(TypeError) as e:
		is_palindrome(342)
		assert str(e.value) == "input must be a string"