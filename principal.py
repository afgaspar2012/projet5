# variavel = 5==6
# print (variavel)

# def decrescente(n):
#     if n==0:
#         print ("decolar")
#     else:
#         print (n)
#         decrescente(n-1)
#
# n=10
# decrescente(n)

n=0

def recursivo(m):
    m=m+1
    print(m)
    recursivo(m)

recursivo(n)