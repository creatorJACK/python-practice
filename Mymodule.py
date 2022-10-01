# def topten():
#        n = 1

#        while n <= 10:
#         sq = n*n
#         yield sq
#         n+=1
# values = topten()
# for i in values:
#         print(i)

#Exception Handling
#x = 9
# y = 0
# k = int(input('Enter a number : '))
# print(k)
# try:
#         print('Resource open')
#         print(x/y)
# except Exception as e:
#         print('Hey U can\'t divide a number by zero',e)

# finally:
#         print('Resourse close')
# print('Bye')


#MultiThreading
# from threading import *
# from time import *
# class Hello(Thread):
#         def run(self):
#                 for i in range(5):
#                         print('Hello')
#                         sleep(1)
# class Hi(Thread):
#         def run(self):
#                 for i in range(5):
#                         print('Hi')
#                         sleep(1)

# t1 = Hello()
# t2 = Hi()

# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()
# print('Bye')


#NUMPY
# new_arr = np.array([1,2,3,4,5])
# print(new_arr)


#File Handling
# f = open('abc.txt','a')
# f.write('of ostion')


#Zip Fnction
# names =('jaron','catom','fgind')
# comp=('ammajaan','MS','Google')
# zipped = zip(names,comp)
# for (j,k) in zipped:
#     print(j,k)



