#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Mason Au Caesar HW <mau1> , <117319101>
import sys

def caesar_str_enc(plaintext, K):
    global ch
    global ciphertext
    ciphertext = ""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch
    print(ciphertext)
    return ciphertext

def caesar_ch_enc(ch, K):
    if ch==chr(32):
        encch=ch
        return encch
    asciiValue = 0
    asciiValue = ord(ch) - 97
    x=(asciiValue+K)%26
    y=x+97
    encch = chr(y)
    #print(encch)
    # everything needed to map a char to its encoded char with K as the parameter
    # ord function and subtract 97 to get 0-26 value: then do the +K: then add 97 to get the char value
    #print("before end")
    return encch
    

def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
    print (plaintext)
    return plaintext

def caesar_ch_dec (ch, K):
    if ch==chr(32): #checking for spaces and not counting the ascci
        decch=ch
        return decch

    asciiValue = ord(ch) - 97 - K
    x = (asciiValue ) % 26
    y = x + 97
    decch = chr(y)

    #print(decch)
    return decch


#def ():
    #K = sys.argv[1]
    #input_str = sys.argv[2]



    #K = 3
    #print(k)
    #print("professor balls")
    input_str = "this is a test"
    
#print(input_str)
#encstr = caesar_str_enc(input_str, K)
#print(encstr)
#decstr = caesar_str_dec(encstr, K)
#print(decstr)

def test_module():

    K = int(sys.argv[1])
    input_str = sys.argv[2]
    #K=3
    #input_str= "abc"
    caesar_str_enc(input_str, K)
    caesar_str_dec(ciphertext, K)
if __name__ == '__main__':
    test_module()






    #print( caesar_ch_enc(ch,K))
    #print(ord('x')+3)


    #print(text)
    #print(caesar_str_enc(plaintext, K))






# In this case, if you call your file like this:
# >python caear_hw.py 3 "string to be encoded"
# it should first print the above string
# then the encrypted version of it
# and next the decrypted version of it i.e., the original one


# In[ ]:




