import tkinter
import random
import sys,os
from tkinter import messagebox

root = tkinter.Tk()
root.title("Sudoku Raw")

box1 = tkinter.StringVar()
box2 = tkinter.StringVar()
box3 = tkinter.StringVar()
box4 = tkinter.StringVar()
box5 = tkinter.StringVar()
box6 = tkinter.StringVar()
box7 = tkinter.StringVar()
box8 = tkinter.StringVar()
box9 = tkinter.StringVar()

box10 = tkinter.StringVar()
box11 = tkinter.StringVar()
box12 = tkinter.StringVar()
box13 = tkinter.StringVar()
box14 = tkinter.StringVar()
box15 = tkinter.StringVar()
box16 = tkinter.StringVar()
box17 = tkinter.StringVar()
box18 = tkinter.StringVar()

box19 = tkinter.StringVar()
box20 = tkinter.StringVar()
box21 = tkinter.StringVar()
box22 = tkinter.StringVar()
box23 = tkinter.StringVar()
box24 = tkinter.StringVar()
box25 = tkinter.StringVar()
box26 = tkinter.StringVar()
box27 = tkinter.StringVar()

box28 = tkinter.StringVar()
box29 = tkinter.StringVar()
box30 = tkinter.StringVar()
box31 = tkinter.StringVar()
box32 = tkinter.StringVar()
box33 = tkinter.StringVar()
box34 = tkinter.StringVar()
box35 = tkinter.StringVar()
box36 = tkinter.StringVar()

box37 = tkinter.StringVar()
box38 = tkinter.StringVar()
box39 = tkinter.StringVar()
box40 = tkinter.StringVar()
box41 = tkinter.StringVar()
box42 = tkinter.StringVar()
box43 = tkinter.StringVar()
box44 = tkinter.StringVar()
box45 = tkinter.StringVar()

box46 = tkinter.StringVar()
box47 = tkinter.StringVar()
box48 = tkinter.StringVar()
box49 = tkinter.StringVar()
box50 = tkinter.StringVar()
box51 = tkinter.StringVar()
box52 = tkinter.StringVar()
box53 = tkinter.StringVar()
box54 = tkinter.StringVar()

box55 = tkinter.StringVar()
box56 = tkinter.StringVar()
box57 = tkinter.StringVar()
box58 = tkinter.StringVar()
box59 = tkinter.StringVar()
box60 = tkinter.StringVar()
box61 = tkinter.StringVar()
box62 = tkinter.StringVar()
box63 = tkinter.StringVar()

box64 = tkinter.StringVar()
box65 = tkinter.StringVar()
box66 = tkinter.StringVar()
box67 = tkinter.StringVar()
box68 = tkinter.StringVar()
box69 = tkinter.StringVar()
box70 = tkinter.StringVar()
box71 = tkinter.StringVar()
box72 = tkinter.StringVar()

box73 = tkinter.StringVar()
box74 = tkinter.StringVar()
box75 = tkinter.StringVar()
box76 = tkinter.StringVar()
box77 = tkinter.StringVar()
box78 = tkinter.StringVar()
box79 = tkinter.StringVar()
box80 = tkinter.StringVar()
box81 = tkinter.StringVar()

array_boxes = [
box1,box2,box3,box4,box5,box6,box7,box8,box9,
box10,box11,box12,box13,box14,box15,box16,box17,box18,
box19,box20,box21,box22,box23,box24,box25,box26,box27,
box28,box29,box30,box31,box32,box33,box34,box35,box36,
box37,box38,box39,box40,box41,box42,box43,box44,box45,
box46,box47,box48,box49,box50,box51,box52,box53,box54,
box55,box56,box57,box58,box59,box60,box61,box62,box63,
box64,box65,box66,box67,box68,box69,box70,box71,box72,
box73,box74,box75,box76,box77,box78,box79,box80,box81
]






grid = [
    [box1.get(),box2.get(),box3.get(),box4.get(),box5.get(),box6.get(),box7.get(),box8.get(),box9.get()],
    [box10.get(),box11.get(),box12.get(),box13.get(),box14.get(),box15.get(),box16.get(),box17.get(),box18.get()],
    [box19.get(),box20.get(),box21.get(),box22.get(),box23.get(),box24.get(),box25.get(),box26.get(),box27.get()],
    [box28.get(),box29.get(),box30.get(),box31.get(),box32.get(),box33.get(),box34.get(),box35.get(),box36.get()],
    [box37.get(),box38.get(),box39.get(),box40.get(),box41.get(),box42.get(),box43.get(),box44.get(),box45.get()],
    [box46.get(),box47.get(),box48.get(),box49.get(),box50.get(),box51.get(),box52.get(),box52.get(),box54.get()],
    [box55.get(),box56.get(),box57.get(),box58.get(),box59.get(),box60.get(),box61.get(),box62.get(),box63.get()],
    [box64.get(),box65.get(),box66.get(),box67.get(),box68.get(),box69.get(),box70.get(),box71.get(),box72.get()],
    [box73.get(),box74.get(),box75.get(),box76.get(),box77.get(),box78.get(),box79.get(),box80.get(),box81.get()]
    ]



row1 = [box1.get(),box2.get(),box3.get(),box10.get(),box11.get(),box12.get(),box19.get(),box20.get(),box21.get()]
row2 = [box4.get(),box5.get(),box6.get(),box13.get(),box14.get(),box15.get(),box22.get(),box23.get(),box24.get()]
row3 = [box7.get(),box8.get(),box9.get(),box16.get(),box17.get(),box18.get(),box25.get(),box26.get(),box27.get()]
row4 = [box28.get(),box29.get(),box30.get(),box37.get(),box38.get(),box39.get(),box46.get(),box47.get(),box48.get()]
row5 = [box31.get(),box32.get(),box33.get(),box40.get(),box41.get(),box42.get(),box49.get(),box50.get(),box51.get()]
row6 = [box34.get(),box35.get(),box36.get(),box43.get(),box44.get(),box45.get(),box52.get(),box53.get(),box54.get()]
row7 = [box55.get(),box56.get(),box57.get(),box64.get(),box65.get(),box66.get(),box73.get(),box74.get(),box75.get()]
row8 = [box58.get(),box59.get(),box60.get(),box67.get(),box68.get(),box69.get(),box76.get(),box77.get(),box78.get()]
row9 = [box61.get(),box62.get(),box63.get(),box70.get(),box71.get(),box72.get(),box79.get(),box80.get(),box81.get()]



row_array = [row1,row2,row3,row4,row5,row6,row7,row8,row9]


col1 = [box1.get(),box4.get(),box7.get(),box28.get(),box31.get(),box34.get(),box55.get(),box58.get(),box61.get()]
col2 = [box2.get(),box5.get(),box8.get(),box29.get(),box32.get(),box35.get(),box56.get(),box59.get(),box62.get()]
col3 = [box3.get(),box6.get(),box9.get(),box30.get(),box33.get(),box36.get(),box57.get(),box60.get(),box63.get()]
col4 = [box10.get(),box13.get(),box16.get(),box37.get(),box40.get(),box43.get(),box64.get(),box67.get(),box70.get()]
col5 = [box11.get(),box14.get(),box17.get(),box38.get(),box41.get(),box44.get(),box65.get(),box68.get(),box71.get()]
col6 = [box12.get(),box15.get(),box18.get(),box39.get(),box42.get(),box45.get(),box66.get(),box69.get(),box72.get()]
col7 = [box19.get(),box22.get(),box25.get(),box46.get(),box49.get(),box52.get(),box73.get(),box76.get(),box79.get()]
col8 = [box20.get(),box23.get(),box26.get(),box47.get(),box50.get(),box53.get(),box74.get(),box77.get(),box80.get()]
col9 = [box21.get(),box24.get(),box27.get(),box48.get(),box51.get(),box54.get(),box75.get(),box78.get(),box81.get()]

col_array = [col1,col2,col3,col4,col5,col6,col7,col8,col9]



def update_grid():
    global grid
    grid = [
    [box1.get(),box2.get(),box3.get(),box4.get(),box5.get(),box6.get(),box7.get(),box8.get(),box9.get()],
    [box10.get(),box11.get(),box12.get(),box13.get(),box14.get(),box15.get(),box16.get(),box17.get(),box18.get()],
    [box19.get(),box20.get(),box21.get(),box22.get(),box23.get(),box24.get(),box25.get(),box26.get(),box27.get()],
    [box28.get(),box29.get(),box30.get(),box31.get(),box32.get(),box33.get(),box34.get(),box35.get(),box36.get()],
    [box37.get(),box38.get(),box39.get(),box40.get(),box41.get(),box42.get(),box43.get(),box44.get(),box45.get()],
    [box46.get(),box47.get(),box48.get(),box49.get(),box50.get(),box51.get(),box52.get(),box52.get(),box54.get()],
    [box55.get(),box56.get(),box57.get(),box58.get(),box59.get(),box60.get(),box61.get(),box62.get(),box63.get()],
    [box64.get(),box65.get(),box66.get(),box67.get(),box68.get(),box69.get(),box70.get(),box71.get(),box72.get()],
    [box73.get(),box74.get(),box75.get(),box76.get(),box77.get(),box78.get(),box79.get(),box80.get(),box81.get()]
    ]
    
def update_row():
    global row1,row2,row3,row4,row5,row6,row7,row8,row9,row_array
    row1 = [box1.get(),box2.get(),box3.get(),box10.get(),box11.get(),box12.get(),box19.get(),box20.get(),box21.get()]
    row2 = [box4.get(),box5.get(),box6.get(),box13.get(),box14.get(),box15.get(),box22.get(),box23.get(),box24.get()]
    row3 = [box7.get(),box8.get(),box9.get(),box16.get(),box17.get(),box18.get(),box25.get(),box26.get(),box27.get()]
    row4 = [box28.get(),box29.get(),box30.get(),box37.get(),box38.get(),box39.get(),box46.get(),box47.get(),box48.get()]
    row5 = [box31.get(),box32.get(),box33.get(),box40.get(),box41.get(),box42.get(),box49.get(),box50.get(),box51.get()]
    row6 = [box34.get(),box35.get(),box36.get(),box43.get(),box44.get(),box45.get(),box52.get(),box53.get(),box54.get()]
    row7 = [box55.get(),box56.get(),box57.get(),box64.get(),box65.get(),box66.get(),box73.get(),box74.get(),box75.get()]
    row8 = [box58.get(),box59.get(),box60.get(),box67.get(),box68.get(),box69.get(),box76.get(),box77.get(),box78.get()]
    row9 = [box61.get(),box62.get(),box63.get(),box70.get(),box71.get(),box72.get(),box79.get(),box80.get(),box81.get()]
    row_array = [row1,row2,row3,row4,row5,row6,row7,row8,row9]

def update_col():
    global col1,col2,col3,col4,col5,col6,col7,col8,col9,col_array
    col1 = [box1.get(),box4.get(),box7.get(),box28.get(),box31.get(),box34.get(),box55.get(),box58.get(),box61.get()]
    col2 = [box2.get(),box5.get(),box8.get(),box29.get(),box32.get(),box35.get(),box56.get(),box59.get(),box62.get()]
    col3 = [box3.get(),box6.get(),box9.get(),box30.get(),box33.get(),box36.get(),box57.get(),box60.get(),box63.get()]
    col4 = [box10.get(),box13.get(),box16.get(),box37.get(),box40.get(),box43.get(),box64.get(),box67.get(),box70.get()]
    col5 = [box11.get(),box14.get(),box17.get(),box38.get(),box41.get(),box44.get(),box65.get(),box68.get(),box71.get()]
    col6 = [box12.get(),box15.get(),box18.get(),box39.get(),box42.get(),box45.get(),box66.get(),box69.get(),box72.get()]
    col7 = [box19.get(),box22.get(),box25.get(),box46.get(),box49.get(),box52.get(),box73.get(),box76.get(),box79.get()]
    col8 = [box20.get(),box23.get(),box26.get(),box47.get(),box50.get(),box53.get(),box74.get(),box77.get(),box80.get()]
    col9 = [box21.get(),box24.get(),box27.get(),box48.get(),box51.get(),box54.get(),box75.get(),box78.get(),box81.get()]
    col_array = [col1,col2,col3,col4,col5,col6,col7,col8,col9]


def empty_check(arr):
    if arr == "":
        return False
    else:
        return True



def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)       



def grid_length_function():
    global grid_length
    grid_length = 0
    for x in grid:
        x_filter = set(filter(empty_check,x))
        grid_length = len(x_filter) + grid_length

    return grid_length

grid_length_function()

def solve():
    
    i = 0

    messagebox.showinfo("Instruction","Please hold 'ENTER' button for 10 Seconds")


    if(grid_length >= 50):
        messagebox.showerror("Not allowed","You cannot use it more than once")

    duplicate_in_grid = False
    duplicate_in_row = False
    duplicate_in_col = False
    duplicate_collector = []
    
    
    while grid_length != 50:
        grid_length_function()
        cell_select = random.randint(0,80)
        i = random.randint(1,9)
        val = array_boxes[cell_select].get()
        while cell_select in duplicate_collector:
            cell_select = random.randint(0,80)
            val = array_boxes[cell_select].get()
            
        
        if(not val):
            array_boxes[cell_select].set(i)
            
            update_col()
            update_grid()
            update_row()
        
            x_filter1 = list(filter(empty_check,grid[0]))
            x_set1 =  set(x_filter1)
            x_filter2 = list(filter(empty_check,grid[1]))
            x_set2 =  set(x_filter2)
            x_filter3 = list(filter(empty_check,grid[2]))
            x_set3 =  set(x_filter3)
            x_filter4 = list(filter(empty_check,grid[3]))
            x_set4 =  set(x_filter4)
            x_filter5 = list(filter(empty_check,grid[4]))
            x_set5 =  set(x_filter5)
            x_filter6 = list(filter(empty_check,grid[5]))
            x_set6 =  set(x_filter6)
            x_filter7 = list(filter(empty_check,grid[6]))
            x_set7 =  set(x_filter7)
            x_filter8 = list(filter(empty_check,grid[7]))
            x_set8 =  set(x_filter8)
            x_filter9 = list(filter(empty_check,grid[8]))
            x_set9 =  set(x_filter9)

            row_filter_1 = list(filter(empty_check,row_array[0]))
            row_set_1 = set(row_filter_1)
            row_filter_2 = list(filter(empty_check,row_array[1]))
            row_set_2 = set(row_filter_2)
            row_filter_3 = list(filter(empty_check,row_array[2]))
            row_set_3 = set(row_filter_3)
            row_filter_4 = list(filter(empty_check,row_array[3]))
            row_set_4 = set(row_filter_4)
            row_filter_5 = list(filter(empty_check,row_array[4]))
            row_set_5 = set(row_filter_5)
            row_filter_6 = list(filter(empty_check,row_array[5]))
            row_set_6 = set(row_filter_6)
            row_filter_7 = list(filter(empty_check,row_array[6]))
            row_set_7 = set(row_filter_7)
            row_filter_8 = list(filter(empty_check,row_array[7]))
            row_set_8 = set(row_filter_8)
            row_filter_9 = list(filter(empty_check,row_array[8]))
            row_set_9 = set(row_filter_9)

            col_filter_1 = list(filter(empty_check,col_array[0]))
            col_set_1 = set(col_filter_1)
            col_filter_2 = list(filter(empty_check,col_array[1]))
            col_set_2 = set(col_filter_2)
            col_filter_3 = list(filter(empty_check,col_array[2]))
            col_set_3 = set(col_filter_3)
            col_filter_4 = list(filter(empty_check,col_array[3]))
            col_set_4 = set(col_filter_4)
            col_filter_5 = list(filter(empty_check,col_array[4]))
            col_set_5 = set(col_filter_5)
            col_filter_6 = list(filter(empty_check,col_array[5]))
            col_set_6 = set(col_filter_6)
            col_filter_7 = list(filter(empty_check,col_array[6]))
            col_set_7 = set(col_filter_7)
            col_filter_8 = list(filter(empty_check,col_array[7]))
            col_set_8 = set(col_filter_8)
            col_filter_9 = list(filter(empty_check,col_array[8]))
            col_set_9 = set(col_filter_9)


            if(len(x_filter1) != len(x_set1) or len(x_filter2) != len(x_set2) or len(x_filter3) != len(x_set3) or len(x_filter4) != len(x_set4) or len(x_filter5) != len(x_set5) or len(x_filter6) != len(x_set6) or len(x_filter7) != len(x_set7) or len(x_filter8) != len(x_set8) or len(x_filter9) != len(x_set9)):
                array_boxes[cell_select].set('')
                duplicate_in_grid = True
                

            if(len(row_filter_1) != len(row_set_1) or len(row_filter_2) != len(row_set_2) or len(row_filter_3) != len(row_set_3) or len(row_filter_4) != len(row_set_4) or len(row_filter_5) != len(row_set_5) or len(row_filter_6) != len(row_set_6) or len(row_filter_7) != len(row_set_7) or len(row_filter_8) != len(row_set_8) or len(row_filter_9) != len(row_set_9)):
                array_boxes[cell_select].set('')
                duplicate_in_row  = True
                
            
            if(len(col_filter_1) != len(col_set_1) or len(col_filter_2) != len(col_set_2) or len(col_filter_3) != len(col_set_3) or len(col_filter_4) != len(col_set_4) or len(col_filter_5) != len(col_set_5) or len(col_filter_6) != len(col_set_6) or len(col_filter_7) != len(col_set_7) or len(col_filter_8) != len(col_set_8) or len(col_filter_9) != len(col_set_9)):
                array_boxes[cell_select].set('')
                duplicate_in_col = True
            
            
            if(duplicate_in_col or duplicate_in_grid or duplicate_in_row):
                pass
            else:
                duplicate_collector.append(cell_select)
            
        else:
            duplicate_collector.append(cell_select)

    if(i == 0):
        messagebox.showinfo("Finished Solving","Please Release 'ENTER' button")
    i = i + 1

def duplicate_check():
    temp_grid = []
    temp_row = []
    temp_col = []
    
    
    for x in grid:

        
        filtered_set = filter(empty_check,x)
        for y in filtered_set:
            i=0
            temp_grid.insert(i,y)
            i=i+1
        cell_set = set(temp_grid)
        if(len(temp_grid) != len(cell_set)):
            messagebox.showwarning("Duplicate Found","There is Duplicate in the Cell You have entered")
            
            return 
        else:
            temp_grid = []
            
    

    for x in row_array:
        filtered_row = filter(empty_check,x)
        for y in filtered_row:
            i=0
            temp_row.insert(i,y)
            i=i+1
        row_set = set(temp_row)
        if(len(temp_row)!=len(row_set)):
            messagebox.showwarning("Duplicate in row","There is a Duplicate in row you entered")
            
            return
        else:
            temp_row = []
            

    for x in col_array:
        filtered_col = filter(empty_check,x)
        for y in filtered_col:
            i=0
            temp_col.insert(i,y)
            i=i+1
        col_set = set(temp_col)
        if(len(temp_col) != len(col_set)):
            messagebox.showwarning("Duplicate in Column","There is duplicate in the Column you entered")
            
            return
        else:
            temp_col = []
            
def quit_option():
    
    res = messagebox.askyesno("Exit application","Do you really want to exit") 
    if res:
        root.destroy()
    else:
        pass

def clicked_box1(var):
    global cell1
    global row1
    val = var.get()
    num = ['1','2','3','4','5','6','7','8','9','']

    if(val in num):
        pass
    else:
        messagebox.showinfo('Illegal Character detected','Value not allowed')
        cell1.delete(0,tkinter.END)
        return

    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell1.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][0] = val_int
            update_grid()
            update_col()
            update_row()
            duplicate_check()
        else:
            grid[0][0] = ''
            update_grid()
            update_col()
            update_row()
        
def clicked_box2(var):
    global cell2
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell2.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
               
def clicked_box3(var):
    global cell3
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell3.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()

def clicked_box4(var):
    global cell4
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell4.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][3] = val_int
            update_grid()
            update_col()
            update_col()
            duplicate_check()
        else:
            grid[0][3] = ''
            update_grid()
            update_col()
            update_col()

def clicked_box5(var):
    global cell5
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell5.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[0][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box6(var):
    global cell6
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell6.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[0][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box7(var):
    global cell7
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell7.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[0][6] = ''
            update_grid()
            update_row()
            update_col()
        
def clicked_box8(var):
    global cell8
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell8.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[0][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box9(var):
    global cell9
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell9.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[0][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
            
        else:
            grid[0][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box10(var):
    global cell10
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell10.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box11(var):
    global cell11
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell11.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box12(var):
    global cell12
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell12.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box13(var):
    global cell13
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell13.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box14(var):
    global cell14
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell14.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box15(var):
    global cell15
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell15.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box16(var):
    global cell16
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell16.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box17(var):
    global cell17
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell17.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box18(var):
    global cell18
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell18.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[1][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[1][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box19(var):
    global cell19
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell19.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box20(var):
    global cell20
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell20.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box21(var):
    global cell21
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell21.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box22(var):
    global cell22
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell22.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box23(var):
    global cell23
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell23.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box24(var):
    global cell24
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell24.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box25(var):
    global cell25
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell25.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box26(var):
    global cell26
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell26.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box27(var):
    global cell27
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell27.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[2][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[2][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box28(var):
    global cell28
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell28.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box29(var):
    global cell29
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell29.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box30(var):
    global cell30
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell30.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box31(var):
    global cell31
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell31.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box32(var):
    global cell32
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell32.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][4] = val_int
            update_grid()
            update_row()
            update_col()

            duplicate_check()
        else:
            grid[3][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box33(var):
    global cell33
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell33.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box34(var):
    global cell34
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell34.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box35(var):
    global cell35
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell35.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box36(var):
    global cell36
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell36.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[3][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[3][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box37(var):
    global cell37
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell37.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box38(var):
    global cell38
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell38.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box39(var):
    global cell39
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell39.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box40(var):
    global cell40
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell40.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box41(var):
    global cell41
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell41.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box42(var):
    global cell42
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell42.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box43(var):
    global cell43
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell43.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box44(var):
    global cell44
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell44.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box45(var):
    global cell45
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell45.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[4][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[4][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box46(var):
    global cell46
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell46.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box47(var):
    global cell47
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell47.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box48(var):
    global cell48
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell48.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box49(var):
    global cell49
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell49.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box50(var):
    global cell50
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell50.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box51(var):
    global cell51
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell51.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box52(var):
    global cell52
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell52.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box53(var):
    global cell53
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell53.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box54(var):
    global cell54
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell54.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[5][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[5][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box55(var):
    global cell55
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell55.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box56(var):
    global cell56
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell56.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box57(var):
    global cell57
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell57.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box58(var):
    global cell58
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell58.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box59(var):
    global cell59
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell59.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box60(var):
    global cell60
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell60.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box61(var):
    global cell61
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell61.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box62(var):
    global cell62
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell62.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box63(var):
    global cell63
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell63.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[6][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[6][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box64(var):
    global cell64
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell64.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box65(var):
    global cell65
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell65.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box66(var):
    global cell66
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell66.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box67(var):
    global cell67
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell67.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box68(var):
    global cell68
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell68.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box69(var):
    global cell69
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell69.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box70(var):
    global cell70
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell70.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box71(var):
    global cell71
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell71.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box72(var):
    global cell72
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell72.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[7][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[7][8] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box73(var):
    global cell73
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell73.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][0] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][0] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box74(var):
    global cell74
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell74.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][1] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][1] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box75(var):
    global cell75
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell75.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][2] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][2] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box76(var):
    global cell76
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell76.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][3] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][3] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box77(var):
    global cell77
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell77.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][4] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][4] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box78(var):
    global cell78
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell78.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][5] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][5] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box79(var):
    global cell79

    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell79.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][6] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][6] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box80(var):
    global cell80
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell80.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][7] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][7] = ''
            update_grid()
            update_row()
            update_col()

def clicked_box81(var):
    global cell81
    
    val = var.get()
    
    if(len(var.get()) > 1):
        messagebox.showinfo("Multiple Values Detected","You can only enter one value in each box")
        cell81.delete(1,tkinter.END)
    else:
        if(val):
            val_int = int(val)
            grid[8][8] = val_int
            update_grid()
            update_row()
            update_col()
            duplicate_check()
        else:
            grid[8][8] = ''
            update_grid()
            update_row()
            update_col()





cell1_color = "#d5dbd8"
cell2_color = "#ffffff"
cell3_color = "#d5dbd8"
cell4_color = "#ffffff"
cell5_color = "#d5dbd8"
cell6_color = "#ffffff"
cell7_color = "#d5dbd8"
cell8_color = "#ffffff"
cell9_color = "#d5dbd8"

font_size = ("bold",15)

#Cell Declaration

cell1 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box1,bg=cell1_color,font=font_size)
cell2 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box2,bg=cell1_color,font=font_size)
cell3 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box3,bg=cell1_color,font=font_size)
cell4 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box4,bg=cell1_color,font=font_size)
cell5 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box5,bg=cell1_color,font=font_size)
cell6 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box6,bg=cell1_color,font=font_size)
cell7 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box7,bg=cell1_color,font=font_size)
cell8 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box8,bg=cell1_color,font=font_size)
cell9 = tkinter.Entry(root,relief="solid",width=5,justify="center",textvariable=box9,bg=cell1_color,font=font_size)

cell10 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box10,bg=cell2_color,font=font_size)
cell11 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box11,bg=cell2_color,font=font_size)
cell12 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box12,bg=cell2_color,font=font_size)
cell13 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box13,bg=cell2_color,font=font_size)
cell14 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box14,bg=cell2_color,font=font_size)
cell15 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box15,bg=cell2_color,font=font_size)
cell16 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box16,bg=cell2_color,font=font_size)
cell17 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box17,bg=cell2_color,font=font_size)
cell18 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box18,bg=cell2_color,font=font_size)

cell19 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box19,bg=cell3_color,font=font_size)
cell20 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box20,bg=cell3_color,font=font_size)
cell21 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box21,bg=cell3_color,font=font_size)
cell22 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box22,bg=cell3_color,font=font_size)
cell23 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box23,bg=cell3_color,font=font_size)
cell24 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box24,bg=cell3_color,font=font_size)
cell25 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box25,bg=cell3_color,font=font_size)
cell26 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box26,bg=cell3_color,font=font_size)
cell27 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box27,bg=cell3_color,font=font_size)

cell28 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box28,bg=cell4_color,font=font_size)
cell29 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box29,bg=cell4_color,font=font_size)
cell30 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box30,bg=cell4_color,font=font_size)
cell31 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box31,bg=cell4_color,font=font_size)
cell32 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box32,bg=cell4_color,font=font_size)
cell33 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box33,bg=cell4_color,font=font_size)
cell34 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box34,bg=cell4_color,font=font_size)
cell35 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box35,bg=cell4_color,font=font_size)
cell36 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box36,bg=cell4_color,font=font_size)

cell37 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box37,bg=cell5_color,font=font_size)
cell38 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box38,bg=cell5_color,font=font_size)
cell39 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box39,bg=cell5_color,font=font_size)
cell40 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box40,bg=cell5_color,font=font_size)
cell41 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box41,bg=cell5_color,font=font_size)
cell42 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box42,bg=cell5_color,font=font_size)
cell43 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box43,bg=cell5_color,font=font_size)
cell44 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box44,bg=cell5_color,font=font_size)
cell45 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box45,bg=cell5_color,font=font_size)

cell46 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box46,bg=cell6_color,font=font_size)
cell47 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box47,bg=cell6_color,font=font_size)
cell48 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box48,bg=cell6_color,font=font_size)
cell49 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box49,bg=cell6_color,font=font_size)
cell50 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box50,bg=cell6_color,font=font_size)
cell51 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box51,bg=cell6_color,font=font_size)
cell52 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box52,bg=cell6_color,font=font_size)
cell53 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box53,bg=cell6_color,font=font_size)
cell54 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box54,bg=cell6_color,font=font_size)

cell55 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box55,bg=cell7_color,font=font_size)
cell56 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box56,bg=cell7_color,font=font_size)
cell57 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box57,bg=cell7_color,font=font_size)
cell58 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box58,bg=cell7_color,font=font_size)
cell59 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box59,bg=cell7_color,font=font_size)
cell60 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box60,bg=cell7_color,font=font_size)
cell61 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box61,bg=cell7_color,font=font_size)
cell62 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box62,bg=cell7_color,font=font_size)
cell63 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box63,bg=cell7_color,font=font_size)

cell64 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box64,bg=cell8_color,font=font_size)
cell65 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box65,bg=cell8_color,font=font_size)
cell66 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box66,bg=cell8_color,font=font_size)
cell67 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box67,bg=cell8_color,font=font_size)
cell68 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box68,bg=cell8_color,font=font_size)
cell69 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box69,bg=cell8_color,font=font_size)
cell70 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box70,bg=cell8_color,font=font_size)
cell71 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box71,bg=cell8_color,font=font_size)
cell72 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box72,bg=cell8_color,font=font_size)

cell73 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box73,bg=cell9_color,font=font_size)
cell74 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box74,bg=cell9_color,font=font_size)
cell75 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box75,bg=cell9_color,font=font_size)
cell76 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box76,bg=cell9_color,font=font_size)
cell77 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box77,bg=cell9_color,font=font_size)
cell78 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box78,bg=cell9_color,font=font_size)
cell79 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box79,bg=cell9_color,font=font_size)
cell80 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box80,bg=cell9_color,font=font_size)
cell81 = tkinter.Entry(root,relief='solid',width=5,justify='center',textvariable=box81,bg=cell9_color,font=font_size)


array_cells = [
cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9,
cell10,cell11,cell12,cell13,cell14,cell15,cell16,cell17,cell18,
cell19,cell20,cell21,cell22,cell23,cell24,cell25,cell26,cell27,
cell28,cell29,cell30,cell31,cell32,cell33,cell34,cell35,cell36,
cell37,cell38,cell39,cell40,cell41,cell42,cell43,cell44,cell45,
cell46,cell47,cell48,cell49,cell50,cell51,cell52,cell53,cell54,
cell55,cell56,cell57,cell58,cell59,cell60,cell61,cell62,cell63,
cell64,cell65,cell66,cell67,cell68,cell69,cell70,cell71,cell72,
cell73,cell74,cell75,cell76,cell77,cell78,cell79,cell80,cell81
]

#Generating Function

def gen():
    i=0
   
    while i<90:
        
        cell_select = random.randint(0,80)
        cell_value = random.randint(1,9)
        array_boxes[cell_select].set(cell_value)
        update_grid()
        update_col()
        update_row()

        x_filter1 = list(filter(empty_check,grid[0]))
        x_set1 =  set(x_filter1)
        x_filter2 = list(filter(empty_check,grid[1]))
        x_set2 =  set(x_filter2)
        x_filter3 = list(filter(empty_check,grid[2]))
        x_set3 =  set(x_filter3)
        x_filter4 = list(filter(empty_check,grid[3]))
        x_set4 =  set(x_filter3)
        x_filter5 = list(filter(empty_check,grid[4]))
        x_set5 =  set(x_filter5)
        x_filter6 = list(filter(empty_check,grid[5]))
        x_set6 =  set(x_filter6)
        x_filter7 = list(filter(empty_check,grid[6]))
        x_set7 =  set(x_filter7)
        x_filter8 = list(filter(empty_check,grid[7]))
        x_set8 =  set(x_filter8)
        x_filter9 = list(filter(empty_check,grid[8]))
        x_set9 =  set(x_filter9)

        row_filter_1 = list(filter(empty_check,row_array[0]))
        row_set_1 = set(row_filter_1)
        row_filter_2 = list(filter(empty_check,row_array[1]))
        row_set_2 = set(row_filter_2)
        row_filter_3 = list(filter(empty_check,row_array[2]))
        row_set_3 = set(row_filter_3)
        row_filter_4 = list(filter(empty_check,row_array[3]))
        row_set_4 = set(row_filter_4)
        row_filter_5 = list(filter(empty_check,row_array[4]))
        row_set_5 = set(row_filter_5)
        row_filter_6 = list(filter(empty_check,row_array[5]))
        row_set_6 = set(row_filter_6)
        row_filter_7 = list(filter(empty_check,row_array[6]))
        row_set_7 = set(row_filter_7)
        row_filter_8 = list(filter(empty_check,row_array[7]))
        row_set_8 = set(row_filter_8)
        row_filter_9 = list(filter(empty_check,row_array[8]))
        row_set_9 = set(row_filter_9)
        
        col_filter_1 = list(filter(empty_check,col_array[0]))
        col_set_1 = set(col_filter_1)
        col_filter_2 = list(filter(empty_check,col_array[1]))
        col_set_2 = set(col_filter_2)
        col_filter_3 = list(filter(empty_check,col_array[2]))
        col_set_3 = set(col_filter_3)
        col_filter_4 = list(filter(empty_check,col_array[3]))
        col_set_4 = set(col_filter_4)
        col_filter_5 = list(filter(empty_check,col_array[4]))
        col_set_5 = set(col_filter_5)
        col_filter_6 = list(filter(empty_check,col_array[5]))
        col_set_6 = set(col_filter_6)
        col_filter_7 = list(filter(empty_check,col_array[6]))
        col_set_7 = set(col_filter_7)
        col_filter_8 = list(filter(empty_check,col_array[7]))
        col_set_8 = set(col_filter_8)
        col_filter_9 = list(filter(empty_check,col_array[8]))
        col_set_9 = set(col_filter_9)
        
        dup_in_grid = True
        dup_in_row = True
        dup_in_col = True

        if(len(x_filter1) != len(x_set1) or len(x_filter2) != len(x_set2) or len(x_filter3) != len(x_set3) or len(x_filter4) != len(x_set4) or len(x_filter5) != len(x_set5) or len(x_filter6) != len(x_set6) or len(x_filter7) != len(x_set7) or len(x_filter8) != len(x_set8) or len(x_filter9) != len(x_set9)):
            array_boxes[cell_select].set('')
            dup_in_grid = False
            
            

        if(len(row_filter_1) != len(row_set_1) or len(row_filter_2) != len(row_set_2) or len(row_filter_3) != len(row_set_3) or len(row_filter_4) != len(row_set_4) or len(row_filter_5) != len(row_set_5) or len(row_filter_6) != len(row_set_6) or len(row_filter_7) != len(row_set_7) or len(row_filter_8) != len(row_set_8) or len(row_filter_9) != len(row_set_9)):
            array_boxes[cell_select].set('')
            dup_in_row = False
            
        
        if(len(col_filter_1) != len(col_set_1) or len(col_filter_2) != len(col_set_2) or len(col_filter_3) != len(col_set_3) or len(col_filter_4) != len(col_set_4) or len(col_filter_5) != len(col_set_5) or len(col_filter_6) != len(col_set_6) or len(col_filter_7) != len(col_set_7) or len(col_filter_8) != len(col_set_8) or len(col_filter_9) != len(col_set_9)):
            array_boxes[cell_select].set('')
            dup_in_col = False
            
       

        if(dup_in_grid and dup_in_col and dup_in_row):
            array_cells[cell_select].config(state="disable")

        
        i = i+1

gen()

#Tracing StringVariable

box1.trace("w",lambda name,index,mode,box1=box1:clicked_box1(box1))
box2.trace("w",lambda name,index,mode,box2=box2:clicked_box2(box2))
box3.trace("w",lambda name,index,mode,box3=box3:clicked_box3(box3))
box4.trace("w",lambda name,index,mode,box4=box4:clicked_box4(box4))
box5.trace("w",lambda name,index,mode,box5=box5:clicked_box5(box5))
box6.trace("w",lambda name,index,mode,box6=box6:clicked_box6(box6))
box7.trace("w",lambda name,index,mode,box7=box7:clicked_box7(box7))
box8.trace("w",lambda name,index,mode,box8=box8:clicked_box8(box8))
box9.trace("w",lambda name,index,mode,box9=box9:clicked_box9(box9))

box10.trace("w",lambda name,index,mode,box10=box10:clicked_box10(box10))
box11.trace("w",lambda name,index,mode,box11=box11:clicked_box11(box11))
box12.trace("w",lambda name,index,mode,box12=box12:clicked_box12(box12))
box13.trace("w",lambda name,index,mode,box13=box13:clicked_box13(box13))
box14.trace("w",lambda name,index,mode,box14=box14:clicked_box14(box14))
box15.trace("w",lambda name,index,mode,box15=box15:clicked_box15(box15))
box16.trace("w",lambda name,index,mode,box16=box16:clicked_box16(box16))
box17.trace("w",lambda name,index,mode,box17=box17:clicked_box17(box17))
box18.trace("w",lambda name,index,mode,box18=box18:clicked_box18(box18))

box19.trace("w",lambda name,index,mode,box19=box19:clicked_box19(box19))
box20.trace("w",lambda name,index,mode,box20=box20:clicked_box20(box20))
box21.trace("w",lambda name,index,mode,box21=box21:clicked_box21(box21))
box22.trace("w",lambda name,index,mode,box22=box22:clicked_box22(box22))
box23.trace("w",lambda name,index,mode,box23=box23:clicked_box23(box23))
box24.trace("w",lambda name,index,mode,box24=box24:clicked_box24(box24))
box25.trace("w",lambda name,index,mode,box25=box25:clicked_box25(box25))
box26.trace("w",lambda name,index,mode,box26=box26:clicked_box26(box26))
box27.trace("w",lambda name,index,mode,box27=box27:clicked_box27(box27))

box28.trace("w",lambda name,index,mode,box28=box28:clicked_box28(box28))
box29.trace("w",lambda name,index,mode,box29=box29:clicked_box29(box29))
box30.trace("w",lambda name,index,mode,box30=box30:clicked_box30(box30))
box31.trace("w",lambda name,index,mode,box31=box31:clicked_box31(box31))
box32.trace("w",lambda name,index,mode,box32=box32:clicked_box32(box32))
box33.trace("w",lambda name,index,mode,box33=box33:clicked_box33(box33))
box34.trace("w",lambda name,index,mode,box34=box34:clicked_box34(box34))
box35.trace("w",lambda name,index,mode,box35=box35:clicked_box35(box35))
box36.trace("w",lambda name,index,mode,box36=box36:clicked_box36(box36))

box37.trace("w",lambda name,index,mode,box37=box37:clicked_box37(box37))
box38.trace("w",lambda name,index,mode,box38=box38:clicked_box38(box38))
box39.trace("w",lambda name,index,mode,box39=box39:clicked_box39(box39))
box40.trace("w",lambda name,index,mode,box40=box40:clicked_box40(box40))
box41.trace("w",lambda name,index,mode,box41=box41:clicked_box41(box41))
box42.trace("w",lambda name,index,mode,box42=box42:clicked_box42(box42))
box43.trace("w",lambda name,index,mode,box43=box43:clicked_box43(box43))
box44.trace("w",lambda name,index,mode,box44=box44:clicked_box44(box44))
box45.trace("w",lambda name,index,mode,box45=box45:clicked_box45(box45))

box46.trace("w",lambda name,index,mode,box46=box46:clicked_box46(box46))
box47.trace("w",lambda name,index,mode,box47=box47:clicked_box47(box47))
box48.trace("w",lambda name,index,mode,box48=box48:clicked_box48(box48))
box49.trace("w",lambda name,index,mode,box49=box49:clicked_box49(box49))
box50.trace("w",lambda name,index,mode,box50=box50:clicked_box50(box50))
box51.trace("w",lambda name,index,mode,box51=box51:clicked_box51(box51))
box52.trace("w",lambda name,index,mode,box52=box52:clicked_box52(box52))
box53.trace("w",lambda name,index,mode,box53=box53:clicked_box53(box53))
box54.trace("w",lambda name,index,mode,box54=box54:clicked_box54(box54))

box55.trace("w",lambda name,index,mode,box55=box55:clicked_box55(box55))
box56.trace("w",lambda name,index,mode,box56=box56:clicked_box56(box56))
box57.trace("w",lambda name,index,mode,box57=box57:clicked_box57(box57))
box58.trace("w",lambda name,index,mode,box58=box58:clicked_box58(box58))
box59.trace("w",lambda name,index,mode,box59=box59:clicked_box59(box59))
box60.trace("w",lambda name,index,mode,box60=box60:clicked_box60(box60))
box61.trace("w",lambda name,index,mode,box61=box61:clicked_box61(box61))
box62.trace("w",lambda name,index,mode,box62=box62:clicked_box62(box62))
box63.trace("w",lambda name,index,mode,box63=box63:clicked_box63(box63))

box64.trace("w",lambda name,index,mode,box64=box64:clicked_box64(box64))
box65.trace("w",lambda name,index,mode,box65=box65:clicked_box65(box65))
box66.trace("w",lambda name,index,mode,box66=box66:clicked_box66(box66))
box67.trace("w",lambda name,index,mode,box67=box67:clicked_box67(box67))
box68.trace("w",lambda name,index,mode,box68=box68:clicked_box68(box68))
box69.trace("w",lambda name,index,mode,box69=box69:clicked_box69(box69))
box70.trace("w",lambda name,index,mode,box70=box70:clicked_box70(box70))
box71.trace("w",lambda name,index,mode,box71=box71:clicked_box71(box71))
box72.trace("w",lambda name,index,mode,box72=box72:clicked_box72(box72))

box73.trace("w",lambda name,index,mode,box73=box73:clicked_box73(box73))
box74.trace("w",lambda name,index,mode,box74=box74:clicked_box74(box74))
box75.trace("w",lambda name,index,mode,box75=box75:clicked_box75(box75))
box76.trace("w",lambda name,index,mode,box76=box76:clicked_box76(box76))
box77.trace("w",lambda name,index,mode,box77=box77:clicked_box77(box77))
box78.trace("w",lambda name,index,mode,box78=box78:clicked_box78(box78))
box79.trace("w",lambda name,index,mode,box79=box79:clicked_box79(box79))
box80.trace("w",lambda name,index,mode,box80=box80:clicked_box80(box80))
box81.trace("w",lambda name,index,mode,box81=box81:clicked_box81(box81))

timer = tkinter.Label(root,text="15:00")

solve_Partial = tkinter.Button(root,text="Slove Partial",command=solve,height=3,width=15,relief="solid",font=font_size)

quit_btn = tkinter.Button(root,text="Quit",command=quit_option,height=3,width=15,relief="solid",font=font_size)

restart_btn = tkinter.Button(root,text="Restart",command=restart,height=3,width=15,relief="solid",font=font_size)

#Placing Cells in Grid

cell1.grid(row=0,column=0)
cell2.grid(row=0,column=1)
cell3.grid(row=0,column=2)
cell4.grid(row=1,column=0)
cell5.grid(row=1,column=1)
cell6.grid(row=1,column=2)
cell7.grid(row=2,column=0)
cell8.grid(row=2,column=1)
cell9.grid(row=2,column=2)

cell10.grid(row=0,column=3)
cell11.grid(row=0,column=4)
cell12.grid(row=0,column=5)
cell13.grid(row=1,column=3)
cell14.grid(row=1,column=4)
cell15.grid(row=1,column=5)
cell16.grid(row=2,column=3)
cell17.grid(row=2,column=4)
cell18.grid(row=2,column=5)

cell19.grid(row=0,column=6)
cell20.grid(row=0,column=7)
cell21.grid(row=0,column=8)
cell22.grid(row=1,column=6)
cell23.grid(row=1,column=7)
cell24.grid(row=1,column=8)
cell25.grid(row=2,column=6)
cell26.grid(row=2,column=7)
cell27.grid(row=2,column=8)

cell28.grid(row=3,column=0)
cell29.grid(row=3,column=1)
cell30.grid(row=3,column=2)
cell31.grid(row=4,column=0)
cell32.grid(row=4,column=1)
cell33.grid(row=4,column=2)
cell34.grid(row=5,column=0)
cell35.grid(row=5,column=1)
cell36.grid(row=5,column=2)

cell37.grid(row=3,column=3)
cell38.grid(row=3,column=4)
cell39.grid(row=3,column=5)
cell40.grid(row=4,column=3)
cell41.grid(row=4,column=4)
cell42.grid(row=4,column=5)
cell43.grid(row=5,column=3)
cell44.grid(row=5,column=4)
cell45.grid(row=5,column=5)

cell46.grid(row=3,column=6)
cell47.grid(row=3,column=7)
cell48.grid(row=3,column=8)
cell49.grid(row=4,column=6)
cell50.grid(row=4,column=7)
cell51.grid(row=4,column=8)
cell52.grid(row=5,column=6)
cell53.grid(row=5,column=7)
cell54.grid(row=5,column=8)

cell55.grid(row=6,column=0)
cell56.grid(row=6,column=1)
cell57.grid(row=6,column=2)
cell58.grid(row=7,column=0)
cell59.grid(row=7,column=1)
cell60.grid(row=7,column=2)
cell61.grid(row=8,column=0)
cell62.grid(row=8,column=1)
cell63.grid(row=8,column=2)

cell64.grid(row=6,column=3)
cell65.grid(row=6,column=4)
cell66.grid(row=6,column=5)
cell67.grid(row=7,column=3)
cell68.grid(row=7,column=4)
cell69.grid(row=7,column=5)
cell70.grid(row=8,column=3)
cell71.grid(row=8,column=4)
cell72.grid(row=8,column=5)

cell73.grid(row=6,column=6)
cell74.grid(row=6,column=7)
cell75.grid(row=6,column=8)
cell76.grid(row=7,column=6)
cell77.grid(row=7,column=7)
cell78.grid(row=7,column=8)
cell79.grid(row=8,column=6)
cell80.grid(row=8,column=7)
cell81.grid(row=8,column=8)


timer.grid(row=9,column=0,columnspan=8)

solve_Partial.grid(row=10,column=0,columnspan=3)
quit_btn.grid(row=10,column=6,columnspan=3)
restart_btn.grid(row=10,column=3,columnspan=3)

seconds = 60
minates = 14


#Generating Function



def timerFunction():
    global seconds,minates,timer,sudokutimer

    if(grid_length_function() == 80):
        messagebox.showinfo('Success','You have solved the puzzle')
        root.destroy()
        
    if(minates == 0 and seconds == 1):
        res = messagebox.askyesno('Game Over','Would you like to restart')
        if res:
            restart()
        else:
            pass
    else:
        if(seconds == 60):
            seconds = seconds - 1
            sudokutimer = str(minates) + ":" +str(seconds)
        elif(seconds == 1):
            minates = minates - 1
            seconds = 60
            sudokutimer = str(minates) + ":" +str(seconds)
        else:
            seconds = seconds - 1
            sudokutimer = str(minates) + ":" +str(seconds)
    
    timer.grid_forget()
    timer = tkinter.Label(root,text="Time Left : " + sudokutimer,bg="white",font=font_size)
    timer.grid(row=9,column=0,columnspan=8)
    root.after(1000,timerFunction)
    

timerFunction()


root.mainloop()