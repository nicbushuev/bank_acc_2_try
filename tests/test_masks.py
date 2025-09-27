from src.masks import get_mask_card_number
import pytest


def test_get_mask_card_number():

	assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
	assert get_mask_card_number("9876987698769876") == "9876 98** **** 9876"


	with pytest.raises(ValueError):
		get_mask_card_number("aaaassssddddffff")

	with pytest.raises(ValueError):
		get_mask_card_number("")


