import tkinter
from tkinter import *
from tkinter import ttk

#Definition of colors 
color1="#333333"
color2="#FFFFFF"
color3="#FFF873"
color8=color3
fundo="#add8e6"

#Window creation
window=Tk()
window.title("TIC TAE TOA")
window.geometry('250x360')
window.configure(bg=fundo)

# Splitting the window into two frames 
frame_up=Frame(window, width=240, height=100, bg=color1, relief="raised")
frame_up.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_down=Frame(window, width=240, height=300, bg=fundo, relief="flat")
frame_down.grid(row=1, column=0, sticky=NW)

#Frame configuration
app_g=Label(frame_up, text="x", height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=color1,fg=color2)
app_g.place(x=25, y=10)
app_g=Label(frame_up, text="Player1", height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=color1,fg=color2)
app_g.place(x=17, y=70)
app_gpoint=Label(frame_up, text="0", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=color1,fg=color2)
app_gpoint.place(x=80, y=20)

app_separete=Label(frame_up, text=":", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=color1,fg=color2)
app_separete.place(x=110, y=20)

app_h=Label(frame_up, text="0", height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=color1,fg=color2)
app_h.place(x=170, y=10)
app_h=Label(frame_up, text="Player2", height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=color1,fg=color2)
app_h.place(x=165, y=80)
app_hpoint=Label(frame_up, text="0", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=color1,fg=color2)
app_hpoint.place(x=130, y=20)

#logica
played_1='x'
played_2='0'

#Pontoacao
point_1=0
point_2=0

#Definicao das listas
tab=[['1', '2', '3'],['4','5', '6'], ['7','8','9']]

#Quem joga primeiro
played='x'
play=''
count=0
count_roands=0
def begin_play():
    but_play.place(x=800, y=350)
    
#Controla o jogo, passa o valor
    def control(k):
        global played
        global count
        global play
        global color
        
        
        #Comparando valor recebido
        if k==str(1):
            #Verificando se a posicao esta vazia ou nao
            if but_0['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3 
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_0['fg']=color
                but_0['text']=played
                tab[0][0]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(2):
            #Verificando se a posicao esta vazia ou nao
            if but_1['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_1['fg']=color
                but_1['text']=played
                tab[0][1]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(3):
            #Verificando se a posicao esta vazia ou nao
            if but_2['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3 
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_2['fg']=color
                but_2['text']=played
                tab[0][2]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='pleyed_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(4):
            #Verificando se a posicao esta vazia ou nao
            if but_3['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_3['fg']=color
                but_3['text']=played
                tab[1][0]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(5):
            #Verificando se a posicao esta vazia ou nao
            if but_4['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_4['fg']=color
                but_4['text']=played
                tab[1][1]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                

        #Comparando valor recebido
        if k==str(6):
            #Verificando se a posicao esta vazia ou nao
            if but_5['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_5['fg']=color
                but_5['text']=played
                tab[1][2]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(7):
            #Verificando se a posicao esta vazia ou nao
            if but_6['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3 
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_6['fg']=color
                but_6['text']=played
                tab[2][0]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
                
        #Comparando valor recebido
        if k==str(8):
            #Verificando se a posicao esta vazia ou nao
            if but_7['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_7['fg']=color
                but_7['text']=played
                tab[2][1]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1         
        #Comparando valor recebido
        if k==str(9):
            #Verificando se a posicao esta vazia ou nao
            if but_8['text']=='':
                #Verificando quem xta a jogar e cor de simbolo 
                if played=='x':
                    color=color1
                if played=='0':
                     color=color3  
                #Definindo a cor do botao e marcar a posicao da table com ovalor do jogador atual
                but_8['fg']=color
                but_8['text']=played
                tab[2][2]=played
                #Verificar quem xta chogar par trocar jogador
                if played=='x':
                    played='0'
                    play='played_1'
                else:
                    played='x'
                    play='played_2'
                #Incremetar o contador pra proxima rodada
                count+=1
                
        if count>=5:
            #linhas
            if tab[0][0] == tab[0][1] == tab[0][2]!="":
                vecendor(played)
            elif tab[1][0] == tab[1][1] == tab[1][2]!="":
                vecendor(played)
            elif tab[2][0] == tab[2][1] == tab[2][2]!="":
                vecendor(played)
                        
            #Colunas
            if tab[0][0] == tab[1][0] == tab[2][0]!="":
                vecendor(played)
            elif tab[0][1] == tab[1][1] == tab[2][1]!="":
                vecendor(played)
            elif tab[0][2] == tab[1][2] == tab[2][2]!="":
                vecendor(played)
                    
            #Diagonais 
            if tab[0][0] == tab[1][1] == tab[2][2]!="":
                vecendor(played)
            elif tab[0][2] == tab[1][1] == tab[2][0]!="":
                vecendor(played)
                        
            #Empate
            if count>=9:
                vecendor("It was tie")    
                                                                                                                                                 
                            
                #Depois que o contador for maior que 5, verifica se houve algum vencedor              
    def vecendor(i):
        global tab
        global point_1
        global point_2
        global count_roands
        global count
        
        
        #Bloqueiando os botoes
        but_0['state']='disable'
        but_1['state']='disable'
        but_2['state']='disable'
        but_3['state']='disable'
        but_4['state']='disable'            
        but_5['state']='disable'
        but_6['state']='disable'
        but_7['state']='disable'
        but_8['state']='disable'
        
        app_win=Label(frame_down, text="", width=17, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=color1,fg=color2)
        app_win.place(x=40, y=219)
        
        if i=="x":
            point_2+=1
            app_win['text']='Pleyed2 won'
            app_hpoint['text']=point_2
        if i =='0':
            point_1+=1
            app_win['text']='Played1 won'
            app_gpoint['text']=point_1
        if i=='It was tie':
            app_win ['text']='It was a tie' 
        
        def start():
            #Limpar botao
            but_0['text']=''
            but_1['text']=''
            but_2['text']=''
            but_3['text']=''
            but_4['text']=''
            but_5['text']=''
            but_6['text']=''
            but_7['text']=''
            but_8['text']=''
            
            but_0['state']='normal'
            but_1['state']='normal'
            but_2['state']='normal'
            but_3['state']='normal'
            but_4['state']='normal'
            but_5['state']='normal'
            but_6['state']='normal'
            but_7['state']='normal'
            but_8['state']='normal'
            
            #Reiniciando a tabela
            tab=[['1', '2', '3'],['4','5', '6'], ['7','8','9']]
            app_win.destroy()
            but_play.destroy()
        but_play=Button(frame_down,command=start, text="Next round", height=1, font=('Ivy 11 bold'), overrelief=RIDGE,bg=fundo,relief='raised', fg=color1)
        but_play.place(x=70, y=187)

        def gameOver():
            but_play.destroy()
            app_win.destroy()
            end_play()
        
        if count_roands>=5:
            end_play()
        else:
            count_roands+=1
            #Reiniciando a tabela 
            tab=[['1', '2', '3'],['4','5', '6'], ['7','8','9']]
            count=0
    def end_play():
        global tab
        global count_roands
        global point_1
        global point_2
        global count
        
        tab=[['1', '2', '3'],['4','5', '6'], ['7','8','9']]
        count_roands=0
        point_1=0
        point_2=0
        count=0
        
        #Bloqueiando os botoes
        but_0['state']='disable'
        but_1['state']='disable'
        but_2['state']='disable'
        but_3['state']='disable'
        but_4['state']='disable'            
        but_5['state']='disable'
        but_6['state']='disable'
        but_7['state']='disable'
        but_8['state']='disable'
        
        app_gameover=Label(frame_down, text="Game Over", width=17, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=color1,fg=color2)
        app_gameover.place(x=25, y=90)
        
        # playAgain
        def playAgain():
           app_gpoint['text']='0'
           app_hpoint['text']='0'
           app_gameover.destroy()
           but_play.destroy()
           
           #Call the function jogo
           begin_play()
        #Button PlayAgain   
        but_play=Button(frame_down,command=playAgain, text="Play Again",  height=1, font=('Ivy 11 bold'), overrelief=RIDGE,bg=fundo,relief='raised', fg=color1)
        but_play.place(x=70, y=187)

           
        



    #Configuracao do frame down 
    #Linhas verticais
    app_=Label(frame_down, text="", height=26, relief='flat', pady=5, anchor='center', font=('Ivy 4 bold'), bg=color1,fg=color1)
    app_.place(x=90, y=15)
    app_=Label(frame_down, text="", height=26, relief='flat', pady=5, anchor='center', font=('Ivy 4 bold'), bg=color1,fg=color1)
    app_.place(x=160, y=15)

    #Linhas horizontais
    app_=Label(frame_down, text="", width=180, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), bg=color1,fg=color1)
    app_.place(x=35, y=64)
    app_=Label(frame_down, text="", width=180, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), bg=color1,fg=color1)
    app_.place(x=35, y=125)

    #Linha 0
    but_0=Button(frame_down, command=lambda:control('1'), text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_0.place(x=40, y=15)
    but_1=Button(frame_down,command=lambda:control('2'), text="", width=3,  height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_1.place(x=100, y=15)
    but_2=Button(frame_down, command=lambda:control('3'), text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_2.place(x=170, y=15)

    #Linha 1
    but_3=Button(frame_down, command=lambda:control('4'), text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_3.place(x=40, y=75)
    but_4=Button(frame_down, command=lambda:control('5'), text="", width=3,  height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_4.place(x=100, y=75)
    but_5=Button(frame_down, command=lambda:control('6'),text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_5.place(x=170, y=75)

    #Linha 2
    but_6=Button(frame_down, command=lambda:control('7'), text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_6.place(x=40, y=135)
    but_7=Button(frame_down, command=lambda:control('8'), text="", width=3,  height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_7.place(x=100, y=135)
    but_8=Button(frame_down, command=lambda:control('9'), text="", width=3, height=1, font=('Ivy 17 bold'), overrelief=RIDGE,bg=fundo,relief='flat', fg=color1)
    but_8.place(x=170, y=135)

#Botaoplay
but_play=Button(frame_down,command=begin_play, text="Play", width=5, height=1, font=('Ivy 11 bold'), overrelief=RIDGE,bg=fundo,relief='raised', fg=color1)
but_play.place(x=100, y=197)


    
    



window.mainloop()



