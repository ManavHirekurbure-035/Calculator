import tkinter

result = "" 

# add button clicked value to result variable
def add_to_result(value) :
    global result
    if len(result) > 0 :
        if isinstance(value, str):
            if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '%' :
                result=result[0:-1]
    
    
    result += str(value) 
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)

# Calculte the resultant value stored in result variable
def evaluate() :    
    global result
    result = text_result.get(1.0, "end")
    try:
        result = str(eval(result))        
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        
    except:   
        clear_screen()
        text_result.insert(1.0, "Error")
        
    
# remove the last added value    
def clear_element() :   
    global result
    if len(result) > 0 :
        result = result[0:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result) 
    else :
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)       
        
    
# clear the entire result value
def clear_screen() :
    global result
    result = ""
    text_result.delete(1.0, "end")



window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)


# input field for to display input value and calculated result 
text_result = tkinter.Text(window, height=1, width = 15, font=("Arial", 24), padx=5, pady=5)
text_result.grid(row=0, column=0, columnspan=4, padx=8, pady=20) 


# Row 1
tkinter.Button(window, text="*", height = 1, width = 5, command = lambda: add_to_result('*'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 1, column= 0, padx = 2, pady = 2)
tkinter.Button(window, text="/", height = 1, width = 5, command = lambda: add_to_result('/'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 1, column= 1, padx = 2, pady = 2)
tkinter.Button(window, text="CE", height = 1, width = 5, command = clear_element, font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 1, column= 2, padx = 2, pady = 2)
tkinter.Button(window, text="C", height = 1, width = 5, command = clear_screen, font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 1, column= 3, padx = 2, pady = 2)

# Row 2
tkinter.Button(window, text="1", height = 1, width = 5, command = lambda: add_to_result(1), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 2, column= 0, padx = 2, pady = 2)
tkinter.Button(window, text="2", height = 1, width = 5, command = lambda: add_to_result(2), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 2, column= 1, padx = 2, pady = 2)
tkinter.Button(window, text="3", height = 1, width = 5, command = lambda: add_to_result(3), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 2, column= 2, padx = 2, pady = 2)
tkinter.Button(window, text="%", height = 1, width = 5, command = lambda: add_to_result('%'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 2, column= 3, padx = 2, pady = 2)

# Row 3
tkinter.Button(window, text="4", height = 1, width = 5, command = lambda: add_to_result(4), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 3, column= 0, padx = 2, pady = 2)
tkinter.Button(window, text="5", height = 1, width = 5, command = lambda: add_to_result(5), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 3, column= 1, padx = 2, pady = 2)
tkinter.Button(window, text="6", height = 1, width = 5, command = lambda: add_to_result(6), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 3, column= 2, padx = 2, pady = 2)
tkinter.Button(window, text="+", height = 1, width = 5, command = lambda: add_to_result('+'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 3, column= 3, padx = 2, pady = 2)

# Row 4
tkinter.Button(window, text="7", height = 1, width = 5, command = lambda: add_to_result(7), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 4, column= 0, padx = 2, pady = 2)
tkinter.Button(window, text="8", height = 1, width = 5, command = lambda: add_to_result(8), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 4, column= 1, padx = 2, pady = 2)
tkinter.Button(window, text="9", height = 1, width = 5, command = lambda: add_to_result(9), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 4, column= 2, padx = 2, pady = 2)
tkinter.Button(window, text="-", height = 1, width = 5, command = lambda: add_to_result('-'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 4, column= 3, padx = 2, pady = 2)

# row 5
tkinter.Button(window, text="0", height = 1, width = 11, command = lambda: add_to_result(0), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 5, column= 0, columnspan = 2, padx = 2, pady = 2)
tkinter.Button(window, text=".", height = 1, width = 5, command = lambda: add_to_result('.'), font = ("Comic Sans MS", 16), activebackground = "#C4BFBF").grid(row = 5, column= 2, padx = 2, pady = 2)
tkinter.Button(window, text="Enter", height = 1, width = 5, command = evaluate, font = ("Comic Sans MS", 16), bg = "#57B7FF").grid(row = 5, column= 3, padx = 2, pady = 2)


window.mainloop()