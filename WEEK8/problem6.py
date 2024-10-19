def find_vowel_with_max_instances(filename):
    vowels="aeiou"
    vowel_count={v:0 for v in vowels}

    with open(filename,'r') as file:
        content=file.read().lower()

    for char in content:
        if char in vowel_count:
            vowel_count[char]+=1

    max_count=max(vowel_count.values())
    max_vowels=[v for v, count in vowel_count.items() if count == max_count]

    if max_count==0:
        print("No vowels found in the file.")
    else:
        string=''.join(max_vowels)
        print(f"Vowel(s) with highest occurrence : {string} , {max_count} times.")


filename='WEEK8/example.txt'
find_vowel_with_max_instances(filename)