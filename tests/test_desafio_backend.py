from desafio_backend import (find_sum_indexes,
                             check_bracket_balance,
                             find_max_profit,
                             find_water_volume)


def test_find_sum_indexes():
    array = [2, 1, 5, 7, 15]
    target = 20
    result = find_sum_indexes(array, target)
    assert result == [2, 4]


def test_find_sum_indexes2():
    array = [2, 1]
    target = 3
    result = find_sum_indexes(array, target)
    assert result == [0, 1]


def test_check_bracket_balance():
    test_string = "jrgjoe(eok{124}kmm)"
    result = check_bracket_balance(test_string)
    assert result == "SIM"

    test_string = "{[([])]}"
    result = check_bracket_balance(test_string)
    assert result == "SIM"

    test_string = "{[(])}"
    result = check_bracket_balance(test_string)
    assert result == "NAO"

    test_string = "{{[([()])]}}"
    result = check_bracket_balance(test_string)
    assert result == "SIM"


def test_find_max_profit():
    input_prices = [7, 1, 5, 3, 6, 4]
    result = find_max_profit(input_prices)
    assert result == 5

    input_prices = [7, 6, 4, 3, 1]
    result = find_max_profit(input_prices)
    assert result == 0

    input_prices = [7, 1, 8, 2, 4, 2, 10]
    result = find_max_profit(input_prices)
    assert result == 9


def test_find_water_volume():
    contour = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = find_water_volume(contour)
    assert result == 6

    contour = [1, 0, 5, 3, 4, 0, 3, 0, 2, 1, 2]
    result = find_water_volume(contour)
    assert result == 8

    contour = [0, 6, 4, 3, 2, 5, 2, 7, 4, 3, 2, 3]
    result = find_water_volume(contour)
    assert result == 15
