'''
字符串转化
在python3中字符串有两种形式str和bytes
当类型为bytes的时候必须要指定编码的方式（e.g. utf8, gbk...），表示是按什么编码方式编成存储的二进制
从str到bytes叫编码，b = bytes(s, encoding = 'utf-8')或者b = s.encode('utf-8)
从bytes到str叫解码，s = str(b, encoding = 'utf-8')或者 s = b.decode('utf-8')

其中的关键就是得到bytes的编码方式使用chardet.detect(b)['encoding']来获取

为了避免读写出错，采取一下策略
读取时：
1. 二进制读取
2. 判断编码方式
3. 根据编码方式将其转化为str进行处理

写入时：
1. 规定文件的编码方式
2. 统一使用str写入

reference : https://blog.csdn.net/lyb3b3b/article/details/74993327
'''
import chardet

def to_string(raw):
    if type(raw) == str:
        temp = raw
    elif type(raw) == bytes:
        b_encoding = chardet.detect(raw)['encoding']
        temp = raw.decode(b_encoding)
    else:
        raise ValueError('the first parameter must be str or bytes')
    return temp

def to_bytes(raw, encoding):
    if type(raw) == str:
        temp = raw.encode(encoding)
    elif type(raw) == bytes:
        b_encoding = chardet.detect(raw)['encoding']
        temp = raw.decode(b_encoding).encode(encoding)
    else:
        raise ValueError('the first parameter must be str or bytes')
    return temp



if __name__ == '__main__':
    file_path = 'test.txt'
    f = open(file_path,'rb')
    a = f.readline()

    print(type(a), a)
    print(type(to_string(a)), to_string(a))
    print(type(to_bytes(a,'gbk')) ,to_bytes(a,'gbk'))
