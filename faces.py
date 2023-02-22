def convert(string: str):
    string = string.replace(":)" , "\U0001f642")
    string = string.replace(":(", "\U0001f641")
    return string
def main():
    string = str(input())
    return convert(string)
print(main())