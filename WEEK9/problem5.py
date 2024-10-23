import string

def alphabet_having_maximum_instance(filename):
    alphabet_count={v:0 for v in string.ascii_lowercase}

    with open(filename,'r') as file:
        content=file.read().lower()

    for char in content:
        if char in alphabet_count:
            alphabet_count[char]+=1

    max_count=max(alphabet_count.values())
    max_alphabet=[key for key,value in alphabet_count.items() if value==max_count]

    if max_count==0:
        print("File does not contain any alphabet.")
    else:
        str_max_alphabet=''.join(max_alphabet)
        print(f"Alphabet(s) having maximum instance : {str_max_alphabet} , {max_count} times")
    

alphabet_having_maximum_instance('WEEK9/file_week9_problem5.txt')