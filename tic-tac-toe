from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import *
from kivy.uix.label import Label


d_factor = True
clicks=0
#this is comme
#this too is comment

def change_d_factor(self,d_factor):
    if d_factor == True:
        d_factor = False
    elif d_factor==False:
        d_factor=True
    return d_factor    
        
        
class MyLayout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.rows=3
        self.widget_1 = Button(text='LET US PLAY TIC-TAC-TOE',size=(200,200),size_hint=(.2,.2),background_color=(.1,.2,56,224))
        self.add_widget(self.widget_1)
        self.main_widget = GridLayout(rows=3,cols=3)
        
        self.button_1 = Button()
        self.button_2 = Button()
        self.button_3 = Button()
        self.button_4 = Button()
        self.button_5 = Button()
        self.button_6 = Button()
        self.button_7 = Button()
        self.button_8 = Button()
        self.button_9 = Button()

        self.button_1.bind(on_press=self.produce_1)
        self.button_2.bind(on_press=self.produce_2)
        self.button_3.bind(on_press=self.produce_3)
        self.button_4.bind(on_press=self.produce_4)
        self.button_5.bind(on_press=self.produce_5)
        self.button_6.bind(on_press=self.produce_6)
        self.button_7.bind(on_press=self.produce_7)
        self.button_8.bind(on_press=self.produce_8)
        self.button_9.bind(on_press=self.produce_9)
        
        
        
        self.main_widget.add_widget(self.button_1)
        self.main_widget.add_widget(self.button_2)
        self.main_widget.add_widget(self.button_3)
        self.main_widget.add_widget(self.button_4)
        self.main_widget.add_widget(self.button_5)
        self.main_widget.add_widget(self.button_6)
        self.main_widget.add_widget(self.button_7)
        self.main_widget.add_widget(self.button_8)
        self.main_widget.add_widget(self.button_9)
        self.add_widget(self.main_widget)

    def change_d_factor(self):
        global d_factor
        if d_factor == True:
            d_factor = False
        elif d_factor==False:
            d_factor=True
        return d_factor    
        
    def increase_click(self):
        global clicks
        clicks+=1
        return clicks
        
    def check_d_factor(self,d_factor):
        if d_factor==True:
            symbol='X'
        elif d_factor==False:
            symbol='O'
        return str(symbol)
    
    def produce_1(self,instance):
        
        self.button_1.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.wins()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_1.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))    
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_1.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
               
    def produce_2(self,instance):
        self.button_2.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.wins()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_2.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))    
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_2.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_3(self,instance):
        self.button_3.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_3.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_3.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_4(self,instance):
        self.button_4.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_4.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))    
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_4.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_5(self,instance):
        self.button_5.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )  
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_5.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_5.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_6(self,instance):
        self.button_6.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_6.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))                          
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_6.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_7(self,instance):
        self.button_7.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_7.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))                          
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_7.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_8(self,instance):
        self.button_8.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True) )
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_8.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))                          
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_8.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
    def produce_9(self,instance):
        self.button_9.text=self.check_d_factor(d_factor)
        self.change_d_factor()
        self.increase_click()
        if clicks==9 and self.win()==False:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Please play again',content=Label(text='Game Over'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))
        elif self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_9.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))                          
        elif clicks==9 and self.win()==True:
            self.remove_widget(self.widget_1)
            self.remove_widget(self.main_widget)
            self.add_widget(Popup(title='Congratulations',content=Label(text=str(self.button_9.text)+' won'),size_hint=(None, None),size = (800,800),pos_hint={'x':.2,'y':.3},auto_dismiss=True))     
            
            
    def display_popup(self,clicks):
        layout = GridLayout(cols=1,text='Bye')
        label = Label(text='Game over')
        layout.add_widget(label)
        popup = Popup(title='',content=layout,size=(100,100),auto_dismiss=True)
        popup.open()
        
    def win(self):
        if ((self.button_1.text=='X' and self.button_2.text=='X' and self.button_3.text=='X'))or((self.button_1.text=='O' and self.button_2.text=='O' and self.button_3.text=='O')):
            return True
        elif ((self.button_1.text=='X' and self.button_4.text=='X' and self.button_7.text=='X'))or((self.button_1.text=='O' and self.button_4.text=='O' and self.button_7.text=='O')):
            return True
        elif ((self.button_1.text=='X' and self.button_5.text=='X' and self.button_9.text=='X'))or((self.button_1.text=='O' and self.button_5.text=='O' and self.button_9.text=='O')):
            return True
        elif ((self.button_3.text=='X' and self.button_5.text=='X' and self.button_7.text=='X'))or((self.button_3.text=='O' and self.button_5.text=='O' and self.button_7.text=='O')):
            return True
        elif ((self.button_3.text=='X' and self.button_6.text=='X' and self.button_9.text=='X'))or((self.button_3.text=='O' and self.button_6.text=='O' and self.button_9.text=='O')):
            return True
        elif ((self.button_7.text=='X' and self.button_8.text=='X' and self.button_9.text=='X'))or((self.button_7.text=='O' and self.button_8.text=='O' and self.button_9.text=='O')):
            return True
        elif ((self.button_4.text=='X' and self.button_5.text=='X' and self.button_6.text=='X'))or((self.button_4.text=='O' and self.button_5.text=='O' and self.button_6.text=='O')):
            return True
        elif ((self.button_2.text=='X' and self.button_5.text=='X' and self.button_8.text=='X'))or((self.button_2.text=='O' and self.button_5.text=='O' and self.button_8.text=='O')):
            return True
        else:
            return False

            
class MyApp(App):
    def build(self):
        return MyLayout()
    
if __name__=='__main__':
    MyApp().run()
