from tkinter import *
import time

class LoginAdministracao:

    #----------------------------- JANELA PRINCIPAL QUE EXIBEM O CRONÔMETRO - CRONÔMETRO ----------------------------
    def __init__(self):
        
        self.cont1 = 0
        
        #Variáveis responsáveis por fazer o código se interligar
        self.chavePausaLigada = False
        self.chaveControle = False
        self.chaveControle2 =  False
        self.chaveFinalizar = False
        
        self.janelaCrono = Tk()
        self.janelaCrono.title("Cronômetro Neon-Style")
        self.janelaCrono.iconbitmap("icons/icon.ico")
        
        largura = 400
        altura = 450
        
        largura_screen = self.janelaCrono.winfo_screenwidth()
        altura_screen = self.janelaCrono.winfo_screenheight()
        
        posicaoX = largura_screen / 2 - largura / 2
        posicaoY = altura_screen / 2 - altura / 2
        
        self.janelaCrono.geometry('%dx%d+%d+%d' % (largura, altura, posicaoX, posicaoY))
        
        self.janelaCrono['bg'] = 'black'
        
        #Variáveis responsáveis por dá início a contagem do cronômetro
        self.secOperacao = None
        self.minuOperacao = None
        self.houOperacao = None
        
        self.display = Frame(self.janelaCrono, width=200, height=70, bg='black')
        self.display.place(x=105, y=50)
        
        self.horas = Label(self.display, text='00:', fg='cyan', bg='black', font=('arial',35))
        self.horas.place(x=0, y=0)
        self.minutos = Label(self.display, text='00:', fg='cyan', bg='black', font=('arial',35))
        self.minutos.place(x=70, y=0)
        self.segundos = Label(self.display, text='00', fg='cyan', bg='black', font=('arial',35))
        self.segundos.place(x=140, y=0)      

        self.botIniciarContOper = Button(self.janelaCrono, text='INICIAR', bg='black', fg='white', activebackground='black', activeforeground='cyan', font=('arial', 20, 'bold'), command = lambda: self.iniciarContOper())
        self.botIniciarContOper.place(x=140, y=240)
        self.botIniciarContOper.focus_force()
        self.botIniciarContOper.bind("<Return>", self.teclaEnter)
        
        #Chamando função que fará o botão INICIAR piscar
        self.brilhar_01()
   
        self.janelaCrono.mainloop()
    
    def teclaEnter(self, event):

        self.iniciarContOper()
        
    #Função que fará o botão iniciar piscar
    def brilhar_01(self):
        
        if self.chaveControle == False:
            
            self.cont1 += 1
            div = self.cont1 % 2
            
            def brilho1():
            
                self.botIniciarContOper['fg'] = 'white'
            
            def brilho2():      
            
                self.botIniciarContOper['fg'] = 'cyan'
            
            if div != 0:
                brilho1()
                
            else:
                brilho2()
                
            self.segundos.after(200, self.brilhar_01)
     
       
       
        
    #------------------------------------ INICIANDO CONTAGEM DO TEMPORIZADOR -----------------------------------
    def iniciarContOper(self):

        if self.chaveControle == False:
            
            self.finalizarContOper = Button(self.janelaCrono, text='PARAR', bg='black', fg='red', activebackground='black', activeforeground='red', font=('arial', 18, 'bold'), command=lambda:self.finalizadaContOper())            
            self.finalizarContOper.place(x=90, y=240)
                        
            self.pausarContOper = Button(self.janelaCrono, text='PAUSAR', bg='black', fg='green', activebackground='black', activeforeground='green', font=('arial', 18, 'bold'), command=lambda:self.pausaContOper())
            self.pausarContOper.place(x=210, y=240)
            
            self.chaveControle = True
            self.botIniciarContOper.destroy()
            
            self.brilhar_02()
        
        #--- configurando os segundos para aparecer no label ---
        if self.secOperacao == None:
            self.secOperacao = 0
            self.sC = '00'
            self.mC = '00:'
            self.hC = '00:'
        
        if self.chaveFinalizar == False:
            self.secOperacao = self.secOperacao + 1
            
        if self.secOperacao > 0 and self.secOperacao <10:
            sA = self.secOperacao / 100
            sB = str(sA)
            self.sC = sB[2:]
        else:
            self.sC = str(self.secOperacao)
        if self.secOperacao > 59:
            self.secOperacao = 0
            self.sC = '00'

            #--- configurando os minutos para aparecer no label ---
            if self.minuOperacao == None:
                self.minuOperacao = 0
            
            if self.chaveFinalizar == False:
                self.minuOperacao = self.minuOperacao + 1

            if self.minuOperacao > 0 and self.minuOperacao <10:
                mA = self.minuOperacao / 100
                mB = str(mA)
                self.mC = mB[2:] + ':'
            else:
                self.mC = str(self.minuOperacao) + ':'            

            if self.minuOperacao > 59:
                self.minuOperacao = 0
                self.minuC = '00:'

                #--- configurando a hora do temporizador ---
                if self.houOperacao == None:
                    self.houOperacao = 0
                
                if self.chaveFinalizar == False:
                    self.houOperacao = self.houOperacao + 1

                if self.houOperacao > 0 and self.houOperacao < 10:
                    hA = self.houOperacao / 100
                    hB = str(hA)
                    self.hC = hB[2:] + ':'
                else:
                    hB = str(self.houOperacao) + ':'
        
        #Inserindo os valores do tempo já convertido em STRING nos labels do Cronômetro
        self.segundos['text'] = self.sC
        self.minutos['text'] = self.mC
        self.horas['text'] = self.hC
        
        #Chamando a mesma função a cada 1 segundo
        if self.chaveFinalizar == False:
            self.segundos.after(1000, self.iniciarContOper)

    def brilhar_02(self):
        
        if self.chaveFinalizar == False:
            self.cont1 += 1
            div = self.cont1 % 2
            
            def brilho1():
                self.finalizarContOper['fg'] = 'red'
                self.pausarContOper['fg'] = 'white'
            
            def brilho2():      
                self.finalizarContOper['fg'] = 'white'
                self.pausarContOper['fg'] = 'green'
            if div != 0:
                brilho1()
            else:
                brilho2()
                
            self.segundos.after(300, self.brilhar_02)

    #------------------------------------ PARANDO O TEMPORIZADOR --------------------------
    def finalizadaContOper(self):

        #Se a chave finalizar for igual a TRUE significar que o cronômetro já foi parado
        if self.chavePausaLigada == True:
            
            self.chavePausaLigada = False
            self.retomarContOper.destroy()
        
        self.chaveFinalizar = True
        self.chaveControle2 = False
        
        self.finalizarContOper.destroy()
        self.pausarContOper.destroy()
        
        #se o botão "limpar" for acionado o tempo será zerado reiniciando todo processo novamente
        def limpar():
            
            #Formatando o cronômetro e configurando cores para reuitilização
            self.houOperacao = None
            self.minuOperacao = None
            self.secOperacao = 0
            self.hC = '00:'
            self.mC = '00:'
            self.sC = '00'
            self.horas['text'] = '00:'
            self.minutos['text'] = '00:'
            self.segundos['text'] = '00'
            self.horas['fg'] = 'cyan'
            self.minutos['fg'] = 'cyan'
            self.segundos['fg'] = 'cyan'
            self.limparContOper.destroy()
            
            self.botIniciarContOper = Button(self.janelaCrono, text='INICIAR', bg='black', fg='white', activebackground='black', activeforeground='cyan', font=('arial', 20, 'bold'), command = lambda: self.iniciarContOper())
            self.botIniciarContOper.place(x=140, y=240)
            
            self.chaveFinalizar = False
            self.chaveControle = False
            
            #Chamando função que fará o botão "Iniciar" piscar
            self.brilhar_01()
        
        self.limparContOper = Button(self.janelaCrono, text='LIMPAR', bg='black', border=5, fg='white', activebackground='black', activeforeground='cyan', font=('arial', 18, 'bold'), command = limpar)
        self.limparContOper.place(x=145, y=240)
        self.cont = 0
        
        #Chamando função que fará o botão "Limpar" piscar e o cronômetro "Piscar"
        self.brilhar()
        
    #Pisca o temporizador ao terminar contagem
    def brilhar(self):
        
        self.cont += 1
        div = self.cont % 2

        def brilho1():
            
            self.horas['fg'] = 'white'
            self.minutos['fg'] = 'white'
            self.segundos['fg'] = 'white'
            self.limparContOper['fg'] = 'cyan'
            
            self.display['width'] = 230
            self.horas['font'] = 'arial',45
            self.minutos['font'] = 'arial',45
            self.segundos['font'] = 'arial',45
            self.horas.place(x=0, y=0)
            self.minutos.place(x=80, y=0)
            self.segundos.place(x=160, y=0)
            self.display.place(x=90 , y=50)
            
        def brilho2():
            
            self.horas['fg'] = 'cyan'
            self.minutos['fg'] = 'cyan'
            self.segundos['fg'] = 'cyan'     
            self.limparContOper['fg'] = 'white'
        
        #Se a chave finalizar for igual a TRUE significa que o cronômetro já foi finalizado
        if div != 0 and self.chaveFinalizar == True and self.chaveControle2 == False:
            brilho1()
            
        elif div == 0 and self.chaveFinalizar == True and self.chaveControle2 == False:
            brilho2()
            
        self.segundos.after(100, self.brilhar)        
    
    #------------------------------------ PAUSANDO O TEMPORIZADOR --------------------------
    def pausaContOper(self):
        
        self.chaveControle2 =  True
        self.chaveFinalizar = True
        
        self.chavePausaLigada = True
        
        self.pausarContOper.destroy()
        
        #Função de despause caso o botão "Retomar" seja acionado
        def retomarContOper():
            
            self.chaveControle2 = False
            self.chaveFinalizar = False 
            self.chavePausaLigada = False
            
            self.iniciarContOper()
            
            self.retomarContOper.destroy()
            
            self.pausarContOper = Button(self.janelaCrono, text='PAUSAR', bg='black', fg='green', activebackground='black', activeforeground='green', font=('arial', 18, 'bold'), command=lambda:self.pausaContOper())
            self.pausarContOper.place(x=210, y=240)            
            
            #Chamando função que fará o botão "Pausar" piscar e o botão "Parar" piscar
            self.brilhar_02()            
            
        self.retomarContOper = Button(self.janelaCrono, text='RETOMAR', bg='black', fg='yellow', activebackground='black', activeforeground='yellow', font=('arial', 18, 'bold'), command = retomarContOper)
        self.retomarContOper.place(x=210, y=240)
        
        #Chamando função que fará o botão "Retomar" piscar e o botão "Parar" piscar
        self.brilhar_03()
        
    def brilhar_03(self):
        
        if self.chavePausaLigada == True:
            
            self.cont1 += 1
            div = self.cont1 % 2
            def brilho1():
                self.finalizarContOper['fg'] = 'red'
                self.retomarContOper['fg'] = 'white'
            def brilho2():      
                self.finalizarContOper['fg'] = 'white'
                self.retomarContOper['fg'] = 'yellow'
            if div != 0:
                brilho1()
            else:
                brilho2()
                
            self.segundos.after(300, self.brilhar_03)

instancia = LoginAdministracao()
