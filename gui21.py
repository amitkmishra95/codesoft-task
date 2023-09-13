from tkinter import *

root = Tk()
root.geometry("550x550")
root.minsize(700,560)
root.title("CALCULATOR")
root.config(bg = 'green')
#root.wm_iconbitmap('calculator.ico')
width = root.winfo_width()
height = root.winfo_height()

answer = ""
def submit(num):

    global answer
    answer = answer + str(num)

    f_result.set(answer)



def final(fun):
    global answer
    try:




        answer = str(eval(answer))
        #answer.update()
        f_result.set(answer)

    except ZeroDivisionError:

        answer = 0
        f_result.set(answer)

    except SyntaxError:

        answer = "Invalid Input"
        f_result.set(answer)

def delete(fun):

    global answer
    #entry.delete(0,END)
    answer = answer[0:len(answer)-1]
    f_result.set(answer)

def clear():
    global answer
    answer = ''

    #equation.set(expression)
    f_result.set(answer)

f_result = StringVar()

entry = Entry(root , bg = 'white' ,width = 80 , font = ("calibre" , 50 , 'bold'),textvariable = f_result   )
entry.pack( anchor = 'n',pady = 10 , padx = 10  ,ipadx = 8 , ipady = 8, fill = X ,expand = True )


frame = Frame(root , width = root.winfo_width() , height = root.winfo_height() ,relief= RAISED , bg = 'grey')

frame.pack(anchor='s')

button_1 = Button(root , text = '1' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(1))
button_1.place(x = 10 , y = 400 )


button_2 = Button(root , text = '2' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(2))
button_2.place(x = 150 , y = 400 )


button_3 = Button(root , text = '3' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(3))
button_3.place(x = 290 , y = 400 )


button_a = Button(root , text = '+' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit('+'))
button_a.place(x = 430 , y = 320 )


button_0 = Button(root , text = '0' , bg = 'black' , fg = 'white' ,width = 13, font = ("arial" , 25 , 'bold'),command= lambda:submit(0))
button_0.place(x = 10 , y = 480 )

button_do = Button(root , text = '.' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit('.'))
button_do.place(x = 290 , y = 480 )

button_4 = Button(root , text = '4' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(4))
button_4.place(x = 10 , y = 320 )


button_5 = Button(root , text = '5' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(5))
button_5.place(x = 150 , y = 320 )


button_6 = Button(root , text = '6' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(6))
button_6.place(x = 290 , y = 320 )

button_7 = Button(root , text = '7' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(7))
button_7.place(x = 10 , y = 240 )


button_8 = Button(root , text = '8' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit(8))
button_8.place(x = 150 , y = 240 )


button_9 = Button(root , text = '9' , bg = 'black' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command=lambda :submit(9))
button_9.place(x = 290 , y = 240 )

button_c = Button(root , text = 'c' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command=clear)
button_c.place(x = 10 , y = 160 )


button_de = Button(root , text = 'del' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:delete('c'))
button_de.place(x = 150 , y = 160 )


button_di = Button(root , text = '/' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit('/'))
button_di.place(x = 290 , y = 160 )

button_m = Button(root , text = '*' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'),command= lambda:submit('*') )
button_m.place(x = 430 , y = 160 )

button_s = Button(root , text = ' - ' , bg = 'orange' , fg = 'white' ,width = 6, font = ("arial" , 25 , 'bold'), command= lambda:submit('-'))
button_s.place(x = 430 , y = 240 )

button_e = Button(root , text = ' = ' , bg = 'orange' , fg = 'black' ,width = 6,height = 3, font = ("arial" , 25 , 'bold'),command= lambda:final('='))
button_e.place(x = 430 , y = 400 )


root.mainloop()


