file=open("sample.txt","r");
file.close();
try:
    content=file.read();
    print(content);
except ValueError as e:
    print("Error:",e);