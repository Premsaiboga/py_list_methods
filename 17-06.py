
# 1. Reverse the list without using methods 
def reverse_list(a):
   b = []
   for i in a[::-1]:
        b.append(i)
   return b


# 2. Sort the list without using methods.
def sort_ace(a):
    for i in  range (len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
        
print(sort_ace([2,1,4,6,5,3]))

# 3. Remove duplicates in the list without using methods 
def remove_dublicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
    
print(remove_dublicates([1,1,2,2,3,3,4,4,5]))

# 4.1) Print the largest value in every list and concate the list 
# Ex: [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]
def largest_value(a):
    b=[]
    for i in a:
            c=max(i)
            b.append(c)
    return b
    
print(largest_value( [ [2,3,1], [4,5,3], [7,6,8] ]))

# 4.2) Sum of Every list
def sum_list(a):
    b=[]
    for i in a:
            c=sum(i)
            b.append(c)
    return b
    
print(sum_list( [ [2,3,1], [4,5,3], [7,6,8] ]))
