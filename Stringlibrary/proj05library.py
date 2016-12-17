ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

def is_alpha(str):
    lower = 0
    upper = 0
    for c in str:
        if c in ASCII_LOWERCASE:
            lower = True
        elif c in ASCII_UPPERCASE:
            upper = True
    if lower == True and upper == True: return False
    else: return True


