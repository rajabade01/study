import re
import sys

def validate_credit_card_numbers(credit_card_numbers_list):
    TESTER = re.compile(
        r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]"
        r"\d{3}"
        r"(?:-?\d{4}){3}"
        r"$")
    for number in credit_card_numbers_list:
        print("Valid" if TESTER.search(number) else "Invalid")


uid_input = sys.stdin.readlines()
end = (int(uid_input[0]))+1
uid_input = uid_input[0 : end]
del uid_input[0]
response = validate_credit_card_numbers(uid_input)
