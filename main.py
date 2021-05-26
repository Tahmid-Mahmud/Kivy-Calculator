from kivymd.app import MDApp
#from kivy.core.window import Window
from kivymd.uix.picker import *
from kivy.lang import Builder
from kivymd.uix.button import *
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock


KV='''
ScreenManager:
	id:scr_mng
	Screen:
		name:'calc'
		BoxLayout:
			orientation:'vertical'
			MDToolbar:
				title:'Calculator'
				elevation:9
			BoxLayout:
				size_hint_y:.48
				TextInput:
					padding:'10dp'
					id:result
					halign:'right'
					readonly:True
					text:'0'
					font_size:'30dp'
					background_normal: 'white.png'
					
					
			MDGridLayout:
				md_bg_color:[20/255.0,20/255.0,20/255.0,1]
				spacing:'7dp'
				cols:4
				Button:
					id:btn1
					text:'AC'
					font_size:'30dp'
					on_press:app.clear()
				Button:
					id:btn2
					text:u'\u00AB'
					font_size:'30dp'
					on_press:app.remove()
					
				Button:
					id:btn3
					text:u'\u039E'
					font_size:'30dp'
					on_press:
						scr_mng.current='about'
				Button:
					id:btn4
					text:'÷'
					font_size:'30dp'
					on_press:app.show(self.text)
				
				Button:
					id:btn5
					text:'7'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn6
					text:'8'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn7
					text:'9'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn8
					text:'×'
					font_size:'30dp'
					on_press:app.show(self.text)
					
				Button:
					id:btn9
					text:'4'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn10
					text:'5'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn11
					text:'6'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn12
					text:'-'
					font_size:'30dp'
					on_press:app.show(self.text)
				
					
				Button:
					id:btn13
					text:'3'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn14
					text:'2'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn15
					text:'1'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn16
					text:'+'
					font_size:'30dp'
					on_press:app.show(self.text)
				
					
				BoxLayout:
					Button:
						id:btn17
						text:'('
						font_size:'30dp'
						background_color:(180/255,180/255,180/255,1)
						on_press:app.br(self.text)
					Button:
						id:btn18
						text:')'
						font_size:'30dp'
						background_color:(180/255,180/255,180/255,1)
						on_press:app.br(self.text)
							
					
				Button:
					id:btn19
					text:'0'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.show(self.text)
				Button:
					id:btn20
					text:'.'
					font_size:'30dp'
					background_color:(180/255,180/255,180/255,1)
					on_press:app.dot()
				Button:
					id:btn21
					text:'='
					font_size:'30dp'
					on_press:app.calculate()
					
	Screen:
		name:'about'
		BoxLayout:
			orientation:'vertical'
			spacing:'10dp'
			MDToolbar:
				title:'About this App'
				left_action_items:[['calculator-variant',lambda x:x]]

				
				elevation:9
			BoxLayout:
				orientation:'vertical'
				spacing:'20dp'
				padding:'7dp'
				MDLabel:
					id:abtext
					text:'This is a very simple calculator app, specially for simple calculation.'
					font_style:'H6'
					size_hint_y:None
					height:self.texture_size[1]
					
				MDRectangleFlatIconButton:
					icon:'information'
					text:'More info'
					pos_hint:{'center_x':.5,'center_y':1}
					on_release:
						app.info()
					
				#MDRectangleFlatIconButton:
#					icon:'alert'
#					text:'Warnings'
#					pos_hint:{'center_x':.5,'center_y':1}
#					on_release:
#						app.warnings()
						
				MDFillRoundFlatIconButton:
					icon:'format-color-fill'
					text:'Theme picker'
					pos_hint:{'center_x':.5,'center_y':1}
					on_release:
						app.show_thm()
					
				MDFillRoundFlatIconButton:
					icon:'calculator'
					text:'Back to Calculator'
					pos_hint:{'center_x':.5,'center_y':1}
					on_release:
						scr_mng.current='calc'
					
				ScrollView:
											
'''

class Calculator(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Red'
		return Builder.load_string(KV)
		
	def on_start(self):
		thm_check=Clock.schedule_interval(self.thm_check,0.01)
		self.integer=True
		self.number=''
		self.main=self.root.ids.result
		self.ptext=True
		
		
	def thm_check(self,*args):
		print(self.theme_cls.primary_palette)
		if self.theme_cls.theme_style=='Dark':
			self.theme_cls.theme_style='Light'
			toast('Sorry Dark theme is not available')
		
		self.font()
	
	def show(self,the_text):
		self.number+=the_text
		checks1=[
		the_text=='+',
		the_text=='-',
		the_text=='×',
		the_text=='÷']
		
		checks2=[
		self.main.text.endswith('+'),
		self.main.text.endswith('-'),
		self.main.text.endswith('×'),
		self.main.text.endswith('÷')]
		
		checks3=[
		'+' in self.number,
		'-' in self.number,
		'×' in self.number,
		'÷' in self.number
		]
		
		if self.ptext==False:
			the_text=''
			toast('Not more than 90 characters at a time')
		else:
			pass
		
		
		if any(checks1) and self.main.text.endswith('.'):
			self.main.text+='0'
		else:
			pass
			
		if any(checks2) and the_text=='-':
			the_text='(-'
			
		if self.main.text=='0' or self.main.text=='Error' or self.main.text=='infinity':
			self.main.text=''
			self.main.text+=the_text
			
		else:
			self.main.text+=the_text
			
		if any(checks3):
			print(self.number)
			self.number=self.number[:-1]
			self.number=''
		
		
			
	def remove(self):
		entry=self.main.text
		if len(entry)>1:
			entry=entry[:-1]
			self.number=self.number[:-1]
			self.main.text=entry
		else:
			self.main.text='0'
			self.number=''
			
			
	def clear(self):
		self.main.text='0'
		self.number=''
		
	def br(self,sign):
		if self.main.text=='0':
			self.main.text=''
			self.main.text=self.main.text+sign
		else:
			self.main.text=self.main.text+sign
			
	def dot(self):
		if '.' in self.number:
			pass
		else:
			if self.number=='' and self.main.text!='0':
				self.main.text+='0.'
				self.number+='.'
			else:
				self.main.text+='.'
				self.number+='.'
				
	
	def calculate(self):
		entry=self.main.text
		
		if '.' in entry:
			self.integer=False
		
		if '×' in entry:
			entry=entry.replace('×','*')
			
		try:
			if '÷' in entry:
				check=entry.replace('÷','%')
				if eval(check)!=0:
					self.integer=False
				else:
					self.integer=True
				entry=entry.replace('÷','/')
					
		except:
				self.main.text='Error'	
				
				
		try:
			if self.integer==False:
				preans=float(eval(entry))
				answer=round(preans,14)
					
				self.integer=True
					
			else:
				answer=int(eval(entry))
			if int(answer)>999999999:
				try:
					answer=format(answer,'e')
				except:
					answer='infinity'
			
			else:
				pass
				
			self.main.text=str(answer)
			self.main.text=str(answer)
			self.number=str(answer)
			
		except Exception as msg:
			self.main.text=str('Error')
		
	def info(self):
		self.dlog=MDDialog(title='More Info',text="This is a very simple Calculator App made with kivy and kivy material design (kivymd). This is a very primary Calculator App, specially for simple calculations.\n\nCopyright © www.learntocode.com || All rights reserved!",size_hint_x=0.9,auto_dismiss=False,
		buttons=[MDFlatButton(text='OK',on_release=self.bck)])
		self.dlog.open()
	
		
	def warnings(self):
		self.dlog=MDDialog(title='Warnings',text="1.  Inspite of our trying, there are still remaining some calculation problems.\n\n2.  Always try to write valid syntax, this will made the app run smoothly.\n\n3.  Very large calculation which is out math range can be the cause of crash of this app.\n\n4.  An unclosed bracket can show an error!\n\n5.  Copy paste system is not well organized here.",size_hint_x=0.83,auto_dismiss=False,
		buttons=[MDRectangleFlatButton(text='Got it',on_release=self.bck)])
		self.dlog.open()
	
	def bck(self,obj):
		self.dlog.dismiss()
		
	def show_thm(self):
		MDThemePicker().open()
	
	def font(self):
		if len(self.main.text)>=60:
				self.main.font_size='24dp'
				self.ptext=True
				
		else:
			self.main.font_size='30dp'
			self.ptext=True
			
		if len(self.main.text)>=90:
			self.ptext=False
		
	
Calculator().run()