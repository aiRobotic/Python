import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

# Replace this with
# current version
kivy.require('1.11.1')  
Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up (self):
        self.manager.current = "Sign_Up_Screen"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] ={'username':uname,'password':pword,
        'created':datetime.now().strftime("%Y-%M-%D-%H-%S")}
        with open ("users.joson","w") as file:
            json.dump(users,file)


class RootWidget (ScreenManager):
    def build(self):
        return LoginScreen()

# Defining a class
class MyFirstKivyApp(App):
    # Function that returns 
    # the root widget
    def build(self):
        # Label with text Hello World is 
        # returned as root widget
        return RootWidget()        
  
  
# Here our class is initialized
# and its run() method is called. 
# This initializes and starts 
# our Kivy application.
MyFirstKivyApp().run()   