#coding:utf-8
import os

class Tool:
    def __init__(self):
        pass
    def test(self):
        print "Hello World!"
    def getDir(self, flag = "pwd"):
        if flag == "pwd":
            res_path = os.getcwd()
        if flag == "father":
            pwd = os.getcwd()
            res_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        if flag == "grand":
            pwd = os.getcwd()
            res_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
        return res_path

if __name__ == '__main__':
    T = Tool()
    print "Hello World"