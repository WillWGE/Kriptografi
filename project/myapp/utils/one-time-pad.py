#one-time-pad-cipher
import random

# fungsi untuk baca file text
def createKey(plain_text,kunci):
    key=[]
    if len(plain_text)==len(kunci):
        return(kunci)
    elif(len(plain_text)<len(kunci)):
        for i in range(len(plain_text)):
            key.append(random.choice(kunci)) #mengisi secara random dari list huruf acak 
    x="".join(key)
    return(x)


#fungsi buat encrypt text
def encrypt(plain_text,kunci):
    kunci=kunci.upper()
    plain_text=plain_text.upper()
    encrypted_text=[]
    for i in range(len(plain_text)):
        x=(ord(plain_text[i])+ord(kunci[i])) % 26
        x+=65
        encrypted_text.append(chr(x))
    return("".join(encrypted_text))

#fungsi buat decrypt text
def decrypt(encrypted_text,kunci):
    kunci=kunci.upper()
    decrypted_text=[]
    for i in range(len(encrypted_text)):
        x=(ord(encrypted_text[i])-ord(kunci[i])) % 26
        x += 65
        decrypted_text.append(chr(x))
    return("".join(decrypted_text))

#membaca file text
kunci_txt=open("C:/Users/hp/Documents/kriptografi/plaintext.txt","r")

kunci_acak=kunci_txt.read()

kunci_txt.close()


pesan=input("Masukkan teks : ")
pesan=pesan.replace(" ","")
key = createKey(pesan, kunci_acak)
print("kunci acak : "+key)
encrypted_text = encrypt(pesan,key)
print("Encrypted text :", encrypted_text)
print("Decrypted Text :",decrypt(encrypted_text,key))  
