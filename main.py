from functions import print_string, process_data_v2, process_data, validate_string_length, print_data, print_number, \
    calculate_square_root, safe_division, divide_numbers, get_element_from_list, return_positive, convert_to_int


def main():
    # 1
    return_positive(-1)
    divide_numbers(1, 0)

    # 2
    convert_to_int("abc")

    # 3
    get_element_from_list([1, 2, 3], 4)

    # 4
    calculate_square_root(-1)
    safe_division(1, 0)
    validate_string_length("abc", 2)

    # 5
    process_data((1, 2, 3))

    # 7
    process_data_v2((1, 2, 3))

    # 8
    print_string("Hello, world!")
    print_number(42)
    print_data([1, 2, 3])


if __name__ == "__main__":
    main()