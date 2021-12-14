import time

# def mop_floor():
#     print('我要拖地了')
#     time.sleep(1)
#     print('地拖完了')
#
# def heat_up_watrt():
#     print('我要烧水了')
#     time.sleep(6)
#     print('水烧开了')
#
#
# start_time = time.time()
# heat_up_watrt()
# mop_floor()
# end_time = time.time()
# print('总共耗时:{}'.format(end_time-start_time))


# def mop_floor():
#     print('我要拖地了')
#     time.sleep(1)
#     print('地拖完了')
#
# def heat_up_watrt():
#     print('我要烧水了')
#     time.sleep(6)
#     print('水烧开了')
#
# start_time = time.time()
# t1 = threading.Thread(target=heat_up_watrt)
# t2 = threading.Thread(target=mop_floor)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time = time.time()
# print('总共耗时:{}'.format(end_time-start_time))

from multiprocessing import Pool
import time
def test(p):
       print(p)
       time.sleep(3)
if __name__=="__main__":
    pool = Pool(processes=2)
    for i  in range(500):
        '''
         （1）循环遍历，将500个子进程添加到进程池（相对父进程会阻塞）\n'
         （2）每次执行2个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程不阻塞）\n'
        '''
        pool.apply_async(test, args=(i,))   #维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
    print('test')
    pool.close()
    pool.join()
