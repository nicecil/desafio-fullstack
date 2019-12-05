# ----------------------------Questao 1----------------------------
def find_sum_indexes(array, target):
    for (index_one, first_number) in enumerate(array):
        for (index_two, second_number) in enumerate(array[index_one + 1:]):
            actual_index_two = index_one + index_two + 1
            if first_number + second_number == target:
                return [index_one, actual_index_two]


# ----------------------------Questao 2----------------------------
class NotBalancedException(BaseException):
    pass


def is_open_bracket(input_char):
    accepted_brackets = '{[('
    if input_char in accepted_brackets:
        return True
    return False


def is_close_bracket(input_char):
    accepted_brackets = '}])'
    if input_char in accepted_brackets:
        return True
    return False


def compare_bracket_type(x, y):
    parenthesis = '()'
    curly = '{}'
    square = '[]'
    if x in parenthesis and y in parenthesis:
        return True
    elif x in curly and y in curly:
        return True
    elif x in square and y in square:
        return True
    return False


def check_balance(open_bracket_control_list, compared_char):
    if len(open_bracket_control_list) == 0:
        raise NotBalancedException()
    last_open_bracket = open_bracket_control_list[-1]
    if compare_bracket_type(last_open_bracket, compared_char):
        open_bracket_control_list.pop()
        return
    raise NotBalancedException()


def check_bracket_balance(input_string):
    open_bracket_control_list = []
    try:
        for char in input_string:
            if is_open_bracket(char):
                open_bracket_control_list.append(char)
            if is_close_bracket(char):
                check_balance(open_bracket_control_list, char)
    except NotBalancedException as e:
        return "NAO"
    return "SIM"


# ----------------------------Questao 3----------------------------
def find_max_profit(price_array):
    max_profit = 0

    for (index, buy_price) in enumerate(price_array):
        for sell_price in price_array[index + 1:]:
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
    return max_profit


# ----------------------------Questao 4----------------------------

def check_column_of_water(contour_array, current_index):
    current_altitude = contour_array[current_index]
    left = contour_array[:current_index]
    right = contour_array[current_index + 1:]

    try:
        lowest_between_left_and_right_peak = min(
            [max(left), max(right)])
        column = lowest_between_left_and_right_peak - current_altitude
        return column if column >= 0 else 0
    except Exception as e:
        return 0


def find_water_volume(contour_array):
    water = 0

    for (index, height) in enumerate(contour_array):
        water += check_column_of_water(contour_array, index)
    return water
