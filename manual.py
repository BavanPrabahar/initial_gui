from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup 
from kivy.config import Config
import subprocess
import sys

class MyGrid5(Widget):
   
    def btn3(self):
        show_popup()
    def btn5(self):
        print("o")
        s1()
       
    def btn4(self):
        print("<")
        s2()
        
    	
class P(FloatLayout):
	def slide(self,*args):
		print(args)
	
class mymApp(App):
    def build(self):
      Window.clearcolor = (1, 1, 1, 1)
      return MyGrid5() 
	      
      
      
def show_popup():
    show=P()
    popupWindow=Popup(title="volume",content=show,size_hint=(None,None),size=(400,400))
    popupWindow.open()

def s1():      
    subprocess.Popen(["python3", "/home/racer/gui/main.py"],bufsize=1)
    sys.exit()

def s2():      
    subprocess.Popen(["python3", "/home/racer/gui/s2.py"],bufsize=1)
    sys.exit()

        

if __name__ == "__main__":
    window = mymApp()

    
    window.run()
		
