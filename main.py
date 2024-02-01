from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup 
from kivy.config import Config
import subprocess
import sys

class MyGrid(Widget):
   
    
    def btn1(self):
        print("on")
        start_another_kivy_app()
  
    def btn2(self):
        print("off") 
         
    def btn3(self):
        show_popup()
    def btn5(self):
        print("o")
    def btn4(self):
        print("<")
    	
class P(FloatLayout):
	def slide(self,*args):
		print(args)
	
class My1App(App):
    def build(self):
      Window.clearcolor = (1, 1, 1, 1)
      return MyGrid() 
	      
      
      
def show_popup():
    show=P()
    popupWindow=Popup(title="volume",content=show,size_hint=(None,None),size=(400,400))
    popupWindow.open()

def start_another_kivy_app():
    subprocess.Popen(["python3", "/home/racer/gui/s2.py"],bufsize=1)
    sys.exit()

        

if __name__ == "__main__":
    window = My1App()
   
    window.run()
