from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label   
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import datetime

class TestApp(App):
    def build(self):
        i = 0

        self.m=i
        # return TextInput(multiline=False)
        today=str(datetime.date.today())

        lbl=Label(text='name? ')
        time_lbl=Label(text= today)

        txt = TextInput()
        btn = Button(text='[b]tap![/b]' ,font_size='30',markup= True, background_color= (2,1,2), color=(1,1,3),
        size_hint=(0.3,0.4), pos_hint={'x':0.6 ,'y': 0.2}, background_normal='green.jpg',
        background_down='download.jpg')

        self.lbl = lbl
        self.txt=txt
        self.btn=btn

        btn.bind(on_press= self.press)
        btn.bind(on_ = self.press)

        box = BoxLayout(orientation='vertical', spacing=10)
        box.add_widget(lbl)
        box.add_widget(txt)
        box.add_widget(btn)
        box.add_widget(time_lbl)

        return box

    def press(self, event):
        m=self.m+1

#self.lbl.text='alrightt'



if __name__ == "__main__":
    TestApp().run()


'''from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class app(App):
    def mai(self):

        lbl1=Label(text='your name? ')
        lbl2=Label(text='your last name? ', pos_hint={'x':0.6 ,'y':0.5})
        lbl3=Label(text='age', pos_hint={'x':0.6,'y':0.5 })

        txt1=TextInput(pos_hint={'x':0.6 ,'y':0.5})
        txt2=TextInput(pos_hint={'x':0.6 ,'y':0.5})
        txt3=TextInput(pos_hint={'x':0.6,'y':0.5 })

        submit_btn=Button(text='submit!')

        box=BoxLayout(orientation='horizontal')
        box.add_widet(lbl1)

        return box


if __name__ == "__main__":
    app().run()
'''
