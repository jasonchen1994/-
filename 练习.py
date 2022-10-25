def circulate_print(str, count=0):
    if count == 5:
        return
    for char in str:
        print(char)

    # TODO(You): 请在此完成函数递归调用
    circulate_print(str,count+1)


if __name__ == '__main__':
    str = "Hello,World!"
    circulate_print(str)

if __name__ ==  '__main__';
    str ="hello world"
