filename=input("Enter file name:");
try:
    file=open(filename,"r");
    content=file.read().lower();
    vowels="aeiou";
    v_count=0;
    c_count=0;
    for ch in content:
        if ch.isalpha():
            if ch in vowels:
                v_count+=1;
            else:
                c_count+=1;
    total=v_count+c_count;
    if total>0:
        v_percentage=(v_count/total)*100;
        c_percentage=(c_count/total)*100;

        print("Vowel percentage:",v_percentage);
        print("Consonant percentage:",c_percentage);
    else:
        print("No alphabetic characters found in the file.");
    file.close();
except FileNotFoundError:
    print("file not found");