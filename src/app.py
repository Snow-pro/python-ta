import sys
import re


def palindrome(s):
    # your code goes here
    t=str(s)
    t=t.upper()
    u=re.sub(r"\s+","",t)
    p=u[::-1]
    if p==u:
        return True
    else:
        return False

def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
