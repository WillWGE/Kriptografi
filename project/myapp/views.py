from django.shortcuts import render
from .utils import std_vigenere_cipher,playfair_cipher,one_time_pad,extended_vigenere


# # Create your views here.

def vigenere(request):
    if (request.method=='POST'):
        submit_button=request.POST['submit_button']
        if (submit_button =='encrypt'):
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_enkripsi=std_vigenere_cipher.vigenere_encrypt(pesan,kunci)
            return render(request,'vigenere.html',{'hasil':hasil_enkripsi})
        else:
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_dekripsi=std_vigenere_cipher.vigenere_decrypt(pesan,kunci)
            return render(request,'vigenere.html',{'hasil':hasil_dekripsi})
    return render(request,'vigenere.html')

def extcipher(request):
    pass


def playfair(request):
    if(request.method=='POST'):
        submit_button=request.POST['submit_button']
        if(submit_button=='encrypt'):
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_enkripsi=playfair_cipher.playfaircipher(kunci,pesan,True)
            return render(request,'extcipher.html',{'hasil':hasil_enkripsi})
        else:
            pesan=request.POST['pesan']
            kunci=request.POST['kunci']
            hasil_dekripsi=playfair_cipher.playfaircipher(kunci,pesan,False)
            return render(request,'extcipher.html',{'hasil':hasil_dekripsi})
    return render(request,'playfair.html')

def otpcipher(request):
    return render(request,'otpcipher.html')










