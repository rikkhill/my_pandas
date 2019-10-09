import pytest

from my_pandas.series import Series


def test_series_builds_from_list():

    my_list = [9, 8, 7, 6, 5]

    series = Series(my_list)

    assert series, "Series is truthy"

    assert series.index == list(range(1, len(my_list) + 1)), "Series index is sequential integers"
    assert series.values == my_list, "Series values are what we put in"


def test_get_series_element_from_subscript():

    my_list = [9, 8, 7, 6, 5]

    series = Series(my_list)

    assert series[2] == 8


def test_get_series_element_from_index():

    my_list = [9, 8, 7, 6, 5]

    series = Series(my_list)

    subselect = series.loc[2]

    assert isinstance(subselect, Series), "Subselection of series is also a series"

    assert subselect.values == [7]
