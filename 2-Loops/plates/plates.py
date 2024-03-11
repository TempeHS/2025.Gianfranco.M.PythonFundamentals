def main():
    plate = input("what ur plate mna !!!.>>: ")
    if is_valid(plate):
        print("haha i dmv accept !! good job man")
    else:
        print("you are declined")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


main()
