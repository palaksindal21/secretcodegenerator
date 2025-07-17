from django.shortcuts import render

def home(request):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain_text = ""
    print(request.POST)
    if request.method == "POST" and request.POST.get('method') == "encode":
        plain_text = request.POST.get('plain_text')
        shift_key = int(request.POST.get('shift_key'))
        cipher_text = "" #empty string which will store the encoded text
        for char in plain_text:
           if char in alphabet:
              position = alphabet.index(char) #position variable will store index number of alphabet
              new_position = (position+shift_key)%26 # new_position variable store the index of alphabet after shifting
              cipher_text += alphabet[new_position] # after shifting letters encoded letters are stored in cipher_text
           else: #else condition for symbols and numbers
              cipher_text += char
        result = cipher_text
        return render(request,"code_generator/index.html",{'result':result})
   
    if request.method == "POST" and request.POST.get('method') == "decode":
       cipher_text = request.POST.get('plain_text')
       shift_key = int(request.POST.get('shift_key'))
       plain_text = "" #empty string which will store the encoded text
       for char in cipher_text:
          if char in alphabet:
             position = alphabet.index(char)
             new_position = (position-shift_key)%26
             plain_text += alphabet[new_position]
          else:
             plain_text += char
    result = plain_text
    return render(request,"code_generator/index.html",{'result':result})


