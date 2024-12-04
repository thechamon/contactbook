def validate_phone_number(phone):
    return phone.isdigit()

def validate_string(value):
    return all(x.isalpha() or x.isspace() for x in value)
