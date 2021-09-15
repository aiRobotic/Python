import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
import json,glob,random
from datetime import datetime
from pathlib import Path

# Replace this with
# current version
kivy.require('1.11.1')  
Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up (self):
        self.manager.current = "Sign_Up_Screen"
    
    def login(self,uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        if uname in users and users[uname]['password']== pword:
            self.manager.current = "Login_Success"
        else:
            self.ids.incorrect_input.text = "Incorrect Username or Password \n                  Try again!" 

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] ={'username':uname,'password':pword,
        'created':datetime.now().strftime("%Y-%M-%D-%H-%S")}
        with open ("users.json","w") as file:
            json.dump(users,file)
        self.manager.current = "Sign_Up_Screen_Success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "Login_Screen"

class LoginSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_Screen"
    
    def get_feeling(self, feel):
        feel = feel.lower()
        files = glob.glob("quotes/*.txt")
        feelings = [Path(filename).stem for filename in files]
        if feel in feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"    
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