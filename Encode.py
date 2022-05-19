from unittest import result

#Encoding and Decoding a message.
#get a message
message = input("enter a message")
message = message.upper()  #to uppercase
output = ""                #create an empty string to hod output

for letter in message:     #loop trough eah letter in a message
    if letter.isupper():   #if the letter is in the alphabet (a-z)
        value = ord(letter) + 13  #shift the letter up by 13
        letter = chr(value)      #turn the value back into a letter 
        if not letter.isupper():
           value -= 26
           letter = chr(value)
           output+=letter                  #Add a letter to our output string           
           print('output message',output) 

def encode(user):
    output = ""
    char = ''
    count = 1
    for index, Char in enumerate(user):
        if index == 0:
            char = Char 
            continue

        if char == Char:
            count +=1

        else:
            print("added result")
            result += f"{count}{char}"
            count = 1
            print(char ,Char ,output)
  
            return output

        if name == "main":
            print(encode('binary'))


