def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower();
    str2=str2.replace(" ","").lower();

    if len(str1) != len(str2):
        return False;

    for char in str1:
        if str1.count(char)!=str2.count(char):
            return False;
    else:
            return True;

s1=input("Enter 1st string:");
s2=input("Enter 2nd string:");
if is_anagram(s1,s2):
    print("The strings are anagrams.");
else:
    print("The strings are not anagrams.");