from django.shortcuts import render



# Create your views here.
def generateKey(plain_text,kunci):
    kunci=list(kunci)
    if len(plain_text)==len(kunci):
        return(str(kunci))
    else:
        for i in range(len(plain_text)-len(kunci)):
            kunci.append(kunci[i%len(kunci)])         
    return ("".join(kunci))

#fungsi untuk encrypt plaintext
def vigenere_encrypt(plain_text,kunci):
    plain_text=plain_text.replace(" ","")
    kunci=generateKey(plain_text,kunci)
    kunci=kunci.upper()
    plain_text=plain_text.upper()
    encrypted_text=[]
    for i in range(len(plain_text)):
        x=(ord(plain_text[i])+ord(kunci[i])) % 26
        x+=65
        encrypted_text.append(chr(x))
    a="".join(encrypted_text)
    return a

#fungsi untuk decrypt plaintext
def vigenere_decrypt(encrypted_text,kunci):
    kunci=kunci.upper()
    decrypted_text=[]
    for i in range(len(encrypted_text)):
        x=(ord(encrypted_text[i])-ord(kunci[i])) % 26
        x += 65
        decrypted_text.append(chr(x))
    b="".join(decrypted_text)
    return b

def vigenere(request):
    if (request.method=='POST'):
        submit_button=request.POST['submit_button']
        if (submit_button =='encrypt'):
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_enkripsi=vigenere_encrypt(pesan,kunci)
            return render(request,'vigenere.html',{'hasil':hasil_enkripsi})
        else:
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_dekripsi=vigenere_decrypt(pesan,kunci)
            return render(request,'vigenere.html',{'hasil':hasil_dekripsi})
    return render(request,'vigenere.html')

    

def extcipher(request):
    return render(request,'extcipher.html')

def playfair(request):
    return render(request,'playfair.html')

def otpcipher(request):
    return render(request,'otpcipher.html')










