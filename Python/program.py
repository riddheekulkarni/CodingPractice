import sys;
if(len(sys.argv)!=3):
    print("Usage: python program.py <num1> <num2>");
else:
    try:
        num1=float(sys.argv[1]);
        num2=float(sys.argv[2]);
        print("Sum:",num1+num2);
    except ValueError:
        print("plz enter valid input.");