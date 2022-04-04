import urllib.request
from tkinter import *
import webbrowser
import win32comext.shell.shell as shell #Редактор кода скажет что тут ошибка, забей хуй,
import tkinter.ttk as ttk
# прога работает итак, а без этого не будет
# todo :  -------- python -m auto_py_to_exe

class Grip:
    ''' чтобы двигать окно '''
    def __init__ (self, parent, disable=None, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split("+")
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD is not None:
            self.releaseCMD()


def win71etap():
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                         lpParameters='/c ' + "slmgr –rearm")
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                         lpParameters='/c ' + "shutdown /r")

def activation(): #АКТИВЕЙШН ТАЙМ
    if kmsver.get() == 0 :
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")
        # os.system('cmd /k "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"')   ----- ЗАПАСНОЙ ВАРИК
        #os.system('cmd /k "slmgr /skms s8.uk.to"')       я через shell.shellexecuteex сделал потому что нужны права админа
        #os.system('cmd /k "slmgr /ato"')

    if kmsver.get() == 1 :
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")
    if kmsver.get() == 2 :
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")
    if kmsver.get() == 3 :
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c '+ "slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")
    if kmsver.get() == 4 :
        win7step = Toplevel(root) # Там два этапа - до перезагрузки и после, так что так :
        win7step.geometry('480x200')
        win7step.resizable(False,False)
        win7step.title('Активация WIN7')
        win7step.focus()
        win7label = Label(win7step,text = """Активация состоит из 2 этапов :
                                после первого этапа Ваш ПК перезагрузится,
                                вернитесь сюда и продолжайте со вторым этапом""")
        win7label.pack(side="left")

        firststep = Button(win7step,text = 'Первый этап', command = lambda : win71etap())  #костыль, потому что нужен рестарт для Семёры
        secondstep = Button(win7step,text = 'Второй этап', command = lambda : shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato"))
        firststep.pack()
        secondstep.pack()

    if kmsver.get() == 5 :
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")

    if kmsver.get() == 6:
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /skms s8.uk.to")
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                             lpParameters='/c ' + "slmgr /ato")
def initkms():
    kms = Toplevel(root) #Всё про активацию будет на отдельном окошке
    kms.geometry('600x400')
    kms.resizable(False, False)
    kms.title('Активация от Лэпа')
    kms.overrideredirect(True)
    kms.geometry('+200+200')


    can = Canvas(kms)

    can.create_rectangle(0,0,600,40,
                         fill='#5f87ab')



    can.pack(fill=BOTH)
    kmsgrip = Grip(can)
    kmsclose = Button(kms, text='X', font='Comfortaa 10 bold', bg='#5f87ab',borderwidth=0, command=lambda: kms.destroy())
    kmsclose.place(x=575, y=2)
    kms.focus()

    kmstitle =  Label(kms,text = 'Активация Windows', font ='Comfortaa 14 bold', bg ='#5f87ab')
    kmstitle.place(x=4,y=4)

    inff = Label(kms,text = """Все ОС взяты из данной программы
    (но никто не запрещает попробовать на других сборках Винды)""")
    inff.place(x=100, y =45)
    go = Button(kms,text = 'Активировать', command=lambda :activation())
    go.place(y = 240, x = 10)
# я решил что лучше флажком выбрать чем дохуя кнопок, так что
    w10pro = Radiobutton(kms,text = 'Windows 10 Pro', variable = kmsver, value = 0) #kmsver = ось, которую юзер выбрал для активации
    w10home = Radiobutton(kms,text='Windows 10 Home', variable=kmsver, value=1)
    w10ent = Radiobutton(kms,text='Windows 10 Enterprise', variable=kmsver, value=2)
    w10homeone = Radiobutton(kms,text = 'Windows 10 Home для одного языка', variable = kmsver, value = 3)
    w7 = Radiobutton(kms,text = 'Windows 7', variable = kmsver, value = 4)
    w81pro = Radiobutton(kms,text = 'Windows 8.1 Pro', variable = kmsver, value = 5)
    w11 = Radiobutton(kms,text = 'Windows 11', variable = kmsver,value = 6)

    w11.place(x=5,y=80)
    w10pro.place(x = 5,y = 100)
    w10home.place(x = 5, y = 120)
    w10ent.place(x = 5, y = 140)
    w10homeone.place(x = 5, y = 160)
    w7.place(x = 5, y = 180)
    w81pro.place(x=5, y= 200)

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #checkaem inet
        return True
    except:
        return False

def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = '#365673'
    a.geometry('+400+300')
    a.overrideredirect(True)
    Label(a, text="от Лэпа. Версия 0.2.1")\
        .pack(expand=1)
    a.after(1000, lambda: a.destroy())

root = Tk()

kmsver = IntVar()
kmsver.set(0)


more = PhotoImage(file = 'recources/more.png')
w10 = PhotoImage(file = 'recources/win10.png')
w11 = PhotoImage(file = 'recources/win11.png')
w7 = PhotoImage(file = 'recources/win7.png')
s8 = PhotoImage(file = 'recources/ser8.png')
w8 = PhotoImage(file = 'recources/win8.png')
s12 = PhotoImage(file= 'recources/ser12.png')
s16 = PhotoImage(file='recources/ser16.png')
kmsimg = PhotoImage(file='recources/kms.png')
frame = Frame(root)
canvas = Canvas(root)

canvas.create_rectangle(0,0,600,40,
                        fill = '#5f87ab')


canvas.pack(fill=BOTH)

root.geometry('570x400')
root.resizable(False, False)
root.title("Шиндовс манагер от Лэпа")
root.geometry('+200+300')
root.overrideredirect(True)
frame.pack()
btn = Button(image = w10,borderwidth = 0,
             command=lambda: webbrowser.open('https://windows64.net/index.php?do=download&id=702', new=2))
btn2 = Button(image = w11,borderwidth = 0, command=lambda: webbrowser.open(
    'https://windows64.net/415-windows-11-2022-originalnyj-iso-obraz-21h2-ot-microsoft-10022000376.html', new=2))
btn15 = Button(image = w8, borderwidth = 0,command=lambda: webbrowser.open('https://windows64.net/382-windows-81-professional-x64-x32-dlja-slabyh-kompjuterov.html',new=2))

btn3 = Button(image = w7, borderwidth = 0,command =lambda : webbrowser.open('https://windows64.net/213-windows-7-x64-maksimalnaya-s-2020-finalnymi-obnovleniyami.html', new=2))

btns = Button(image = s8, borderwidth = 0,command =lambda : webbrowser.open('https://windows64.net/87-windows-server-2008-sp2-x64-x86-rus-torrent.html', new = 2))

btns2 = Button(image = s12, borderwidth = 0,command=lambda : webbrowser.open('https://windows64.net/51-windows-server-2012-r2-na-russkom.html',new=2))

btns3 = Button(image = s16, borderwidth = 0,command=lambda :webbrowser.open('https://windows64.net/29-windows-server-2016-r2-x64-rus-c-klyuchom.html',new=2))

btndocks = Button(image = more,borderwidth = 0, command = lambda : webbrowser.open('https://github.com/lap-does-things',new = 2))

btnkms = Button(image = kmsimg,borderwidth = 0, command = lambda:initkms())

splash = Label(text = 'Windows Manager', font = 'Comfortaa 14 bold', borderwidth=0,bg = '#5f87ab')
splash.place(x=5,y=4)

closebtn = Button(text = 'X', font = 'Comfortaa 10 bold', borderwidth=0,bg = '#5f87ab', command = lambda : root.destroy())
closebtn.place(x=540,y=2)

btnkms.place(x=460,y=50)
btn3.place(x = 5, y = 50)
btn15.place(x=120, y = 50)
btn.place(x= 235, y=50)
btn2.place(x=350,y=50)

btns.place(x=5,y = 165)
btns2.place(x = 120,y = 165)
btns3.place(x = 235,y=165)

btndocks.place(x = 460, y = 165)

inf = Button(text="Инфо", width=20, command=about)
inf.place(x = 10, y = 350)

style = ttk.Style(root)
root.tk.call('source', 'recources/azure.tcl')
style.theme_use('azure')

#style.configure("Accentbutton", foreground='white')
#.configure("Togglebutton", foreground='white')

grip1 = Grip(canvas)

vercontrol = Label(text='v. 0.2.1', font = 'Comfortaa 14 bold', bg = "#5f87ab", fg = '#afc9e0')
vercontrol.place(x=200,y=2)


root.mainloop()
