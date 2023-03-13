def leiaInt(num=0):
    
    print(f"\nThe int digited was {num}.")
       
     

def leiaFloat(num=0):
    
    print(f"The float digited was {num:.2f}.")
     
     
while(True):
    try:    
        num = int(input("Type an integer: "))
        
    except ValueError:
        print("\nERROR! Invalid integer value\n")
        
    except KeyboardInterrupt:
        print("Gone stack")
        
    else:
        break
    
while(True):
    try:    
        flo = float(input("Type a float number: "))
        
    except ValueError:
        print("\nERROR! Invalid floatv value\n")
        
    except KeyboardInterrupt:
        print("Gone stack")
        
    else:
        break
    
leiaInt(num)
leiaFloat(flo)
