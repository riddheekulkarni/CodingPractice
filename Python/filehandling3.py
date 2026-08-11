filename=input("Enter file name:");
ch=input("Enter charcter to search:");
try:
    file=open(filename,"r");
    content=file.read();
    count=content.count(ch);
    print("The character",ch,"appears",count,"times in the file");
    file.close();
except FileNotFoundError:
    print("File not found");