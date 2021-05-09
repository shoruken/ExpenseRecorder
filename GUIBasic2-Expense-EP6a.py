# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

#  GUI -- Tab1-F1-L1-E1 -- Tab2-F2-L2-E2
GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Uncle Engineer')
GUI.geometry('800x800+500+50')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

###############   MENU BAR   ###################
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

def About():
	messagebox.showinfo('About','Donate 1 BTC Address: xxxx')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

def Donate():
	messagebox.showinfo('Donate','BTC Address: xxxxxxxxxxxxxxxxxxxx')

donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)
#################################################

Tab = ttk.Notebook(GUI)     # Tab เรียกว่า Notebook
T1 = Frame(Tab)
T2 = Frame(Tab)
#T3 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='t1.png') #  .subsample(2) = ย่อรูป  , ใส่รูป
icon_t2 = PhotoImage(file='t2.png')
#icon_t3 = PhotoImage(file='t3.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')
#Tab.add(T3, text=f'{"ทดสอบ":^{30}}',image=icon_t3,compound='top')

F1 = Frame(T1)
F2 = Frame(T2)
#F1.place(x=100,y=50)
F1.pack()
F2.pack()

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showwarning('Error','กรุณากรอกราคา')
		return
	elif quantity == '':
		quantity = 1

	total = float(price) * float(quantity)

	try:
		total = float(price) * float(quantity)
		# .get() คือดึงค่ามาจาก v_expense = StringVar()
		print('รายการ: {} ราคา: {}'.format(expense,price))
		print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
		text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
		text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [dt,expense,price,quantity,total]
			fw.writerow(data)

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		update_record()  ## tab2 info
		#table_info2()  ## tab2 table info
		update_table()

		E1.focus()
		
	except Exception as e:
		print('ERROR',e)
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

#------Image--------

main_icon = PhotoImage(file='wallet.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()


#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

icon_save = PhotoImage(file='save.png')

B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_save,compound='left',command=Save)
B2.pack(ipadx=50,ipady=10,pady=10)

# Result 
v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
# result = Label(F1, textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=20)


#######################  TAB2  #######################

###rs = []

def read_csv():
	###global rs
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
		#print(data) ...... all data [a,b,c,d,e] [a,b,c,d,e] [a,b,c,d,e]
		#print(data[0]) ........ first [a,b,c,d,e]
		#print(data[0][0]) ............[a]
		#print("{}\n ".format(data))
		#for a,b,c,d,e in data:
		#	print(a,b)
		###rs = data
	return data

###read_csv()
###print(rs)

def update_record():
	getdata = read_csv()
	#v_allrecord.set('')
	text2 = ''
	for d in getdata:
		#print(d)
		#text2 = print("{}\n ".format(d))
		text2 = text2 + '{}\n '.format(d)	
		#print(text2)
		b_result.set(text2)

############# show table #####################

def table_info():
	with open('savedata.csv',newline='',encoding='utf-8') as file:
		fr2 = csv.DictReader(file,delimiter=',')

		for row in fr2:
			a1 = row['Date']
			a2 = row['Item']
			a3 = row['Price']
			a4 = row['Amount']
			a5 = row['Total']
			my_tree.insert("", index='end', values=(a1, a2, a3, a4, a5))

def table_info2():
	data3 = read_csv()
	count = 0
	for ii in data3:
		my_tree.insert(parent="",index=count, iid=count, values = ii)
		count += 1



############# tab 2 #####################

#main_icon2 = PhotoImage(file='wallet.png')
#Mainicon2 = Label(F2,image=main_icon2)
#Mainicon2.pack()

L11 = ttk.Label(F2,text='Result',font=FONT1).pack()

b_result = StringVar()
result2 = ttk.Label(F2, textvariable=b_result,font=FONT1,foreground='green').pack()


header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()

#for c in range(len(header)):
#	resulttable.heading(header[c],text = header[c])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [150,170,80,80,80]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)
	
#resulttable.insert('',0,value=['Mon','Drink',30,4,120])
#resulttable.insert('','end',value=['Tue','Drink',30,4,120])

def update_table():
	resulttable.delete(*resulttable.get_children())
	# for g in resulttable.get_children():
	#	resulttable.delete(g)

	data = read_csv()
	#print(data)
	for d in data:
		resulttable.insert('',0,value=d)

update_table()
#print('GET CHILD:',resulttable.get_children())
#print('GET CHILD:',*resulttable.get_children())



# ---- Treeview -----
# Add some style
#style = ttk.Style()
# Pick a themes
#style.theme_use('default')
# Config style
#style.configure('Treeview',background='#FFFFFF',foreground='black',rowheight=25,fieldbackground='#FFFFFF')
#style.map('Treeview',background=[('selected', 'blue')])

'''
my_tree = ttk.Treeview(F2, selectmode='extended')
my_tree.pack(pady=20)
# define columns
my_tree['columns'] = ('วันที่','รายการ','ราคา','จำนวน','รวมยอด')
# format columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('วันที่', anchor=W, width=120)
my_tree.column('รายการ', anchor=W, width=120)
my_tree.column('ราคา', anchor=W, width=80)
my_tree.column('จำนวน', anchor=W, width=120)
my_tree.column('รวมยอด', anchor=W, width=120)
# Create Heading
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('วันที่', text='วันที่', anchor=W,)
my_tree.heading('รายการ', text='รายการ', anchor=W)
my_tree.heading('ราคา', text='ราคา', anchor=W)
my_tree.heading('จำนวน', text='จำนวน', anchor=W)
my_tree.heading('รวมยอด', text='รวมยอด', anchor=W)


icon_save = PhotoImage(file='save.png')
BB2 = ttk.Button(F2,text=f'{"Refresh": >{10}}',image=icon_save,compound='left',command=table_info2)
BB2.pack(ipadx=50,ipady=10,pady=10)
#tableinfo2()
'''

#

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
