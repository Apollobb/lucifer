# -*- coding: utf-8 -*-
# author: itimor


def binEncode(str):
    n = 0b0000
    lst = str.split(',')
    if 'post' in lst: n = n | 0b1000
    if 'delete' in lst: n = n | 0b0100
    if 'put' in lst: n = n | 0b0010
    if 'get' in lst: n = n | 0b0001

    x = bin(n).replace('0b','')
    y = d = '0'*(4 - len(x)) + x
    return y

a = binEncode('put,get')
print(a)

def binDecode(bin):
    s = []
    if bin[0] == '1': s.append('post')
    if bin[1] == '1': s.append('delete')
    if bin[2] == '1': s.append('put')
    if bin[3] == '1': s.append('get')
    return s

b = binDecode('1001')
print(b)