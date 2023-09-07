#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    li = dir(hidden)
    for i in range(len(li)):
        if(li[i][0] != '_'):
            print(li[i])
