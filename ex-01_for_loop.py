
my_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1,11):
    my_array[i] = i
print('my_array = {}'.format(my_array))
print('======================================')

sum = 0
for i in range(11):
    sum += i

print('sum = {}'.format(sum))
print('======================================')

sum = 0
for i in range(1,11):
    sum += i

print('sum = {}'.format(sum))
print('======================================')

# Lists as an iterable

collection = ['hey', 5, 'd']
for x in collection:
    print(x)
print('======================================')

# Loop over Lists of lists

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)