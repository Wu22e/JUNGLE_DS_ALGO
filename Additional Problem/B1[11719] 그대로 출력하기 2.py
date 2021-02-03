while True:
    try:
        print(input()) # 왜 rstrip넣으면 틀렷다고 하지?
    except EOFError:
        break