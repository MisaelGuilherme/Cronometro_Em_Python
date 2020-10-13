from tkinter import *

class LoginAdministracao:

    #------------------------------------ LABELS QUE IMPRIMEM O CRONÔMETRO - CRONÔMETRO ------------------------------------
    def __init__(self):
    
        self.janelaCrono = Tk()
        self.janelaCrono.geometry('500x500+200+100')
        self.janelaCrono['bg'] = 'black'
        
        self.secOperacao = None
        self.minuOperacao = None
        self.houOperacao = None
        
        self.horas = Label(self.janelaCrono, text='00', fg='cyan', bg='black', font=('arial',30), width=2)
        self.horas.place(x=178, y=50)
        self.minutos = Label(self.janelaCrono, text='00', fg='cyan', bg='black', font=('arial',30), width=2)
        self.minutos.place(x=233, y=50)
        self.segundos = Label(self.janelaCrono, text='00', fg='cyan', bg='black', font=('arial',30), width=2)
        self.segundos.place(x=288, y=50)

        self.chaveControle2 = False
        self.chaveFinalizar2 = False


        self.botIniciarContOper = Button(self.janelaCrono, text='INICIAR', bg='cyan', fg='white', font=('arial', 20, 'bold'), command = lambda: self.iniciarContOper())
        self.botIniciarContOper.place(x=195, y=200)
   
        self.janelaCrono.mainloop()    

    #------------------------------------ TEMPORIZADOR -----------------------------------
    def iniciarContOper(self):

        if self.chaveControle2 == False:
            
            self.finalizarContOper = Button(self.janelaCrono, text='FINALIZAR.OS', font=('arial', 12, 'bold'), width=15, command=lambda:self.finalizadaContOper())
            self.finalizarContOper.pack()
            self.chaveControle2 = True
            self.botIniciarContOper.destroy()

        #configurando os segundos para aparecer no label

        if self.secOperacao == None:
            self.secOperacao = 0
            self.sC = '00'
            self.mC = '00'
            self.hC = '00'
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

            #configurando os minutos para aparecer no label
            if self.minuOperacao == None:
                self.minuOperacao = 0
            self.minuOperacao = self.minuOperacao + 1

            if self.minuOperacao > 0 and self.minuOperacao <10:
                mA = self.minuOperacao / 100
                mB = str(mA)
                self.mC = mB[2:]
            else:
                self.mC = str(self.minuOperacao)            

            if self.minuOperacao > 59:
                self.minuOperacao = 0
                self.minuC = '00'

                #configurando a hora do temporizador
                if self.houOperacao == None:
                    self.houOperacao = 0
                self.houOperacao = self.houOperacao + 1

                if self.houOperacao > 0 and self.houOperacao < 10:
                    hA = self.houOperacao / 100
                    hB = str(hA)
                    self.hC = hB[2:]
                else:
                    hB = str(self.houOperacao)

        self.segundos['text'] = self.sC
        self.minutos['text'] = self.mC
        self.horas['text'] = self.hC

        if self.chaveFinalizar2 == False:
            self.segundos.after(1000, self.iniciarContOper)
        else:
            self.finalizarContOper.destroy()

    #------------------------------------ PARAR O TEMPORIZADOR --------------------------
    def finalizadaContOper(self):
        
        self.chaveFinalizar2 = True

instancia = LoginAdministracao()
