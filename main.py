import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
  
# Replace this with
# current version
kivy.require('1.11.1')  
Builder.load_file('design.kv')

class LoginScreen(Screen):
    pass

# Defining a class
class MyFirstKivyApp(App):
      
    # Function that returns 
    # the root widget
    def build(self):
          
        # Label with text Hello World is 
        # returned as root widget
        return LoginScreen()        
  
  
# Here our class is initialized
# and its run() method is called. 
# This initializes and starts 
# our Kivy application.
MyFirstKivyApp().run()   