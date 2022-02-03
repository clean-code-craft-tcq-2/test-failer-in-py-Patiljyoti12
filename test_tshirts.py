import tshirts

def validate_tshirt_size(passed_size_value,expected_size):
    result=tshirts.size(passed_size_value)
    assert (result==expected_size)
    


if __name__ == '__main__':
    validate_tshirt_size(37,'S')
    validate_tshirt_size(38,'M')
    validate_tshirt_size(42,'M')
    validate_tshirt_size(43,'L')
    validate_tshirt_size(45,'XL')
    validate_tshirt_size(100,'Invalid size')

print("All is well (maybe!)\n")
