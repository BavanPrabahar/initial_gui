from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup 
import subprocess
import sys
class MyGrid2(Widget):
   
    
    def btn1(self):
        print("on")
        start_another_kivy_app()
  
    def btn2(self):
        print("off") 
        start2() 
    def btn3(self):
        show_popup()
    def btn5(self):
        print("o")
        start4()
    def btn4(self):
        print("<")
        start4()
    def btn6(self):
        print("map")
        start3()	
class P(FloatLayout):
	def slide(self,*args):
		print(args)
	
class My2App(App):
    def build(self):
      Window.clearcolor = (1, 1, 1, 1)
    
      return MyGrid2() 
	      
      
      
def show_popup():
    show=P()
    popupWindow=Popup(title="volume",content=show,size_hint=(None,None),size=(400,400))
    popupWindow.open()

def start_another_kivy_app():
    subprocess.Popen(["python3", "/home/racer/gui/manual.py"],bufsize=1)  
    sys.exit()
	
def start2():
    subprocess.Popen(["python3", "/home/racer/gui/remote.py"],bufsize=1)  
    sys.exit()
def start3():
    subprocess.Popen(["python3", "/home/racer/gui/map.py"],bufsize=1) 
    sys.exit()
def start4():
    subprocess.Popen(["python3", "/home/racer/gui/main.py"],bufsize=1)                   
    sys.exit()    

if __name__ == "__main__":
    window = My2App()
    window.run()
