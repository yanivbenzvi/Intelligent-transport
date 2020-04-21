def hexadecimal_converter(convert_type, convert_value):
    """
    :param convert_type: Hexadecimal-> hex to Decimal -> dec
                         Or Decimal -> dec to Hexadecimal -> hex
    :param convert_value: String value Decimal OR Hexadecimal
    :return: Decimal OR Hexadecimal value
    """
    output = ""
    # Hexadecimal to Decimal
    if convert_type == "hex2dec":
        output = str(int(convert_value, 16))

    # Decimal to Hexadecimal
    if convert_type == "dec2hex":
        output = hex(int(convert_value))
    return output


class Hexadecimal:
    pass
