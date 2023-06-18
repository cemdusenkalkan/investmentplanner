import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style

style.use('ggplot')

class InvestmentApp:
    def __init__(self, root):

        root.title('Investment Planner')
        root.geometry('1200x800')
        root.configure(background='#d0d3d4')

        
        self.input_frame = ttk.Frame(root)
        self.input_frame.grid(column=2, row=0, padx=50, pady=50)
    
        ttk.Label(self.input_frame, text = "Monthly Contribution:", background='#d0d3d4', font=('Times New Roman', 14, 'bold')).grid(column = 0, row = 0)
        self.monthly_investment = tk.StringVar()
        ttk.Entry(self.input_frame, width = 20, textvariable = self.monthly_investment, font=('Times New Roman', 14)).grid(column = 0, row = 1)

        ttk.Label(self.input_frame, text = "Starting Amount:", background='#d0d3d4', font=('Times New Roman', 14, 'bold')).grid(column = 0, row = 2)
        self.start_amount = tk.StringVar()
        ttk.Entry(self.input_frame, width = 20, textvariable = self.start_amount, font=('Times New Roman', 14)).grid(column = 0, row = 3)

        ttk.Label(self.input_frame, text = "Expected Annual Return(%):", background='#d0d3d4', font=('Times New Roman', 14, 'bold')).grid(column = 0, row = 4)
        self.annual_return = tk.StringVar()
        ttk.Entry(self.input_frame, width = 20, textvariable = self.annual_return, font=('Times New Roman', 14)).grid(column = 0, row = 5)

        ttk.Label(self.input_frame, text = "Years of Saving:", background='#d0d3d4', font=('Times New Roman', 14, 'bold')).grid(column = 0, row = 6)
        self.years = tk.StringVar()
        ttk.Entry(self.input_frame, width = 20, textvariable = self.years, font=('Times New Roman', 14)).grid(column = 0, row = 7)

        ttk.Button(self.input_frame, text = "Calculate", command = self.calculate).grid(column = 0, row = 8)

        self.fig = Figure(figsize = (6, 6), dpi = 100) 
        self.canvas = FigureCanvasTkAgg(self.fig, master = root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column = 0, row = 0, rowspan=9, padx=50, pady=50)
       
        self.output_text = tk.StringVar()
        self.output_label = ttk.Label(root, textvariable=self.output_text, background='#d0d3d4', font=('Times New Roman', 14, 'bold'), wraplength=800)
        self.output_label.grid(column = 0, row = 10, padx=20, pady=20, columnspan=3)

    def calculate(self):

        P = float(self.monthly_investment.get())
        P0 = float(self.start_amount.get())
        r = float(self.annual_return.get()) / 100 / 12
        t = float(self.years.get()) * 12

        
        savings = [P0]
        for i in range(int(t)):
            savings.append(savings[-1]*(1 + r) + P)
     
        self.fig.clear()

        plot = self.fig.add_subplot(111)
        plot.plot(range(int(t) + 1), savings, color='skyblue')

        plot.set_title('Investment Planner', fontdict={'fontsize':14, 'fontweight':'bold', 'color':'#f49ac2', 'fontname':'Times New Roman'})
        plot.set_xlabel('Months', fontdict={'fontsize':12, 'fontweight':'bold', 'color':'#f49ac2', 'fontname':'Times New Roman'})
        plot.set_ylabel('Savings ($)', fontdict={'fontsize':12, 'fontweight':'bold', 'color':'#f49ac2', 'fontname':'Times New Roman'})

        self.canvas.draw()

        self.output_text.set(
            f"{self.years.get()} years of savings with a starting money of {self.start_amount.get()} dollars \nand monthly contribution of {self.monthly_investment.get()} dollars \nin return of {self.annual_return.get()}% per year will end up with {savings[-1]} dollars. Good Luck!"
        )

root = tk.Tk()
app = InvestmentApp(root)
root.mainloop()
