import time


def __str__(self):
    return self.name

def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'{func}的运行时间为：', end_time - start_time, 's')
        return result
    return wrapper