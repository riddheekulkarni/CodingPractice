file=open("sample.txt","r");
print("File name:",file.name);
print("File mode:",file.mode);
print("File closed:",file.closed);
file.close();
print("File closed after closing:",file.closed);