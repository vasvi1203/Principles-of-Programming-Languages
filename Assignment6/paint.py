from tkinter import *
from tkinter import ttk
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab
import tkinter as tk




class Paint(object):
	def __init__(self, root):
		self.root = root
		self.root.title("Paint")
		self.width_value = self.root.winfo_screenwidth()
		self.height_value = self.root.winfo_screenheight()
		self.root.geometry("900x700")
		self.root.configure(background = 'white')
		#self.root.resizable(0, 0)
		self.pen_color = "black"
		self.eraser_color = "white"
		self.save_color = "black"
		self.old_x = None
		self.old_y = None
		self.stack = []
		self.line_stack = []
		self.item = None
		self.choice = "    Pencil"
		self.add_widgets()

	def add_widgets(self):
		#self.controls.grid(row = 0, column = 0, sticky=NE)
		self.color_frame = Frame(self.root, bd = 1, relief = RIDGE, bg = "white")
		#self.color_frame.place(x = 0, y = 0, width = 185, height = 70)
		self.color_frame.grid(sticky = NW, row = 0, column = 0, padx = 15, pady = 10)
		self.color_frame.config(cursor = "hand2")
		#self.color_frame.pack()
		
		self.palette_image = PhotoImage(file = 'paint.png')
		self.palette_button = Button(self.root, image = self.palette_image, command = self.select_palette_color)
		#self.canvas_button.place(x = 247, y = 0)
		self.palette_button.grid(sticky="W", row = 0, column = 1, padx = 10, pady = 10)
		self.palette_button.config(cursor = "hand2")
		self.palette_tooltip = CreateToolTip(self.palette_button, 'Select a color from the color palette')

		colors = ['black', 'white', '#4d4d4d', 'grey', '#990033', '#993300', 'red', 'pink', 'orange', '#ffcc99', 'yellow', '#ffff99', 'lime', '#d9ffb3', 'green', '#88cc00', '#0099ff', 'turquoise', '#3333ff', '#6699cc', 'purple', '#bfbff2']
		i = j = 0
		for color in colors:
			Button(self.color_frame, bg = color, bd = 2, relief = RIDGE, height = 1, width = 3, command = lambda col = color:self.select_color(col)).grid(row = i, column = j)
			i += 1
			if i == 2:
				i = 0
				j += 1

		self.pencil_image = PhotoImage(file = 'pencil.png')
		self.pencil_button = Button(self.root, image = self.pencil_image, command = self.pencil)
		#self.pencil.place(x = 0, y = 187)
		self.pencil_button.grid(sticky="W", row = 1, column = 0, padx = 16)
		self.pencil_button.config(cursor = "hand2")
		self.pencil_tooltip = CreateToolTip(self.pencil_button, 'Pencil')

		self.bg_image = PhotoImage(file = 'bg.png')
		self.bg_button = Button(self.root, image = self.bg_image, command = self.bg_color)
		self.bg_button.grid(sticky="W", row = 2, column = 0, padx = 16)
		self.bg_button.config(cursor = "hand2")
		self.bg_tooltip = CreateToolTip(self.bg_button, 'Change background color')

		self.eraser_image = PhotoImage(file = 'eraser.png')
		self.eraser_button = Button(self.root, image = self.eraser_image, command = self.eraser)
		#self.eraser.place(x = 0, y = 187)
		self.eraser_button.grid(sticky="W", row = 3, column = 0, padx = 16)
		self.eraser_button.config(cursor = "hand2")
		self.eraser_tooltip = CreateToolTip(self.eraser_button, 'Eraser')

		self.clear_image = PhotoImage(file = 'clear.png')
		self.clear_button = Button(self.root, image = self.clear_image, command = self.clear)
		#self.clear.place(x = 0, y = 217)
		self.clear_button.grid(sticky = "W", row = 4, column = 0, padx = 16)
		self.clear_button.config(cursor = "hand2")
		self.clear_tooltip = CreateToolTip(self.clear_button, 'Clear the canvas area')

		self.line_image = PhotoImage(file = 'line.png')
		self.line_button = Button(self.root, image = self.line_image, command = self.line)
		#self.line.place(x = 0, y = 367)
		self.line_button.grid(sticky="W", row = 5, column = 0, padx = 16)
		self.line_button.config(cursor = "hand2")
		self.line_tooltip = CreateToolTip(self.line_button, 'Draw a line')

		self.arrow_image = PhotoImage(file = 'arrow.png')
		self.arrow_button = Button(self.root, image = self.arrow_image, command = self.arrow)
		#self.line.place(x = 0, y = 367)
		self.arrow_button.grid(sticky="W", row = 6, column = 0, padx = 16)
		self.arrow_button.config(cursor = "hand2")
		self.arrow_tooltip = CreateToolTip(self.arrow_button, 'Draw an arrow')

		self.rectangle_image = PhotoImage(file = 'rectangle.png')
		self.rectangle_button = Button(self.root, image = self.rectangle_image, command = self.rectangle)
		#self.rectangle.place(x = 0, y = 307)
		self.rectangle_button.grid(sticky="W", row = 7, column = 0, padx = 16)
		self.rectangle_button.config(cursor = "hand2")
		self.rectangle_tooltip = CreateToolTip(self.rectangle_button, 'Draw a rectangle')

		self.oval_image = PhotoImage(file = 'oval.png')
		self.oval_button = Button(self.root, image = self.oval_image, command = self.oval)
		#self.oval.place(x = 0, y = 397)
		self.oval_button.grid(sticky="W", row = 8, column = 0, padx = 16)
		self.oval_button.config(cursor = "hand2")
		self.oval_tooltip = CreateToolTip(self.oval_button, 'Draw an oval/a circle')

		self.undo_image = PhotoImage(file = 'undo.png')
		self.undo_button = Button(self.root, image = self.undo_image, command = self.undo)
		#self.oval.place(x = 0, y = 397)
		self.undo_button.grid(sticky="W", row = 9, column = 0, padx = 16)
		self.undo_button.config(cursor = "hand2")
		self.undo_tooltip = CreateToolTip(self.undo_button, 'Undo')

		# creating a scale for pen and eraser size
		self.slider = Frame(self.root, bd = 3, bg = "white", relief = RIDGE)
		#self.slider.place(x = 0, y = 400)
		self.slider.grid(sticky="W", row = 10, column = 0, padx = 16, pady = 20)
		self.pen_size = Scale(self.slider, orient = VERTICAL, from_ = 50, to = 0, length = 170)
		self.pen_size.set(1)
		self.pen_size.grid(sticky="W", row = 10, column = 0, ipadx = 2, padx = 7, pady = 7)
		self.slider.config(cursor = "hand2")
		self.slider_tooltip = CreateToolTip(self.slider, 'Size')

		# creating canvas
		self.canvas = Canvas(self.root, relief = GROOVE, height = self.height_value, width = self.width_value, bg = "white")
		self.canvas.place(x = 70, y = 75)
		# self.canvas.grid(row = 0, column = 1)
		
		# bind the canvas with mouse drag
		self.canvas.bind('<B1-Motion>', self.paint) 
		self.canvas.bind('<ButtonRelease-1>', self.reset)
		
		self.msg = Message(self.root, text = self.choice, width = 70, bg = "white")
		self.msg.grid(sticky = "W", row = 11, column = 0)
		
		menu = Menu(self.root)
		self.root.config(menu = menu)
		filemenu = Menu(menu)
		colormenu = Menu(menu)
		menu.add_cascade(label = 'File', menu = filemenu)
		filemenu.add_command(label = 'Save File', command = self.save_file)
		optionmenu = Menu(menu)
		menu.add_cascade(label = 'Options', menu = optionmenu)
		optionmenu.add_command(label = 'Exit', command = self.root.destroy) 

	# functions
	def change_label(self):
		self.msg.config(text = self.choice)

	def paint(self, event):
		if self.old_x and self.old_y:
			self.line_stack.append(self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = self.pen_size.get(), fill = self.pen_color, capstyle=ROUND, smooth=True))
		
		self.oldx = self.old_x
		self.oldy = self.old_y			
		self.old_x = event.x
		self.old_y = event.y
		self.newx = event.x
		self.newy = event.y
		
	def reset(self, event):		# reset x and y 
		# self.line_stack.append(self.canvas.create_line(self.oldx, self.oldy, self.newx, self.newy, arrow = 'last', width = self.pen_size.get(), fill = self.pen_color, capstyle=ROUND, smooth=True))
		self.old_x = None
		self.old_y = None 
		self.line_stack.append('#')
		# print(self.line_stack)

	def select_color(self, col):
		self.pen_color = col
		self.save_color = col

	def eraser(self):
		self.pen_color = self.eraser_color
		self.canvas.bind('<B1-Motion>', self.paint) 
		self.canvas.bind('<ButtonRelease-1>', self.reset)
		self.canvas.config(cursor = "dot")
		self.choice = "    Eraser"
		self.change_label()

	def select_palette_color(self):
		self.choice = "   Palette"
		self.change_label()
		color = colorchooser.askcolor()
		self.pen_color = color[1]
		self.save_color = color[1]
		#self.canvas.configure(background = color[1])
		#self.eraser_color = color[1]

	def bg_color(self):
		self.canvas.configure(background = self.pen_color)
		self.eraser_color = self.pen_color
		self.choice = "   Canvas\n    Color"
		self.change_label()

	def clear(self):
		self.canvas.configure(background = "white")
		self.canvas.delete("all")

	def undo(self):
		try:
			if self.line_stack[-1] == '$':
				self.item = self.stack.pop()
				self.line_stack.pop()

			else:
				if self.line_stack[-1] == '#':
					self.item = self.line_stack.pop()
				while(1):
					if len(self.line_stack) == 0:
						break
					elif len(self.stack) != 0 or len(self.line_stack) != 0:
						# print(self.line_stack)
						if self.line_stack[-1] != '#' and self.line_stack[-1] != '$':
							self.item = self.line_stack.pop()
							self.canvas.delete(self.item)
						else:
							break
					else:
						break
			self.canvas.delete(self.item)

		except LookupError:
			print("LookupError: list index out of range")
		self.choice = "    Undo"
		self.change_label()

	def pencil(self):
		self.pen_color = self.save_color
		self.canvas.unbind("<Button-1>")
		self.canvas.unbind("<ButtonRelease-1>")
		self.canvas.unbind("<B1-Motion>")
		self.canvas.bind("<B1-Motion>", self.paint) 
		self.canvas.bind("<ButtonRelease-1>", self.reset)
		self.canvas.config(cursor = "pencil")
		self.choice = "    Pencil"
		self.change_label()

	def rectangle(self):
		self.rectx0 = 0
		self.recty0 = 0
		self.rectx1 = 0
		self.recty1 = 0
		self.rectid = None
		self.pen_color = self.save_color
		self.canvas.unbind("<Button-1>")
		self.canvas.unbind("<ButtonRelease-1>")
		self.canvas.unbind("<B1-Motion>")
		self.canvas.bind("<Button-1>", self.startRect)
		self.canvas.bind("<ButtonRelease-1>", self.stopRect)
		self.canvas.bind("<B1-Motion>", self.movingRect)
		self.canvas.config(cursor = "crosshair")
		self.choice = " Rectangle"
		self.change_label()

	def startRect(self, event):
		self.rectx0 = self.canvas.canvasx(event.x)
		self.recty0 = self.canvas.canvasy(event.y) 
		self.rectid = self.canvas.create_rectangle(self.rectx0, self.recty0, self.rectx0, self.recty0, outline = self.pen_color, width = self.pen_size.get())
		
	def movingRect(self, event):
		self.rectx1 = self.canvas.canvasx(event.x)
		self.recty1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.rectid, self.rectx0, self.recty0, self.rectx1, self.recty1)

	def stopRect(self, event):
		self.rectx1 = self.canvas.canvasx(event.x)
		self.recty1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.rectid, self.rectx0, self.recty0, self.rectx1, self.recty1)
		self.stack.append(self.rectid)
		self.line_stack.append('$')

	def line(self):
		self.linex0 = 0
		self.liney0 = 0
		self.linex1 = 0
		self.liney1 = 0
		self.lineid = None
		self.pen_color = self.save_color
		self.canvas.unbind("<Button-1>")
		self.canvas.unbind("<ButtonRelease-1>")
		self.canvas.unbind("<B1-Motion>")
		self.canvas.bind("<Button-1>", self.startLine)
		self.canvas.bind("<ButtonRelease-1>", self.stopLine)
		self.canvas.bind("<B1-Motion>", self.movingLine)
		self.canvas.config(cursor = "crosshair")
		self.choice = "     Line"
		self.change_label()

	def startLine(self, event):
		self.linex0 = self.canvas.canvasx(event.x)
		self.liney0 = self.canvas.canvasy(event.y) 
		self.lineid = self.canvas.create_line(self.linex0, self.liney0, self.linex0, self.liney0, fill = self.pen_color, width = self.pen_size.get())

	def movingLine(self, event):
		self.linex1 = self.canvas.canvasx(event.x)
		self.liney1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.lineid, self.linex0, self.liney0,self.linex1, self.liney1)
		
	def stopLine(self, event):
		self.linex1 = self.canvas.canvasx(event.x)
		self.liney1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.lineid, self.linex0, self.liney0,self.linex1, self.liney1)
		self.stack.append(self.lineid)
		self.line_stack.append('$')

	def arrow(self):
		self.arrowx0 = 0
		self.arrowy0 = 0
		self.arrowx1 = 0
		self.arrowy1 = 0
		self.arrowid = None
		self.pen_color = self.save_color
		self.canvas.unbind("<Button-1>")
		self.canvas.unbind("<ButtonRelease-1>")
		self.canvas.unbind("<B1-Motion>")
		self.canvas.bind("<Button-1>", self.startArrow)
		self.canvas.bind("<ButtonRelease-1>", self.stopArrow)
		self.canvas.bind("<B1-Motion>", self.movingArrow)
		self.canvas.config(cursor = "crosshair")
		self.choice = "     Arrow"
		self.change_label()

	def startArrow(self, event):
		self.arrowx0 = self.canvas.canvasx(event.x)
		self.arrowy0 = self.canvas.canvasy(event.y) 
		self.arrowid = self.canvas.create_line(self.arrowx0, self.arrowy0, self.arrowx0, self.arrowy0, arrow = 'last', fill = self.pen_color, width = self.pen_size.get())

	def movingArrow(self, event):
		self.arrowx1 = self.canvas.canvasx(event.x)
		self.arrowy1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.arrowid, self.arrowx0, self.arrowy0,self.arrowx1, self.arrowy1)

	def stopArrow(self, event):
		self.arrowx1 = self.canvas.canvasx(event.x)
		self.arrowy1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.arrowid, self.arrowx0, self.arrowy0,self.arrowx1, self.arrowy1)
		self.stack.append(self.arrowid)
		self.line_stack.append('$')

	def oval(self):
		self.ovalx0 = 0
		self.ovaly0 = 0
		self.ovalx1 = 0
		self.ovaly1 = 0
		self.ovalid = None
		self.pen_color = self.save_color
		self.canvas.unbind("<Button-1>")
		self.canvas.unbind("<ButtonRelease-1>")
		self.canvas.unbind("<B1-Motion>")
		self.canvas.bind("<Button-1>", self.startOval)
		self.canvas.bind("<ButtonRelease-1>", self.stopOval)
		self.canvas.bind("<B1-Motion>", self.movingOval)
		self.canvas.config(cursor = "crosshair")
		self.choice = "     Oval"
		self.change_label()
		
	def startOval(self, event):
		self.ovalx0 = self.canvas.canvasx(event.x)
		self.ovaly0 = self.canvas.canvasy(event.y) 
		self.ovalid = self.canvas.create_oval(self.ovalx0, self.ovaly0, self.ovalx0, self.ovaly0, outline = self.pen_color, width = self.pen_size.get())

	def movingOval(self, event):
		self.ovalx1 = self.canvas.canvasx(event.x)
		self.ovaly1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.ovalid, self.ovalx0, self.ovaly0,self.ovalx1, self.ovaly1)

	def stopOval(self, event):
		self.ovalx1 = self.canvas.canvasx(event.x)
		self.ovaly1 = self.canvas.canvasy(event.y)
		self.canvas.coords(self.ovalid, self.ovalx0, self.ovaly0,self.ovalx1, self.ovaly1)
		self.stack.append(self.ovalid)
		self.line_stack.append('$')

	def save_file(self):
		try:
			filename = filedialog.asksaveasfilename(defaultextension = '.png')
			'''x = self.root.winfo_rootx() + self.canvas.winfo_x()
			y = self.root.winfo_rooty() + self.canvas.winfo_y()
			x1 = x + self.canvas.winfo_width()
			y1 = y + self.canvas.winfo_height()'''
			ImageGrab.grab().save(filename)
			messagebox.showinfo('Paint', 'Image is saved as ' + str(filename))

		except:
			messagebox.showerror('Paint', 'Unable to save image!')

class CreateToolTip(object):
	def __init__(self, widget, text='widget info'):
		self.waittime = 500     #miliseconds
		self.wraplength = 180   #pixels
		self.widget = widget
		self.text = text
		self.widget.bind("<Enter>", self.enter)
		self.widget.bind("<Leave>", self.leave)
		self.widget.bind("<ButtonPress>", self.leave)
		self.id = None
		self.tw = None

	def enter(self, event=None):
		self.schedule()

	def leave(self, event=None):
		self.unschedule()
		self.hidetip()

	def schedule(self):
		self.unschedule()
		self.id = self.widget.after(self.waittime, self.showtip)

	def unschedule(self):
		id = self.id
		self.id = None
		if id:
			self.widget.after_cancel(id)

	def showtip(self, event=None):
		x = y = 0
		x, y, cx, cy = self.widget.bbox("insert")
		x += self.widget.winfo_rootx() + 55
		y += self.widget.winfo_rooty() + 20
		# creates a toplevel window
		self.tw = Toplevel(self.widget)
		# Leaves only the label and removes the app window
		self.tw.wm_overrideredirect(True)
		self.tw.wm_geometry("+%d+%d" % (x, y))
		label = Label(self.tw, text=self.text, justify='left', background="#ffffff", relief='solid', borderwidth=1, wraplength = self.wraplength)
		label.pack(ipadx=1)

	def hidetip(self):
		tw = self.tw
		self.tw= None
		if tw:
			tw.destroy()

if __name__ == "__main__":
	root = Tk()
	root.style = ttk.Style()
	root.style.theme_use('clam')
	p = Paint(root)
	root.mainloop()
