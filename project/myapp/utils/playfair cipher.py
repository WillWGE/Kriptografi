#playfair cipher

#fungsi untuk menghilangkan spasi/whitespace dalam string
def editPesan(text):
    text=text.replace(" ","")
    text=text.upper()
    return text

#fungsi untuk menyisipkan x jika ada pasangan huruf yang sama
def fillX(text):
    panjang=len(text)
    #jika panjang text genap
    if (panjang%2==0):
        for i in range(0,panjang,2):
            if text[i]==text[i+1]:
                kalimat_baru=text[0:i+1] + str("X")+text[i+1:] #menambahkan huruf x setelah huruf pertama jika 2 huruf sama
                kalimat_baru=fillX(kalimat_baru)
                break
            else:
                kalimat_baru=text
    else: #jika panjang text ganjil
        for i in range(0,panjang-1,2):
            if text[i]==text[i+1]:
                kalimat_baru=text[0:i+1] +str("X") +text[i+1:]
                kalimat_baru=fillX(kalimat_baru) #rekursif
                break
            else:
                kalimat_baru=text
    return kalimat_baru

#fungsi untuk membuat matrix 5x5
def createMatrix(kunci):
    kunci=editPesan(kunci)
    matrix=[[0 for i in range(5)] for j in range(5)] #membuat kotak matrix 5x5
    matrix_letter_added=[]
    #menambahkan kunci ke matrix
    for huruf in kunci:
        if huruf not in matrix_letter_added:
            matrix_letter_added.append(huruf)
    #menambahkan alphabet sisa ke matrix
    for huruf in range(65,91):
        if huruf==74: #tidak menambahkan huruf J
            continue
        elif chr(huruf) not in matrix_letter_added: #tidak menambahkan huruf yang duplikat
            matrix_letter_added.append(chr(huruf))
    indeks=0
    for i in range(5):
        for j in range(5):
            matrix[i][j]=matrix_letter_added[indeks]
            indeks+=1
    return matrix

def indexOf(huruf,matrix):
    for i in range (5):
        try:
            indeks = matrix[i].index(huruf)
            return (i,indeks)
        except:
            continue

#fungsi playfair cipher
def playfaircipher(kunci,pesan,encrypt=True): #jika true , maka fungsi akan encrypt. Jika false, maka fungsi akan decrypt
    cons=1
    if encrypt==False:
        cons=-1
    matrix=createMatrix(kunci)
    pesan=editPesan(pesan)
    pesan=fillX(pesan)

    encrypted_text=""
    for (l1, l2) in zip(pesan[0::2], pesan[1::2]):
        baris1,kolom1 = indexOf(l1,matrix)
        baris2,kolom2 = indexOf(l2,matrix)

        #aturan 1: dua huruf terdapat pada baris kunci yang sama
        if (baris1==baris2):
            encrypted_text+=matrix[baris1][(kolom1+cons)%5]+matrix[baris2][(kolom2+cons)%5]
        #aturan 2 : dua huruf terdapat pada kolom kunci yang sama
        elif (kolom1==kolom2):
            encrypted_text+=matrix[(baris1+cons)%5][kolom1]+matrix[(baris2+cons)%5][kolom2]
        #aturan 3 :dua huruf pada kolom dan baris yang berbeda
        else:
            encrypted_text+=matrix[baris1][kolom2]+matrix[baris2][kolom1]

    return encrypted_text


if __name__=='__main__':
    # a sample of encryption and decryption
    print ('Encripting')
    print ( playfaircipher('secret', 'my secret message'))
    print ('Decrypting')
    print ( playfaircipher('secret', 'LZECRTCSITCVAHBT', False))