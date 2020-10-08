try:
    # print(b)
    li=[1,2,3,]
    print(li[10])
    a=10/0
    pass
# except NameError as errorinfo:
#     print(errorinfo)
#     pass
# except IndexError as msg:
#     print(msg)
#     pass
except Exception as result:
    print(result)
    pass
#
# except ZeroDivisionError as msg:
#     print(msg)

print('程序初次执行')

def A(s):
    return 10/int(s)
def B(s):
    return A(s)*2
def main():
    # B('0')
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass
main()