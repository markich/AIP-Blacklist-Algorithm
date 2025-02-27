"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
"""
#! /usr/local/bin/python3

import pytest

from models.raw_ratings import RawRating


def test_raw_rating_instantiation_success():
    """
    Verifies that RawRating has correct data types
    """
    new_rating = RawRating('198.20.68.2', 0.005)
    assert isinstance(new_rating.src_address, str)
    assert isinstance(new_rating.total_score, float)


def test_raw_rating_instantiation_failure_without_params():
    """
    Verifies that RawRating instantiation fails without params
    """
    with pytest.raises(TypeError) as e:
        return RawRating()
