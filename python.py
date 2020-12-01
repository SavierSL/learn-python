a = "Xavier San Lorenzo"
print(a[1:3]) #av
print(a[::-1]) #ozneroL naS reivaX
print(a[1:8:2]) #airS
print(a[::2]) #Xve a oez
print(a[2::]) #vier San Lorenzo
print(a[2:]) #vier San Lorenzo
print(a[:2]) #Xa
print(a[:-1]) #Xavier San Lorenz

#changing a char
name = 'Lucy'
last_letters = name[1:] #am
new_name ='S' + last_letters #Sucy
#change the c to z
lu_letters = new_name[:2]
y_letter = name[-1:] 

bae = lu_letters + 'z' + y_letter #Suzy
print(new_name)
print(bae)

#multi of letters
letter = 'a'
print(letter * 10) #aaaaaaaaaa
print('2' + '3') #23

x = 'Hello World'
string = 'this is a string'
print(x.upper()) #all uppercase
print(x.lower()) #all lowercase
print(x.split()) #['Hello', 'World']
print(a.split('i')) #['Xav', 'er San Lorenzo']

print(x + ' ' + string)
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick')) #The fox brown quick
print('The {} {} {}'.format('fox', 'brown', 'quick', 'black')) #The fox brown quick
print('The {2} {1} {0}'.format('fox', 'brown', 'quick')) #The quick brown fox
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) #The quick brown fox

result = 100/777
print(result) #0.1287001287001287
print('This is the result {r:1.4f}'.format(r=result)) #This is the result 0.1287
print('This is the result {r:10.4f}'.format(r=result)) #This is the result     0.1287

name_ko = 'Xavier'
print(f'Hello his name is {name_ko}') #Hello his name is Xavier
print(f'Hello his name is {name_ko} and his friend is {name}') #Hello his name is Xavier and his friend is Lucy

# LIST IN PYTHON or ARRAY IN JAVASCRIPT
my_list = [1,2,3]
my_list_mix = [1,'a',3,4.2,True]
print(len(my_list_mix))
print(my_list[0]) #1
print(my_list[1:]) #[2,3]

another_list = ['four','five']
new_list = my_list + another_list
print(new_list) #[1, 2, 3, 'four', 'five']
new_list[0] = 10
print(new_list)#[10, 2, 3, 'four', 'five']
new_list.append('six')
print(new_list)#[10, 2, 3, 'four', 'five', 'six']






















