# -*- coding: utf-8 -*-
# author: itimor


def binEncode(list):
    n = 0b0000
    if 'post' in list: n = n | 0b1000
    if 'delete' in list: n = n | 0b0100
    if 'put' in list: n = n | 0b0010
    if 'get' in list: n = n | 0b0001

    x = bin(n).replace('0b','')
    y = '0'*(4 - len(x)) + x
    return y

def binDecode(bin):
    s = []
    if bin[0] == '1': s.append('post')
    if bin[1] == '1': s.append('delete')
    if bin[2] == '1': s.append('put')
    if bin[3] == '1': s.append('get')
    return s

if __name__ == '__main__':
    a = binEncode(['put','get'])
    print(a)
    b = binDecode('1001')
    print(b)