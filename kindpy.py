import tkinter
label=0
window = tkinter.Tk()

def 출력(am):
    print(am)

def 입력다음출력(inp, qut):
    qut = input(inp)
    print(qut)

def 변수생성(vo):
    vo = 0

def gui생성(w, h):
    window.geometry(f"{w}x{h}")

def gui실행():
    window.mainloop()

def gui제목(jamok):
    window.title(jamok)

def gui텍스트(text):
    label = tkinter.Label(window, text=text)
    label.pack()
def gui버튼(button):
    button1 = tkinter.Button(window, text=button, command=guibuttonn)
    button1.pack()
def guibuttonn(a):
    print(a)
def 적기(a,b):
    f = open(a, 'w')
    f.write(b)
    f.close()
