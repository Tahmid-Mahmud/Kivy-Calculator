from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import ILeftBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
import os, subprocess
from functools import partial

#0.2, 0.2, 0.7,0.7

KV='''
<ItemConfirm>
    on_release: root.set_icon(check)

    LeftCheckbox:
        id: check
        group: "check"
		on_active:app.font(root.text)


ScreenManager:
	MDScreen:
		name:'terminal'
		md_bg_color:(1,0,0,1)
		BoxLayout:
			id:layout
			orientation:'vertical'
			MDToolbar:
				id:tool
				title:'Terminal'
				md_bg_color: 1,1,1,1
				left_action_items:[['console-line',lambda x:x]]
				right_action_items:[['keyboard',lambda x:app.kboard()], ['ubuntu',lambda x:app.goto('ref')]]
			ScrollView:
				id:scrlv
				TextInput:
					id:console
					padding:('0dp', '7dp')
					font_size:'17dp'
					size_hint:(1, None)
					line_height:'5dp'
					height:max(self.minimum_height, scrlv.height)
					font_name:'E:\KivyProjects\PyTerminal\CONSOLA'
					readonly:True
					background_color: (0,0,0,1)
					foreground_color: (1,1,1,1)
					background_active: 'black.png'
					background_normal: 'black.png'
					
	MDScreen:
		name:'ref'
		BoxLayout:
			orientation:'vertical'
			MDToolbar:
				title:'Preference'
				md_bg_color:tool.md_bg_color
				left_action_items:[['arrow-left', lambda x:app.goto('terminal')]]
			ScrollView:
				MDList:
					TwoLineListItem:
						text:"Font size"
						secondary_text:"choose character height in points"
						on_press:app.size()
					TwoLineListItem:
						text:"Color"
						secondary_text:"Choose text color"
					TwoLineListItem:
						text:'Appearance'
						secondary_text:"Choose theme palette"
						on_press:app.show_thm()
						# IconLeftWidget:
						# 	icon:'format-color-fill'
					TwoLineListItem:
						text:'Info'
						secondary_text:"About this app"
						on_press:app.info()
						# IconLeftWidget:
						# 	icon:'information'
			
'''

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom right container.'''

class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False

class MainApp(MDApp):
	dialog = None
	def build(self):
		self.board=True
		self.w=MDBoxLayout(size_hint_y=0.65,md_bg_color=(1,1,0,1))
		return Builder.load_string(KV)
		
	def on_start(self):
		Window.bind(on_key_down=self.key_action)
		self.term=self.root.ids.console
		self.scrlvw=self.root.ids.scrlv
		tool=self.root.ids.tool
		f=open("color.txt", 'r')
		tool.md_bg_color=eval(f.read().splitlines()[1])
		os.chdir('C:/')
		
		self.cursor=u"\u2588"
		self.cwd=os.getcwd()+" $ "+self.cursor
		self.term.text=self.cwd
		
	def key_action(self, *args):
		textl=self.term.text.splitlines()
		l=textl[len(textl)-1]
		print(args[1])
		
		if args[1]==8:
			if l==self.cwd:
				print('ok')
			else:
				self.term.text=f"{self.term.text[:-2]}{self.cursor}"
			
		elif args[1]==13:
			cmd=l.replace(self.cwd[:-1], "")
			cmd=cmd.replace(self.cursor, "")
			self.term.text=f"{self.term.text[:-1]}\n{self.cursor}"
			Clock.schedule_once(partial(self.enter, cmd) ,0.3)
			
		elif args[1]==27:
			self.board=False
			self.kboard()
			
		
		if args[3]!=None:
			if args[3]=='İ':
				Clock.schedule_once(self.caps_lock, 0.01) #remove the unknown sign after loading the next letter
			self.term.text=f"{self.term.text[:-1]}{args[3]}{self.cursor}"
			
		Clock.schedule_once(self.scroll ,0.5)
		
	def enter(self, cmd, *args):
		print(cmd)
		self.term.text=self.term.text[:-1] #remove cursor
		if cmd=="clear" or cmd=="cls":
			self.term.text=""
		elif cmd[:2]=="cd":
			try:
				os.chdir(cmd[3:])
				self.cwd=os.getcwd()+" $ "+self.cursor
			except Exception as msg:
				self.term.text+=str(msg)
		else:
			out=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
			output=str(out.stdout.read()+out.stderr.read(), 'utf-8')
			# do something with output
			self.term.text+=output
			
		if self.term.text.endswith('\n') or cmd!="cls" or cmd!="clear":
			self.term.text+=self.cwd
		else:
			self.term.text+='\n'+self.cwd
		
	#	cursor=end
	def kboard(self, *args):
		if self.board:
			Window.request_keyboard(self.func('open'), self.term)
			self.root.ids.layout.add_widget(self.w)
			
		else:
			Window.release_keyboard(self.term)
			self.root.ids.layout.remove_widget(self.w)
			self.board=True
		
	def func(self, ins):
		print(ins)
		self.board=False
	
	def caps_lock(self, *args):
		letter=self.term.text[-2]
		self.term.text=f"{self.term.text[:-3]}{letter.upper()}{self.cursor}"
		
	def scroll(self, *args):
		if self.term.height>=self.scrlvw.height:
			self.scrlvw.scroll_y=0
			
	def goto(self, scr):
		self.root.current=scr

	def show_thm(self):
		MDThemePicker().open()

	def info(self):
		self.dlog=MDDialog(title='Info',text="This is a very simple Console App made with kivy and kivy material design (kivymd). This is made in the linux os based console.\n\nCopyright © www.learntocode.com || All rights reserved!",size_hint_x=0.9,auto_dismiss=False,
		buttons=[MDFlatButton(text='OK',on_release=self.bck)])
		self.dlog.open()

	def size(self):
		if not self.dialog:
			self.dlog = MDDialog(
                title="Phone ringtone",
                type="confirmation",
                items=[
                    ItemConfirm(text="14dp"),
                    ItemConfirm(text="15dp"),
                    ItemConfirm(text="16dp"),
                    ItemConfirm(text="17dp"),
                    ItemConfirm(text="18dp"),
                    ItemConfirm(text="19dp"),
                    ItemConfirm(text="20dp")
                ],size_hint_x=0.9,
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="Cancel",
                        on_release=self.bck
                    )
                ]
            )
		self.dlog.open()

	def font(self, fs):
		self.term.font_size=fs
		self.bck('test')

	def bck(self,obj):
		self.dlog.dismiss()
		
MainApp().run()