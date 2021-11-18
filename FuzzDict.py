import itertools
import os

def bruce1():
    if start_num == end_num:
        with open("result.txt", "a+") as f:
            for i in list(itertools.combinations(List, start_num)):
                temp = ""
                for j in i:
                    temp = temp + j
                f.write(temp + '\n')
        with open("result.txt", "r") as f:
            length = len(f.readlines())
        print("[+]已生成%d条字符，请查看result.txt!" % length)
    else:
        if start_num < end_num:
            for i1 in range(start_num, end_num):
                with open("result.txt", "a+") as f:
                    for i in list(itertools.combinations(List, i1)):
                        temp = ""
                        for j in i:
                            temp = temp + j
                        f.write(temp + '\n')
            with open("result.txt", "r") as f:
                length = len(f.readlines())
            print("[+]已生成%d条字符，请查看result.txt!" % length)
        if start_num > end_num:
            print("[-]错误：最小长度大于最大长度!")

def bruce2():
    if start_num == end_num:
        with open("result.txt", "a+") as f:
            for i in itertools.product(List, repeat=start_num):
                temp = ""
                for j in i:
                    temp = temp + j
                f.write(temp + '\n')
        with open("result.txt", "r") as f:
            length = len(f.readlines())
        print("[+]已生成%d条字符，请查看result.txt!" % length)
    else:
        if start_num < end_num:
            for i1 in range(start_num, end_num):
                with open("result.txt", "a+") as f:
                    for i in itertools.product(List, repeat=i1):
                        temp = ""
                        for j in i:
                            temp = temp + j
                        f.write(temp + '\n')
            with open("result.txt", "r") as f:
                length = len(f.readlines())
            print("[+]已生成%d条字符，请查看result.txt!" % length)
        if start_num > end_num:
            print("[-]错误：最小长度大于最大长度!")



if __name__=="__main__":
    print("""
    
    
    Bruce Fuzz               Author:Judas
    
    
    """)
    List = []
    if (not os.path.exists("char.txt")):
        print("[-]错误：字符文件不存在，请在目录下创建char.txt!")
        exit()
    else:
        with open("char.txt", "r") as f:
            chars = f.readlines()
            if chars == [] or chars == ["\n"]:
                print("[-]错误：字符文件char.txt内容为空!")
                exit()
            else:
                for i in chars:
                    List.append(i.strip("\n"))

    if (os.path.exists("result.txt")):
        with open("result.txt", "w")as f:
            f.truncate()

    while (True):
        start_num = input("[+]请输入字典最小长度:")
        if start_num.isdigit():
            start_num = int(start_num)
            if start_num > len(chars):
                print("[-]错误：最小长度大于字符总长度")
            else:
                break
        else:
            print("[-]错误：请输入一个整数!")

    while (True):
        end_num = input("[+]请输入字段最大长度：")
        if end_num.isdigit():
            end_num = int(end_num)
            if end_num > len(chars):
                print("[-]错误：最大长度大于字符总长度")
            else:
                break
        else:
            print("[-]错误：请输入一个整数!")

    while (True):
        print("""[+]请输入生成字典模式：
(1)生成不重复字符字典
(2)生成重复字符字典""")
        mode=input()
        if mode.isdigit():
            mode = int(mode)
            if mode ==1:
                bruce1()
                break
            elif mode ==2:
                bruce2()
                break
            else:
                print("[-]错误：未知模式!")

        else:
            print("[-]错误：请输入一个整数!")