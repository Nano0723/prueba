about ="""
___________________________________________
*Instituto Tecnologico de Costa Rica*
*Computer Engineering*
*Taller de programación *
*
*Milton Villegas Lemus* 
*Segundo Proyecto*
*Juego de SpaceBattle*
*
*Jose Ignacio Masis Rodriguez 2018132727*
*Steven Badilla Soto 2018183391*
*fecha de emision: 1/6/2018*
*Version: 1.0.0*
____________________________________________*
"""

How="""
Objetivo:
-Tu equipo de Busqueda de asteroides se perdio en el espacio!!!
-Para sobrevivir debes destruit los asteroides o pasar por los aros
-Ten cuidado tu energia es limitada
- Selecciona un piloto y un modo de juego
Para mover la nave presiona:
W= Arriba
S= Abajo
D= Derecha
A= Izquierda
Espacio= Disparo
"""

from tkinter import *               
from threading import Thread        
import threading                   
import winsound                     
import os                           
import time                         
from tkinter import messagebox
import random

def cargarImg(nombre):
    ruta=os.path.join('images',nombre)#funcion que carga imagenes
    imagen=PhotoImage(file=ruta)
    return imagen

root=Tk()
root.title("interfaz principal")
root.minsize(800,600)
root.resizable(width=NO,height=NO)


C_root=Canvas(root, width=800,height=600, bg='black')
C_root.place(x=0,y=0)

CE=cargarImg("img5.gif")
C_root.create_image(400,300,image=CE,state=NORMAL)

global Mod
Mod=2
    
def Song1():
    winsound.PlaySound('Song1.wav', winsound.SND_ASYNC)#funcion tomada de ejemplo tkinter brindado por el asistente Santiago Gamboa
    time.sleep(287)# funcion que carga la el sonido
    Song1()
    
def off():
    winsound.PlaySound(None, winsound.SND_ASYNC)    
    
q=Thread(target=Song1,args=())
q.start()

    


def ventana_about():
    root.withdraw()
    info=Toplevel()
    info.title('INFORMACION')
    info.minsize(800,600)
    info.resizable(width=NO, height=NO)
    
    C_info=Canvas(info, width=800,height=600, bg='black')
    C_info.place(x=0,y=0)
    
    CE=cargarImg("img7.gif")
    C_info.create_image(400,300,image=CE,state=NORMAL)
    
    def volver():
        info.destroy()
        root.deiconify()

        
    Btn_volver=Button(C_info,text="volver",command=volver,bg="Grey",fg="blue")
    Btn_volver.place(x=500, y=550)
    
    L_titulo=Label(C_info,text=about,font=('Agency FB',14),bg="grey",  fg='blue')
    L_titulo.place(x=500,y=10)

    root.mainloop()
def empezar_juego():
    nombre = str(E_nombre.get())
    dific= str(E_dif.get())
    if len(list(nombre))==4 and (dific=="1"or dific=="2"or dific=="3"):
        VentanaJuego(nombre,dific)
    else:
        messagebox.showinfo("Error","Tu nombre debe ser de 4 letras y Debes seleccionar una dificultad")

def ventana_como_jugar():
    root.withdraw()
    how=Toplevel()
    how.title('Como Jugar')
    how.minsize(800,600)
    how.resizable(width=NO, height=NO)
    
    C_how=Canvas(how, width=800,height=600, bg='black')
    C_how.place(x=0,y=0)
    
    CE=cargarImg("img8.gif")
    C_how.create_image(400,300,image=CE,state=NORMAL)
    
    def volver():
        how.destroy()
        root.deiconify()

        
    Btn_volver=Button(C_how,text="volver",command=volver,bg="Black",fg="dark red")
    Btn_volver.place(x=500, y=550)
    
    L_titulo=Label(C_how,text=How,font=('Agency FB',14),bg='black',fg='dark red')
    L_titulo.place(x=0,y=10)


    root.mainloop()
    
def ventana_sel():
    root.withdraw()
    how=Toplevel()
    how.title('Seleccion de Jugador')
    how.minsize(800,600)
    how.resizable(width=NO, height=NO)
    
    C_how=Canvas(how, width=800,height=600, bg='black')
    C_how.place(x=0,y=0)
    
    CE=cargarImg("img10.gif")
    C_how.create_image(400,300,image=CE,state=NORMAL)
    
    L_ingresarNombre = Label(C_how,text="Ingrese su nombre:",font=('Agency FB',14),bg='Black',fg='white')
    L_ingresarNombre.place(x=100,y=385)
    E_nombre = Entry(C_how,width=20,font=('Agency FB',14))
    E_nombre.place(x=100,y=410)

    global Pjs,Cont
    Pjs=["Pepe","Luis","Jose","Katy","Cher","Jess","Gene","Elke","Dana","Xion","Nano","Enzo","Zero","Dr.D","Lulu","Lucy","Vivs","Alex","Juan","Nico"]
    Cont=0
    uno=cargarImg("uno.gif")
    dos=cargarImg("dos.gif")
    tres=cargarImg("tres.gif")
    cuatro=cargarImg("cuatro.gif")
    cinco=cargarImg("cinco.gif")
    seis=cargarImg("seis.gif")
    siete=cargarImg("siete.gif")
    ocho=cargarImg("ocho.gif")
    nueve=cargarImg("nueve.gif")
    diez=cargarImg("diez.gif")
    once=cargarImg("once.gif")
    doce=cargarImg("doce.gif")
    trece=cargarImg("trece.gif")
    catorce=cargarImg("cator.gif")
    quince=cargarImg("quince.gif")
    dieciseis=cargarImg("dieciseis.gif")
    diecisiete=cargarImg("diecisiete.gif")
    dieciocho=cargarImg("dieciocho.gif")
    diecinueve=cargarImg("diecinueve.gif")
    veinte=cargarImg("veinte.gif")
    
    def select(Name):
        Pjs=["Pepe","Luis","Jose","Katy","Cher","Jess","Gene","Elke","Dana","Xion","Nano","Enzo","Zero","Dr.D","Lulu","Lucy","Vivs","Alex","Juan","Nico"]
        Jugador=str(E_nombre.get())
        Pjs.remove(Name)
        Pjs.insert(0,Jugador)
        
    Btn_hilos = Button(C_how,image=uno,command=lambda:select("Luis"),fg='white',bg='green')
    Btn_hilos.place(x=92,y=50)
    Btn_hilos = Button(C_how,image=dos,command=lambda:select("Katy"),fg='white',bg='purple')
    Btn_hilos.place(x=477,y=50)
    Btn_hilos = Button(C_how,image=tres,command=lambda:select("Dana"),fg='white',bg='yellow')
    Btn_hilos.place(x=169,y=50)
    Btn_hilos = Button(C_how,image=cuatro,command=lambda:select("Lulu"),fg='white',bg='pink')
    Btn_hilos.place(x=246,y=50)
    Btn_hilos = Button(C_how,image=cinco,command=lambda:select("Elke"),fg='white',bg='red')
    Btn_hilos.place(x=323,y=50)
    Btn_hilos = Button(C_how,image=seis,command=lambda:select("Jose"),fg='white',bg='pink')
    Btn_hilos.place(x=400,y=50)
    Btn_hilos = Button(C_how,image=siete,command=lambda:select("Lucy"),fg='white',bg='light pink')
    Btn_hilos.place(x=554,y=50)
    Btn_hilos = Button(C_how,image=ocho,command=lambda:select("Xion"),fg='white',bg='dark green')
    Btn_hilos.place(x=631,y=50)
    Btn_hilos = Button(C_how,image=nueve,command=lambda:select("Jess"),fg='white',bg='pink')
    Btn_hilos.place(x=92,y=127)
    Btn_hilos = Button(C_how,image=diez,command=lambda:select("Pepe"),fg='white',bg='orange')
    Btn_hilos.place(x=169,y=127)
    Btn_hilos = Button(C_how,image=once,command=lambda:select("Gene"),fg='white',bg='green')
    Btn_hilos.place(x=246,y=127)
    Btn_hilos = Button(C_how,image=doce,command=lambda:select("Nano"),fg='white',bg='dark green')
    Btn_hilos.place(x=323,y=127)
    Btn_hilos = Button(C_how,image=trece,command=lambda:select("Dr.D"),fg='white',bg='dark blue')
    Btn_hilos.place(x=400,y=127)
    Btn_hilos = Button(C_how,image=catorce,command=lambda:select("Vivs"),fg='white',bg='pink')
    Btn_hilos.place(x=477,y=127)
    Btn_hilos = Button(C_how,image=quince,command=lambda:select("Enzo"),fg='white',bg='dark green')
    Btn_hilos.place(x=554,y=127)
    Btn_hilos = Button(C_how,image=dieciseis,command=lambda:select("Nico"),fg='white',bg='yellow')
    Btn_hilos.place(x=631,y=127)
    Btn_hilos = Button(C_how,image=diecisiete,command=lambda:select("Alex"),fg='white',bg='pink')
    Btn_hilos.place(x=477,y=204)
    Btn_hilos = Button(C_how,image=dieciocho,command=lambda:select("Juan"),fg='white',bg='green')
    Btn_hilos.place(x=246,y=204)
    Btn_hilos = Button(C_how,image=diecinueve,command=lambda:select("Zero"),fg='white',bg='purple')
    Btn_hilos.place(x=323,y=204)
    Btn_hilos = Button(C_how,image=veinte,command=lambda:select("Cher"),fg='white',bg='light blue')
    Btn_hilos.place(x=400,y=204)
    
    def volver():
        how.destroy()
        root.deiconify()
        
    Btn_volver=Button(C_how,text="volver",command=volver,bg="Black",fg="white")
    Btn_volver.place(x=500, y=550)
    
    Btn_aste=Button(C_how,text="Destrir Asteroides",command=lambda:start(1),bg="Black",fg="white")
    Btn_aste.place(x=500, y=400)
    
    Btn_aros=Button(C_how,text="Pasa a travez de los aros",command=lambda:start(0),bg="Black",fg="white")
    Btn_aros.place(x=300, y=400)
    def start(Num):
        global Mod
        if Num==1:
            Mod=1
            ventana_juego()
        elif Num==0:
            Mod=0
            ventana_juego()
            
    def ventana_juego():
        how.withdraw()
        juego=Toplevel()
        juego.title('SpaceBattle')
        juego.minsize(1200,800)
        juego.resizable(width=NO, height=NO)

        C_juego=Canvas(juego, width=1200,height=800, bg='black')
        C_juego.place(x=0,y=0)
        
        CE=cargarImg("img12.gif")
        C_juego.create_image(600,400,image=CE,state=NORMAL)

        global Pos_jug,Pos_ast,Pos_mira,X,Y,Num_ast,Pos_energy,N,Energia
        Num_ast=9
        def randx(Num):
            if Num%25==0:
                return Num
            else:
                return randx(random.randint(100,1100))
        def randy(Num):
            if Num%25==0:
                return Num
            else:
                return randy(random.randint(100,600))
        Pos_jug=[600,400]
        Pos_ast=[randx(random.randint(100,1000)),randy(random.randint(25,600))]
        Pos_mira=[775,350]
        Pos_energy=[1200,randy(random.randint(25,600))]
        X=0
        Y=0
        N=4
        Energia=20

        if Mod==1:
            mira=cargarImg("mira.gif")
            nave=cargarImg('img11.gif')
            bala=cargarImg("img13.gif")
            ener=cargarImg("tank.gif")
            ast1=cargarImg("ast1.gif")
            ast2=cargarImg("ast2.gif")
            ast3=cargarImg("ast3.gif")
            ast7=cargarImg("ast4.gif")
            ast4=cargarImg("ast5.gif")
            ast5=cargarImg("ast6.gif")
            ast6=cargarImg("ast7.gif")
            ast8=cargarImg("ast8.gif")
            def creador():
                global Pos_jug,Pos_ast,Pos_mira
                Pos_ast=[randx(random.randint(100,1000)),randy(random.randint(25,600))]
                C_juego.delete("player")
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast1,anchor=NW,tags=("ast1","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast2,anchor=NW,tags=("ast2","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast3,anchor=NW,tags=("ast3","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast7,anchor=NW,tags=("ast4","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast4,anchor=NW,tags=("ast5","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast5,anchor=NW,tags=("ast6","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast6,anchor=NW,tags=("ast7","ast"),state=HIDDEN)
                C_juego.create_image(Pos_ast[0],Pos_ast[1],image=ast6,anchor=NW,tags=("ast8","ast"),state=HIDDEN)
                C_juego.create_image(Pos_jug[0],Pos_jug[1],image=nave,anchor=NW,tags=("player"),state=NORMAL)
                C_juego.create_image(Pos_mira[0],Pos_mira[1],image=mira,anchor=NW,tags=("player"),state=NORMAL)
                L_ast=Label(C_juego,text="Asteroides restantes:"+str(Num_ast),font=('Agency FB',14),bg='black',fg='dark red')
                L_ast.place(x=20,y=20)

            creador()
            def energy():
                global Pos_jug,N,Pos_energy
                if N==0:
                    if Pos_energy[0]>0:
                        if (Pos_energy[0]<=Pos_jug[0] and Pos_energy[0]+50>=Pos_jug[0]) and (Pos_energy[1]<=Pos_jug[1] and Pos_energy[1]+50>=Pos_jug[1]):
                            C_juego.delete("energy")
                            New=[1200,randy(random.randint(25,600))]
                            C_juego.create_image(New[0],New[1],image=ener,anchor=NW,tags=("energy"),state=NORMAL)
                            N=4
                            Pos_energy=New
                            print("yeah")
                            C_juego.update()
                            time.sleep(8)
                            Cont_energy()
                        if (Pos_energy[0]<=Pos_jug[0]+125 and Pos_energy[0]+50>=Pos_jug[0]+125) and (Pos_energy[1]<=Pos_jug[1] and Pos_energy[1]+50>=Pos_jug[1]):
                            C_juego.delete("energy")
                            New=[1200,randy(random.randint(25,600))]
                            C_juego.create_image(New[0],New[1],image=ener,anchor=NW,tags=("energy"),state=NORMAL)
                            N=4
                            Pos_energy=New
                            print("yeah")
                            C_juego.update()
                            time.sleep(8)
                            Cont_energy()
                        if (Pos_energy[0]<=Pos_jug[0]+350 and Pos_energy[0]+50>=Pos_jug[0]+350) and (Pos_energy[1]<=Pos_jug[1] and Pos_energy[1]+50>=Pos_jug[1]):
                            C_juego.delete("energy")
                            New=[1200,randy(random.randint(25,600))]
                            C_juego.create_image(New[0],New[1],image=ener,anchor=NW,tags=("energy"),state=NORMAL)
                            N=4
                            Pos_energy=New
                            print("yeah")
                            C_juego.update()
                            time.sleep(8)
                            Cont_energy()
                        else:
                            C_juego.itemconfig("energy",state=NORMAL)
                            Pos_energy[0]=Pos_energy[0]-25
                            C_juego.move("energy",-25,0)
                            C_juego.update()
                            time.sleep(0.3)
                            energy()
                    elif Pos_energy[0]==0:
                        C_juego.delete("energy")
                        New=[1200,randy(random.randint(25,600))]
                        C_juego.create_image(New[0],New[1],image=ener,anchor=NW,tags=("energy"),state=NORMAL)
                        N=4
                        Pos_energy=New
                        C_juego.update()
                        time.sleep(8)
                        Cont_energy()
                else:
                    Cont_energy()
            def Cont_energy():
                global N
                if N!=0:
                    N=N-1
                    time.sleep(0.7)
                    energy()
                else:
                    pass
                   
            def ast_num():
                global Num_ast
                L_ast.config(text="Asteroides restantes:"+str(Num_ast))


            def ast(Cont1):
                global Cont,Pos_ast,X,Y,Num_ast,Pos_jug,Num_ast,Energia
                
                if Cont<=7:
                    if Cont1==0:
                        C_juego.itemconfig("ast1",state=NORMAL)
                    elif Cont1==1:
                        C_juego.itemconfig("ast1",state=HIDDEN)
                        C_juego.itemconfig("ast2",state=NORMAL)
                        X=45
                        Y=50
                        C_juego.update()
                    elif Cont1==2:
                        C_juego.itemconfig("ast2",state=HIDDEN)
                        C_juego.itemconfig("ast3",state=NORMAL)
                        X=75
                        Y=80
                        C_juego.update()
                    elif Cont1==3:
                        C_juego.itemconfig("ast3",state=HIDDEN)
                        C_juego.itemconfig("ast4",state=NORMAL)
                        X=105
                        Y=110
                        C_juego.update()
                    elif Cont1==4:
                        C_juego.itemconfig("ast4",state=HIDDEN)
                        C_juego.itemconfig("ast5",state=NORMAL)
                        X=125
                        Y=130
                        C_juego.update()
                    elif Cont1==5:
                        C_juego.itemconfig("ast5",state=HIDDEN)
                        C_juego.itemconfig("ast6",state=NORMAL)
                        X=153
                        Y=160
                        C_juego.update()
                    elif Cont1==6:
                        C_juego.itemconfig("ast6",state=HIDDEN)
                        C_juego.itemconfig("ast7",state=NORMAL)
                        X=184
                        Y=190
                        C_juego.update()
                    elif Cont1==7:
                        C_juego.itemconfig("ast7",state=HIDDEN)
                        C_juego.itemconfig("ast8",state=NORMAL)
                        X=213
                        Y=220
                        Num_ast=Num_ast-1
                        if (Pos_ast[0]<=Pos_jug[0] and Pos_ast[0]+X>=Pos_jug[0]) and (Pos_ast[1]<=Pos_jug[1] and Pos_ast[1]+Y>=Pos_jug[1]):
                            C_juego.delete("ast")
                            creador()
                            Energia=Energia-20
                        elif (Pos_ast[0]<=Pos_jug[0]+125 and Pos_ast[0]+X>=Pos_jug[0]+125) and (Pos_ast[1]<=Pos_jug[1] and Pos_ast[1]+Y>=Pos_jug[1]):
                            C_juego.delete("ast")
                            creador()
                            Energia=Energia-20
                        elif (Pos_ast[0]<=Pos_jug[0]+350 and Pos_ast[0]+X>=Pos_jug[0]+350) and (Pos_ast[1]<=Pos_jug[1] and Pos_ast[1]+Y>=Pos_jug[1]):
                            C_juego.delete("ast")
                            creador()
                            Energia=Energia-20
                        else:
                            C_juego.delete("ast")
                            creador()
                        
            
            def disparo():
                global Pos_ast,Pos_mira,Cont,X,Y,Num_ast
                if (Pos_ast[0]<=Pos_mira[0] and Pos_ast[0]+X>=Pos_mira[0]) and (Pos_ast[1]<=Pos_mira[1] and Pos_ast[1]+Y>=Pos_mira[1]):
                    C_juego.create_image(Pos_mira[0],Pos_mira[1],image=bala,anchor=NW,tags=("bala"),state=NORMAL)
                    C_juego.delete("ast")
                    Pos_ast[0]+=2000
                    Pos_ast[1]+=2000
                    time.sleep(0.3)
                    C_juego.delete("bala")
                    Cont=0
                    C_juego.update()
                    
                else:
                    C_juego.itemconfig("bala",state=HIDDEN)
                    C_juego.update()
            def disp(event):
                b=Thread(target=disparo,args=())
                b.start
                disparo()
            
            def start2():
                global Cont
                if Cont<=7:
                    ast(Cont)
                    Cont+=1
                    time.sleep(1)
                    start2()
                elif Cont>7:
                    Cont=0
                    start2()
                    
                
            b=Thread(target=Cont_energy,args=())
            b.start()
            a=Thread(target=start2,args=())
            a.start()
            
        
            def mover(event):
                key = event.char
                global Pos_jug,Pos_mira
                if Pos_jug[0]>=900 or Pos_jug[1]>=700 or Pos_jug[0]<=0 or Pos_jug[1]<=0:
                    if Pos_jug[1]<=0:
                            Pos_jug[1]=Pos_jug[1]+25
                            Pos_mira[1]=Pos_mira[1]+25
                            C_juego.move("player",0,25)
                    elif Pos_jug[0]<=0:
                            Pos_jug[0]=Pos_jug[0]+25
                            Pos_mira[0]=Pos_mira[0]+25
                            C_juego.move("player",25,0)
                    elif Pos_jug[0]>=760:
                            Pos_jug[0]=Pos_jug[0]-25
                            Pos_mira[0]=Pos_mira[0]-25
                            C_juego.move("player",-25,0)
                    elif Pos_jug[1]>=560:
                            Pos_jug[1]=Pos_jug[1]-25
                            Pos_mira[1]=Pos_mira[1]-25
                            C_juego.move("player",0,-25)
                else:
                    if (key == "w")or(key == "W"):
                            Pos_jug[1]=Pos_jug[1]-25
                            Pos_mira[1]=Pos_mira[1]-25
                            C_juego.move("player",0,-25)
                    elif (key == "a")or (key == "A"):
                            Pos_jug[0]=Pos_jug[0]-25
                            Pos_mira[0]=Pos_mira[0]-25
                            C_juego.move("player",-25,0)
                    elif (key == "d") or (key == "D"):
                            Pos_jug[0]=Pos_jug[0]+25
                            Pos_mira[0]=Pos_mira[0]+25
                            C_juego.move("player",25,0)
                    elif (key == "s")or (key == "S"):
                            Pos_jug[1]=Pos_jug[1]+25
                            Pos_mira[1]=Pos_mira[1]+25
                            C_juego.move("player",0,25)
            def volver():
                juego.destroy()
                root.deiconify()    
            
            Btn_volver=Button(C_juego,text="volver",command=volver,bg="Black",fg="white")
            Btn_volver.place(x=10, y=750)
            
                        
            
        juego.bind("<space>",disp)
        juego.bind("<Key>",mover)
        
        root.mainloop()
    root.mainloop()

    
def ventana_pun():
    global Puntuaciones
    root.withdraw()
    pun=Toplevel()
    pun.title('Puntuaciones')
    pun.minsize(800,600)
    pun.resizable(width=NO, height=NO)
    
    C_pun=Canvas(pun, width=800,height=600, bg='black')
    C_pun.place(x=0,y=0)
    
    CE=cargarImg("img9.gif")
    C_pun.create_image(400,300,image=CE,state=NORMAL)
    
    file1=open("VariablePun.txt","r")
    punt=file1.read()
    punt=eval(punt)
    file2=open("nombres.txt","r")
    nom=file2.read()
    nom=eval(nom)
    
    L_Pun=Label(C_pun,text="Mejores Puntuaciones:",font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun.place(x=100,y=10)
    
    L_Pun1=Label(C_pun,text=nom[0]+".........." +str(punt[0]),font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun1.place(x=100,y=60)
    
    L_Pun2=Label(C_pun,text=nom[1]+".........."+ str(punt[1]),font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun2.place(x=100,y=110)
    
    L_Pun3=Label(C_pun,text=nom[2]+".........."+ str(punt[2]),font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun3.place(x=100,y=160)

    L_Pun4=Label(C_pun,text=nom[3]+".........." +str(punt[3]),font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun4.place(x=100,y=210)
    
    L_Pun5=Label(C_pun,text=nom[4]+".........." +str(punt[4]),font=('Agency FB',20),bg="black",  fg='blue')
    L_Pun5.place(x=100,y=260)
    file1.close
    file2.close
    def volver():
        pun.destroy()
        root.deiconify()

        
    Btn_volver=Button(C_pun,text="volver",command=volver,bg="Black",fg="blue")
    Btn_volver.place(x=500, y=550)

    root.mainloop()


Btn_juego = Button(C_root,text='Juego',command=ventana_sel,fg='dark red',bg='black')
Btn_juego.place(x=450,y=300)

Btn_info = Button(C_root,text='Informacion',command=ventana_about,bg='black',fg='dark red')
Btn_info.place(x=200,y=200)

Btn_how = Button(C_root,text='¿Como Jugar?',command=ventana_como_jugar,bg='black',fg='dark red')
Btn_how.place(x=200,y=300)

Btn_pun = Button(C_root,text='Puntuaciones',command=ventana_pun,bg='black',fg='dark red')
Btn_pun.place(x=200,y=400)

root.mainloop()

    
