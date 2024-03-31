# def my_gen():
#    for i in range(10):
#       yield i
# gen = my_gen()
# # print(next(gen))
# # print(next(gen))
# for j in gen:
#    print(j)

#Iterator 
list = [1,2,3,4,5]
it = iter(list)
# print(next(it))
for i in it:
    print(i)