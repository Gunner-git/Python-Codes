def oddeven(x,y):
    if(y%2 == 0):
        even.append(x[y])
    else:
        odd.append(x[y])

from tkinter import Tk,simpledialog,messagebox

root = Tk()
root.withdraw()

messagebox.showinfo('Information','this is an encrypter and decrypter software for me and my friends')
a=int(simpledialog.askstring('Q.','PRESS 1 TO ENCRYPT AND 2 TO DECRYPT AND ANY OTHER KEY TO EXIT.'))

x=0
z=0
e=0
p=''

if(a==1):
    c=simpledialog.askstring('','type a word')
    d=[]
    d.extend(c)
    
    even=[]
    odd=[]
    gurnoor=[]

    for y in c:
        oddeven(c,x)
        x+=1

    if len(odd)<len(even):
        odd.append('$')

    while z<len(odd):
        gurnoor.append(odd[z])
        gurnoor.append(even[z])
        z+=1

    while e<len(gurnoor):
        p=p+gurnoor[e]
        e+=1

    messagebox.showinfo('encrypted message',p)


elif(a==2):
    c=simpledialog.askstring('','type a word')
    d=[]
    d.extend(c)
    
    even=[]
    odd=[]
    gurnoor=[]

    for y in c:
        oddeven(c,x)
        x+=1

    while z<len(odd):
        gurnoor.append(odd[z])
        gurnoor.append(even[z])
        z+=1
    
    if(len(gurnoor)%2!=0):
        gurnoor.pop()

    while e<len(gurnoor):
        p=p+gurnoor[e]
        e+=1
    
    messagebox.showinfo('decrypted message',p)

else:
    exit()
