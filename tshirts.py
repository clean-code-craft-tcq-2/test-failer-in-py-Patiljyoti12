
def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms <= 42:
        return 'M'
    elif cms > 42 and cms < 45:
        return 'L'
    elif cms >= 45 and cms <= 48:
        return 'XL'
    else:
        return "Invalid size"


