'''
The code generates a UI based calculator which works
with on screen buttons and keyboard input as well.
It works with integer as well as float values.
The evaluation algorithm used in this code is infix to
postfix conversion followed by postfix evaluation.
'''

# Import the Tkinter package to create UI
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

# Initializing tkinter root window and font
root = tk.Tk()
root.title('Calculator')
font1 = font.Font(family="Times New Roman", size=15)

# Defining Class for calculator Frame
class Calculator(ttk.Frame):

	#Defining the Constructor
	def __init__(self, master):
		super().__init__(master)
		self.result = tk.StringVar()

		# Initializing UI Elements
		self.entry = ttk.Entry(self, font = font1)
		self.resultLabel = ttk.Label(self, font=font1, textvariable=self.result)
		buttoncalc = tk.Button(self, text = "=", font = font1, bg = 'black', fg = 'white', command = self.evaluate)
		buttonclr = tk.Button(self, text = "AC", font = font1, bg = 'black', fg = 'white', command = self.clear)
		buttonerase = tk.Button(self, text = "<-", font = font1, bg = 'black', fg = 'white', command = self.erase)
		button1 = tk.Button(self, text = "1", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(1))
		button2 = tk.Button(self, text = "2", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(2))
		button3 = tk.Button(self, text = "3", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(3))
		button4 = tk.Button(self, text = "4", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(4))
		button5 = tk.Button(self, text = "5", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(5))
		button6 = tk.Button(self, text = "6", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(6))
		button7 = tk.Button(self, text = "7", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(7))
		button8 = tk.Button(self, text = "8", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(8))
		button9 = tk.Button(self, text = "9", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(9))
		button0 = tk.Button(self, text = "0", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(0))
		buttonbop = tk.Button(self, text = "(", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('('))
		buttonbcl = tk.Button(self, text = ")", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(')'))
		buttonadd = tk.Button(self, text = "+", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('+'))
		buttonsub = tk.Button(self, text = "-", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('-'))
		buttonmul = tk.Button(self, text = "x", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('x'))
		buttondiv = tk.Button(self, text = "/", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('/'))
		buttonpow = tk.Button(self, text = "^", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('^'))
		buttondot = tk.Button(self, text = ".", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('.'))
		buttonper = tk.Button(self, text = "%", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('%'))
		buttonsqrt = tk.Button(self, text = "√", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('√'))

		# Arranging UI Elements using grid layout
		self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = "NSEW")
		self.resultLabel.grid(row = 1, column = 0, columnspan = 4, sticky = "NSEW")
		button1.grid(row = 2, column = 0, sticky = "NSEW")
		button2.grid(row = 2, column = 1, sticky = "NSEW")
		button3.grid(row = 2, column = 2, sticky = "NSEW")
		buttonclr.grid(row = 2, column = 3, sticky = "NSEW")
		button4.grid(row = 3, column = 0, sticky = "NSEW")
		button5.grid(row = 3, column = 1, sticky = "NSEW")
		button6.grid(row = 3, column = 2, sticky = "NSEW")
		buttonerase.grid(row = 3, column = 3, sticky = "NSEW")
		button7.grid(row = 4, column = 0, sticky = "NSEW")
		button8.grid(row = 4, column = 1, sticky = "NSEW")
		button9.grid(row = 4, column = 2, sticky = "NSEW")
		buttonadd.grid(row = 4, column = 3, sticky = "NSEW")
		buttondot.grid(row = 5, column = 0, sticky = "NSEW")
		button0.grid(row = 5, column = 1, sticky = "NSEW")
		buttonsqrt.grid(row = 5, column = 2, sticky = "NSEW")
		buttonsub.grid(row = 5, column = 3, sticky = "NSEW")
		buttonbop.grid(row = 6, column = 0, sticky = "NSEW")
		buttonbcl.grid(row = 6, column = 1, sticky = "NSEW")
		buttonpow.grid(row = 6, column = 2, sticky = "NSEW")
		buttondiv.grid(row = 6, column = 3, sticky = "NSEW")
		buttoncalc.grid(row = 7, column = 0, columnspan = 2, sticky = "NSEW")
		buttonper.grid(row = 7, column = 2, sticky = "NSEW")
		buttonmul.grid(row = 7, column = 3, sticky = "NSEW")

		# Binding the Enter key to Evaluate function
		master.bind('<Return>', self.evaluate)

	# Method that returns precedence of operators
	def precedence(self, oper):
		if oper == '+' or oper == '-':
			return 1
		if oper == 'x' or oper == '/' or oper == '%':
			return 2
		if oper == '^' or oper == '√':
			return 3

	# Method to check if a string/substring is float
	def isFloat(self, str):
		try:
			float(str)
			return True
		except:
			return False
	
	# This method converts the string to postfix and then evaluates the postfix expression
	def evaluate(self, *args):
		try:

			# Initialization of variables
			stack = []
			postfix = ''
			brackets = ['(', '[', '{']
			operators = ['-', '+', 'x', '/', '^', '√']
			expression = str(self.entry.get())
			i = 0

			# Loop to iterate through the infix string
			while i < len(expression):

				# If element is space, skip it
				if expression[i] == ' ':
					pass

				# If element is a digit, copy it to postfix string
				elif expression[i].isnumeric() or expression[i] == '.':
					postfix += expression[i]

				# If it is an operator...
				else:

					# Add a space to separate the numeric elements
					if postfix[-1] != ' ':
						postfix += ' '

					# If the stack is empty, or if the element or the top element of stack is an open bracket, insert the operator on stack
					if len(stack) == 0 or expression[i] in brackets or stack[-1] in brackets:
						stack.append(expression[i])

					# If it is closing bracket, pop all the elements till the opening bracket
					elif expression[i] == ')':
						while stack[-1] != '(':
							postfix += stack.pop() + ' '
						stack.pop()
					elif expression[i] == '}':
						while stack[-1] != '{':
							postfix += stack.pop() + ' '
						stack.pop()
					elif expression[i] == ']':
						while stack[-1] != '[':
							postfix += stack.pop() + ' '
						stack.pop()

					# If precedence of element is greater than precedence of top element of stack, append it
					elif self.precedence(expression[i]) > self.precedence(stack[-1]):
						stack.append(expression[i])

					# Else pop elements till precedence of top element is greater or equal than the new element then push the new element
					# Additionally check for any brackets encountered or if the stack gets empty
					else:
						while len(stack) != 0 and stack[-1] not in brackets and self.precedence(expression[i]) <= self.precedence(stack[-1]):
							postfix += stack.pop() + ' '
						stack.append(expression[i])
				
				# Increment Loop Counter Variable
				i += 1

			# Pop all the elements of stack and place in the postfix string
			while len(stack) != 0:
				if postfix[-1] != ' ':
					postfix += ' '
				postfix += stack.pop()
			postfix = postfix.split()

			# Initialize an empty stack for evaluating postfix expression
			stack = []

			# Loop to iterate through the postfix expression
			for elem in postfix:

				# If the element is integer or float, push it to the stack
				if elem.isnumeric() or self.isFloat(elem):
					stack.append(float(elem))

				# If it is an operator...
				else:

					# Pop the top two elements of stack
					b = stack.pop()
					a = stack.pop()

					# Perform the necessary arithmetic operation and push the result back into the stack
					if elem == '+':
						stack.append(a + b)
					elif elem == '-':
						stack.append(a - b)
					elif elem == 'x':
						stack.append(a * b)
					elif elem == '/':
						stack.append(a / b)
					elif elem == '%':
						stack.append(int(a) % int(b))
					elif elem == '^':
						stack.append(a ** b)
					elif elem == '√':
						stack.append(b ** (1/a))
			
			# If the final value does not have fractional part, typecast it to integer
			if stack[-1] == int(stack[-1]):
				stack[-1] = int(stack[-1])

			# Check if '=' button is pressed
			# If yes, copy the result into the entry field
			# If not, copy the result to the result label
			if len(args) == 1:
				self.result.set(str(stack[-1]))
			else:
				self.entry.delete(0, 99)
				self.entry.insert(0, str(stack[-1]))
				self.result.set('')

		# If any errors encountered, empty the result label
		except:
			if len(args) == 0:
				self.result.set('Invalid Expression')
			else:
				self.result.set('')

	# Method to clear the Entry Field
	def clear(self):
		self.entry.delete(0, 99)
		self.result.set('')

	# Method to update content on Entry Field
	def update(self, char):
		temp = len(str(self.entry.get()))
		self.entry.insert(temp, str(char))
		self.evaluate(1)

	# Method to erase last element of Entry Field
	def erase(self):
		temp = len(str(self.entry.get()))
		self.entry.delete(temp - 1)
		self.evaluate(1)

# Declare an object of Calculator Class and display it on root window
calculator = Calculator(root)
calculator.grid(row = 0, column = 0)

# Keep the root window running till program is closed
root.mainloop()