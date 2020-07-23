from tkinter import *
import tkinter.messagebox as box
import re
root = Tk()
root.title("Task 3 - Booking System")

root.A1 = Label(root, text="A1", bg="green")
root.A1.grid(column=1, row=1, sticky=W+E)
root.A2 = Label(root, text="A2", bg="green")
root.A2.grid(column=2, row=1, sticky=W+E )
root.A3 = Label(root, text="A3", bg="green")
root.A3.grid(column=3, row=1, sticky=W+E)
root.A4 = Label(root, text="A4", bg="red")
root.A4.grid(column=4, row=1, sticky=W+E)
root.A5 = Label(root, text="A5", bg="red")
root.A5.grid(column=5, row=1,sticky=W+E)
root.A6 = Label(root, text="A6", bg="green")
root.A6.grid(column=6, row=1,sticky=W+E)
root.A7 = Label(root, text="A7", bg="red")
root.A7.grid(column=7, row=1, sticky=W+E)  
root.A8 = Label(root, text="A8", bg="red")
root.A8.grid(column=8, row=1, sticky=W+E)
root.A9 = Label(root, text="A9", bg="red")
root.A9.grid(column=9, row=1, sticky=W+E)
root.A10 = Label(root, text="A10", bg="green")
root.A10.grid(column=10, row=1, sticky=W+E)

root.B1 = Label(root, text="B1", bg="red")
root.B1.grid(column=1, row=2, sticky=W+E)
root.B2 = Label(root, text="B2", bg="green")
root.B2.grid(column=2, row=2, sticky=W+E)
root.B3 = Label(root, text="B3", bg="green")
root.B3.grid(column=3, row=2, sticky=W+E)
root.B4  = Label(root, text="B4", bg="green")
root.B4.grid(column=4, row=2, sticky=W+E)
root.B5 = Label(root, text="B5", bg="green")
root.B5.grid(column=5, row=2, sticky=W+E)
root.B6 = Label(root, text="B6", bg="green")
root.B6.grid(column=6, row=2, sticky=W+E)
root.B7 = Label(root, text="B7", bg="green")
root.B7.grid(column=7, row=2, sticky=W+E)
root.B8 = Label(root, text="B8", bg="red")
root.B8.grid(column=8, row=2, sticky=W+E)
root.B9 = Label(root, text="B9", bg="red")
root.B9.grid(column=9, row=2, sticky=W+E)
root.B10 = Label(root, text="B10", bg="green")
root.B10.grid(column=10, row=2, sticky=W+E)

root.C1 = Label(root, text="C1", bg="green")
root.C1.grid(column=1, row=3, sticky=W+E)
root.C2 = Label(root, text="C2", bg="red")
root.C2.grid(column=2, row=3, sticky=W+E)
root.C3 = Label(root, text="C3", bg="red")
root.C3.grid(column=3, row=3, sticky=W+E)
root.C4 = Label(root, text="C4", bg="red")
root.C4.grid(column=4, row=3, sticky=W+E)
root.C5 = Label(root, text="C5", bg="green")
root.C5.grid(column=5, row=3, sticky=W+E)
root.C6 = Label(root, text="C6", bg="green")
root.C6.grid(column=6, row=3, sticky=W+E)
root.C7 = Label(root, text="C7", bg="green")
root.C7.grid(column=7, row=3, sticky=W+E)
root.C8 = Label(root, text="C8", bg="green")
root.C8.grid(column=8, row=3, sticky=W+E)
root.C9 = Label(root, text="C9", bg="green")
root.C9.grid(column=9, row=3, sticky=W+E)
root.C10 = Label(root, text="C10", bg="red")
root.C10.grid(column=10, row=3, sticky=W+E)

root.D1 = Label(root, text="D1", bg="red")
root.D1.grid(column=1, row=4, sticky=W+E)
root.D2 = Label(root, text="D2", bg="green")
root.D2.grid(column=2, row=4, sticky=W+E)
root.D3 = Label(root, text="D3", bg="green")
root.D3.grid(column=3, row=4, sticky=W+E)
root.D4 = Label(root, text="D4", bg="green")
root.D4.grid(column=4, row=4, sticky=W+E)
root.D5 = Label(root, text="D5", bg="red")
root.D5.grid(column=5, row=4, sticky=W+E)
root.D6 = Label(root, text="D6", bg="green")
root.D6.grid(column=6, row=4, sticky=W+E)
root.D7 = Label(root, text="D7", bg="green")
root.D7.grid(column=7, row=4, sticky=W+E)
root.D8 = Label(root, text="D8", bg="green")
root.D8.grid(column=8, row=4, sticky=W+E)
root.D9 = Label(root, text="D9", bg="red")
root.D9.grid(column=9, row=4, sticky=W+E)
root.D10 = Label(root, text="D10", bg="red")
root.D10.grid(column=10, row=4, sticky=W+E)

root.E1 = Label(root, text="E1", bg="red")
root.E1.grid(column=1, row=5, sticky=W+E)
root.E2 = Label(root, text="E2", bg="green")
root.E2.grid(column=2, row=5, sticky=W+E)
root.E3 = Label(root, text="E3", bg="green")
root.E3.grid(column=3, row=5, sticky=W+E)
root.E4 = Label(root, text="E4", bg="red")
root.E4.grid(column=4, row=5, sticky=W+E)
root.E5 = Label(root, text="E5", bg="red")
root.E5.grid(column=5, row=5, sticky=W+E)
root.E6 = Label(root, text="E6", bg="red")
root.E6.grid(column=6, row=5, sticky=W+E)
root.E7 = Label(root, text="E7", bg="red")
root.E7.grid(column=7, row=5, sticky=W+E)
root.E8 = Label(root, text="E8", bg="red")
root.E8.grid(column=8, row=5, sticky=W+E)
root.E9 = Label(root, text="E9", bg="green")
root.E9.grid(column=9, row=5, sticky=W+E)
root.E10 = Label(root, text="E10", bg="red")
root.E10.grid(column=10, row=5, sticky=W+E)

rn = StringVar()
rn.set("1")
row_number = ["1","2","3","4","5","6"]

rl = StringVar()
rl.set("A")
row_letter = ["A","B","C","D","E"]

Label(root, text="Number of people in group:").grid(row=6, columnspan=7)
Label(root, text="Desired Row:").grid(row=7, columnspan=7)
OptionMenu(root, rn, *row_number).grid(row=6, column=11)
OptionMenu(root, rl, *row_letter).grid(row=7, column=11)

seats = ['0001101110','1000000110','0111000001','1000100011','1001111101'];

def checkseats():
  row_letter = rl.get()
  number = int(rn.get())
  row = seats[ord(row_letter.lower()) - 97]
  if number == (1):
      people = ("person") 
  else:
      people = ("people")
  if '0' * number in row:
    begin = row.index('0'*number)+1 
    if number > int(1):
      print (begin)
      box.showinfo("Available",("Seats available for {} people {}{}" " - {}{}").format(number,row_letter,begin,row_letter,begin+number-1))
    elif number == int(1):
      box.showinfo("Available",("Seat available at {}{}").format(row_letter,begin+number-1))
  elif '0' * number not in row:
    if row.count('0') == 1:
      box.showinfo("Unavailable",("A block of seats for {} "
            "people is not available in row {}. " "\n" "Only 1 "
            "seat is available in row {}. ").format(number,row_letter,row_letter)) 
    elif len(re.compile("(0+0)").findall(row)) == 0:
      free = row.count('0')
      box.showinfo("Unavailable",("A block of seats for {} "
            "people is not available in row {}. " "\n" "Only {} "
            "single seats are available in row {}. ").format(number,row_letter,free,row_letter))
    else:
      free = len(max(re.compile("(0+0)").findall(row)))
      box.showinfo("Unavailable",("A block of seats for {} "
            "people is not available in row {}. " "\n" "Only {} "
            "consecutive seats are available in row {}. ").format(number,row_letter,free,row_letter))

def colour():
  row_letter = str((rl.get()).upper())
  row = seats[ord(row_letter.lower()) - 97]
  row_count=1
  for i in row:
    if i == '1':
      col = str(row_count)
      print (row_letter+col)
      seat_no1 = (row_letter+col)
      seat_red = getattr(root, row_letter+col)
      seat_red.configure(bg="red")
      root.update()
    row_count = row_count+1
  if number > int(1):  
    box.showinfo("Booked",("Seats booked from {}{} " "- {}{}").format(row_letter,begin+1,row_letter,begin+number)) 
  else:
    box.showinfo("Booked",("Seat booked at {}{}").format(row_letter,begin+1))  

def bookseats():
  global seats
  global begin
  global number
  row_letter = rl.get()
  print (row_letter)
  number = int(rn.get())
  print (number)
  row = seats[ord(row_letter.lower()) - 97]
  if '0' * number not in row:
    box.showinfo("Unavailable",("You cannot book these seats!"))
  elif '0' * number in row:
    begin = row.index('0'*number)
    print (begin)
    end = begin+number
    print (end)
    new_row = (row[0:begin] + ('1' * number) + row[end:len(row)])
    print(new_row)
    seats = [seat.replace(row,new_row)for seat in seats]
    print (seats)
    colour() 

Button(root, text='Check', command=checkseats).grid(row=8, columnspan=11)
Button(root, text='Book Seats', command=bookseats).grid(row=9, columnspan=11)
root.mainloop()
