# Starter code
#index Error
try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")


#ZeroDivisonError
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)



#File Not found error
# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  


