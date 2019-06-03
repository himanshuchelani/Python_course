def vowel_count(s):
    count=0
    vowel=['a','e','i','o','u']
    for i in s:
        if i in vowel:
            count+=1
    print(count)
s="vowel couny"
vowel_count(s)