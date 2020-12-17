# class Keyboard
class Keyboard:
    #Initializing Variables

    def __init__(self):
	    self.char= ["1.","11.","111.",
	           "2.", "22.", "222.", 
	           "3.", "33.", "333.", 
	           "4.", "44.", "444.", 
	           "5.", "55.", "555.", 
	           "6.", "66.", "666.", 
	           "7.", "77.", "777.",  
	           "8.", "88.", "888.", 
	           "9.", "99.", "999." ]

	    self.arr=[['A','B','C'],
	         ['D','E','F'],
	         ['G','H','I'],
	         ['J','K','L'],
	         ['M','N','O'],
	         ['P','Q','R'],
	         ['S','T','U'],
	         ['W','X','Y'],
	         ['Z']]


    #Function to convert Text to Numbers
    def TxtToNum(self, inputs): 
        n = len(inputs)
        output = "" 
        for i in range(n):      
            if(inputs[i] == ' '): 
                output = output + "10."
            else:
                if(inputs[i].islower()):
                    position = (ord(inputs[i])-32) - ord('A')
                    output = output + self.char[position]
                else:
                    position = (ord(inputs[i])) - ord('A')
                    output = output + self.char[position]
            if(i!=n-1):
                if((inputs[i].isupper() and inputs[i+1].islower()) or ((inputs[i].islower() and inputs[i+1].isupper()))):
                    output+="#."
        output=list(output)
        return output[0:len(output)-1]

    #Function to Convert Number to Text
    def NumToText(self,inputs):
        n=inputs.split(".")
        output=""
        count=0
        flag=1
        for i in range(len(n)-1):
            count=len(n[i])-1
            if(n[i]=='#'):
                flag=not flag
                continue
            x=int(n[i][0])-1
            if(flag==0):
                output+=chr(ord(self.arr[x][count])+32)
            else:
                output=output+self.arr[x][count]
        return output

    #function to turn on/off Game Mode
    def Game(self,inputs):
        while True:
            print("If you want to exit press '###' or click any Key to continue: ")
            z=input()
            if(z=="###"):
                break
            inputs=input("Enter the input: ")
            n=list(inputs[:])
            print(n)
            output=""
            c=0
            for i in range(0, len(n)): 
                n[i] = int(n[i])
            for i in range(len(n)):
                if(i!=0 and(n[i]==n[i-1])):
                    output+="error"+" "
                elif(n[i]==2):
                    output+="Up"+" "
                elif(n[i]==4):
                    output+="Left"+" "
                elif(n[i]==6):
                    output+="Right"+" "
                elif(n[i]==8):
                    output+="Down"+" "
                elif(n[i] not in range(2,9,2)):
                    output+="error"+" "
            print(output)
        
        
    
# main 
#Creating and Object of class Keyboard
keyboard = Keyboard()

while True:
    print("\nThis is an Ancient Keyboard: \n1. Text to Number\n2. Number to Text\n3. Game Mode\n4. End")

    choose=int(input("Enter Your Choice: "))
    #Text to Number Function Call
    if(choose==1):
        inputs = input("Enter the Text you want to convert into Number: "); 
        s=(keyboard.TxtToNum( inputs))
        for i in s:
            print(i,end="")

    #Number to Text Function Call        
    elif(choose==2):
        inputs=input("Enter the Number(and end with '.')you want to convert into Text: ")
        result=keyboard.NumToText(inputs)
        print(result)

    # Game Mode Function Call    
    elif(choose==3):
        print("To Start this Game (press '###'): ")
        m=input()
        if(m=="###"):
            keyboard.Game(m)    
    # End of Program Option        
    elif(choose==4):
        print("End of Program!!!")
        break
    # Handlinmg Wrong Choice    
    else:
        print("Wrong Input Enter Again!!")      


            
            

        
            
        

