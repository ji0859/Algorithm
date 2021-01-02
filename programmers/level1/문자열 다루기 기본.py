def solution(s):
    if len(s) % 4 == 0 or len(s) % 6 == 0:
        if s.isnumeric() == True:
            return True
    return False
