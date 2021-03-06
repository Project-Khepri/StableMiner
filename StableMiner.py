import sys, os, subprocess
from subprocess import *
from os import path, chdir
from sys import *
from time import *


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print "StableMiner running at location: " + dname

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('StableMiner')
    root.geometry('600x215+372+536')
    set_Tk_var()
    w = New_Toplevel_1 (root)
    iconloc = dname + r"\Dependencies\design.ico"
    root.wm_iconbitmap(iconloc)
    init()
    root.mainloop()

w = None
def create_New_Toplevel_1 (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x215+372+536')
    set_Tk_var()
    w_win = New_Toplevel_1 (w)
    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None


def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global address
    address = StringVar()

    global bar
    bar = IntVar()

    global mininglabel
    mininglabel = StringVar()


def init():
    pass

address = ""
on = 0
count = 0

def clipboard():
    root.clipboard_clear()
    root.clipboard_append('13GGffkBfcf8nbfBE2qxnxgpqXAbjEyehF')


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = 'SystemButtonFace'  # X11 color: #f0f0f0
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana1color = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana2color = 'SystemButtonFace' # X11 color: #f0f0f0
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant  " + \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Courier New} -size 10 -weight normal -slant " + \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(highlightcolor="black")


        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.02,rely=0.05,relheight=0.91,relwidth=0.97)
        self.TNotebook1.configure(width=584)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Start Mining",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="Info",underline="-1",)

        self.TButton1 = ttk.Button (self.TNotebook1_pg0)
        self.TButton1.place(relx=0.4,rely=0.51,height=25,width=116)
        self.TButton1.configure(command=self.start)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Start/Stop Mining''')

        self.Label1 = Label (self.TNotebook1_pg0)
        self.Label1.place(relx=0.02,rely=0.1,height=21,width=91)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(disabledforeground="#b4b4b4")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Bitcoin Address:''')

        self.Entry1 = Entry (self.TNotebook1_pg0)
        self.Entry1.place(relx=0.19,rely=0.11,relheight=0.12,relwidth=0.78)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#b4b4b4")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#d8d8d8")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=address)


        self.TProgressbar1 = ttk.Progressbar (self.TNotebook1_pg0)
        self.TProgressbar1.place(relx=0.78,rely=0.84,relheight=0.13
                ,relwidth=0.21)
        self.TProgressbar1.configure(variable=bar)

        self.TLabel7 = ttk.Label (self.TNotebook1_pg0)
        self.TLabel7.place(relx=-0.19,rely=0.78,height=1,width=794)
        self.TLabel7.configure(background="#000000")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(text='''______________________________________________________________________________________________________________________________________________________________''')

        self.TLabel8 = ttk.Label (self.TNotebook1_pg0)
        self.TLabel8.place(relx=0.02,rely=0.85,height=19,width=436)
        self.TLabel8.configure(background=_bgcolor)
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(textvariable=mininglabel)

        self.TLabel1 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel1.place(relx=0.02,rely=0.06,height=19,width=193)
        self.TLabel1.configure(background=_bgcolor)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Version: Bitcoin x32 Beta + CGMiner''')

        self.TLabel2 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel2.place(relx=0.02,rely=0.18,height=19,width=109)
        self.TLabel2.configure(background=_bgcolor)
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Created: 01/13/2014''')

        self.TLabel3 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel3.place(relx=0.02,rely=0.29,height=19,width=263)
        self.TLabel3.configure(background=_bgcolor)
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''This software was created by Argutus1 on Reddit.''')

        self.TLabel6 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel6.place(relx=0.02,rely=0.88,height=19,width=576)
        self.TLabel6.configure(background=_bgcolor)
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(text='''Bitcoind or qt must be running to use this software. The config file also must have server mode enabled.''')

        self.TButton2 = ttk.Button (self.TNotebook1_pg1)
        self.TButton2.place(relx=0.02,rely=0.42,height=25,width=366)
        self.TButton2.configure(command=clipboard)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Donations may be sent to: 13GGffkBfcf8nbfBE2qxnxgpqXAbjEyehF''')

        self.Label2 = Label (self.TNotebook1_pg1)
        self.Label2.place(relx=0.84,rely=0.04,height=84,width=84)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(disabledforeground="#b4b4b4")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightcolor="black")
        photoloc = dname + r"\Dependencies\address.gif"
        self._img1 = PhotoImage(file=photoloc)
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')

        self.menubar = Menu(master,font=font10,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

    def start(self):
        global on
        global count
        if on == 0:
            location = dname + r"\Dependencies\p2pool\run_p2pool.py"
            global p2pool
            p2pool = subprocess.Popen([sys.executable,location])
            address = self.Entry1.get()
            print address
            batfile = dname + "\Dependencies\cgminer\cgminer.exe --url http://192.168.1.217:9332/ --userpass " + address + ":123"
            batfile = batfile.replace(" :", " anyusername:") #If a bitcoin address is not given, it is replaced by 'anyusername', it should still work by sending the bitcoins to the local bitcoind/qt address
            print "CGMiner using batch file configured as: " + batfile
            batloc = dname + r"\Dependencies\cgminer\mine.bat"
            save = open(batloc, 'w+')
            save.write(batfile)
            save.close()
            self.TProgressbar1.step(99.9)
            global cgminer
            cgminer = subprocess.Popen(batloc, shell=False)
            print "------------------------------------------------------------"
            print "Mining operations started, work should now generate."
            print "------------------------------------------------------------"
            startedmining = 0
            mining = "Mining activated"
            on = 1
        else:
            p2pool.kill()
            cgminer.kill()
            print
            print "------------------------------------------------------------"
            print "Mining operations have stopped."
            print "------------------------------------------------------------"
            sys.stdout.flush()
            on = 0
            self.TProgressbar1.step(.1)
            mining = "Mining deactivated"







if __name__ == '__main__':
    vp_start_gui()
