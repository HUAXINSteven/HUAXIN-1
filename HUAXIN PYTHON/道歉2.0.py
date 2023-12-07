import os

os.system('shutdown /s /t 360')
a = input('知道错了没？给你六分钟时间思考:(请回答 我知道错了)')

b = ('我知道错了')
if a == b:
    os.system('shutdown/a')
    print('这还差不多，原谅你一次!')
else:
    c = input('请你再思考一下:')
    if c == b:
        os.system('shutdown/a')
        print('这还差不多，原谅你一次!')
    else:
        d = input('最后一次机会:')
        if d == b:
            os.system('shutdown/a')
            print('勉强原谅你一次!')
        else:
            os.system('shutdown /s /t 0')
