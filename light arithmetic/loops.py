
for i in range (100):
    
    count = i + 1
    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    
    
    elif count % 3 == 0 and count % 5 != 0:
        print('Fizz')
        
    
    elif count % 3 != 0 and count % 5 == 0:
        print('Buzz')
        
    else:
        print(count)