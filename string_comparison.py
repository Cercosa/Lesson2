a = "000"
b = "learn"

def string_comparison(a,b):
    if isinstance(a,str) and isinstance(b,str):
        if a == b:
            print("1")
        elif a != b and len(a) > len(b):
            print("2")
        elif a != b and b == "learn":
            print("3")
        else: 
            print("no information")
    else:
        print("0")
        
if __name__=='__main__':        
    string_comparison(a,b)