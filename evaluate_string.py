def strcheck(str1, sub_str):
    if len(str1) >= 8:
        if any(ele.isupper() for ele in str1):
            if any(char.isdigit() for char in str1):
                if any(not c.isalnum() for c in str1):
                    for i in sub_str:
                        if i not in str1:
                            return True
        return False


str1 = input()
lst1 = ['123', 'qwerty', 'abc']
result = strcheck(str1, lst1)
print(result)

#Thomson, [11.10.21 14:20]
def strcheck(str1, sub_str):
    count=0
    if len(str1) >= 8:
        if any(ele.isupper() for ele in str1):
            if any(char.isdigit() for char in str1):
                if any(not c.isalnum() for c in str1):
                    for i in sub_str:
                        if i in str1:
                            count+=1
                    if count==0:
                        return True
        return False


str1 = input()
lst1 = ['123', 'qwerty', 'abc']
result = strcheck(str1, lst1)
print(result)
