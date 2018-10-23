from kivy.app import App
from kivy.lang import Builder
from os import getcwd
from os.path import exists
from os.path import splitext
import recognize
import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger
from kivy.core.audio import SoundLoader
from plyer import camera
from kivy.uix.screenmanager import ScreenManager, Screen

__version__ = '0.0.1'

Builder.load_string("""

<MenuScreen>:
    FloatLayout:

        Button:
            text: 'Take picture from camera!'
            pos_hint: {'x': 0, 'y': 0}
            size_hint: 1, 1
            on_press:  root.do_capture()
        Image:
            source:"dez/main.jpg"
            size_hint:1, 1

<ResultScreen>:
    FloatLayout:

        Button:
            text: 'Take picture from camera!'
            pos_hint: {'x': 0, 'y': 0}
            size_hint: 1, 1
            on_press: root.do_capture()
        Image:
            source:"dez/result.jpg"
            size_hint:1, 1


<MsgPopup>:
    size_hint: .7, .4
    title: "Attention"

    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 20

        Label:
            id: message_label
            size_hint_y: 0.4
            text: "Label"
        Button:
            text: 'Dismiss'
            size_hint_y: 0.4
            on_press: root.dismiss()

<ImgPopup>:
    size_hint: .7, .4
    title: "Attention"

    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 20

        Image:
            id: image_label
            source: "filepath"
        Button:
            text: 'Dismiss'
            size_hint_y: 0.4
            on_press: root.dismiss()


""")
sm = ScreenManager()


class MenuScreen(Screen):

    def __init__(self):
        super(MenuScreen, self).__init__()
        self.name = 'menu'
        self.cwd = getcwd() + "/"
        self.filepath = self.cwd + "value.jpg"
        main_sound = SoundLoader.load("audio/mainsound.mp3")
        main_sound.play()
    def change(self):
        sm.current = "result"
    def do_capture(self):

        ext = splitext(self.filepath)[-1].lower()

        try:
            camera.take_picture(filename=self.filepath,
                                on_complete=self.camera_callback)
        except NotImplementedError:
            if __name__ == "__main__":
                value = recognize.Main("known_people","one.jpg",1,0.5,True)
            print(value)
            if value[0] == "1":
                sound1 = SoundLoader.load("audio/sound1.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Одна Гривна"))
            if value[0] == "5":
                sound1 = SoundLoader.load("audio/sound5.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пять Гривен"))
            if value[0] == "10":
                sound1 = SoundLoader.load("audio/sound10.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Десять Гривен"))
            if value[0] == "20":
                sound1 = SoundLoader.load("audio/sound20.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Двадцать Гривен"))
            if value[0] == "50":
                sound1 = SoundLoader.load("audio/sound50.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пятьдесят Гривен"))
            if value[0] == "100":
                sound1 = SoundLoader.load("audio/sound100.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Сто Гривен"))
            if value[0] == "200":
                sound1 = SoundLoader.load("audio/sound200.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Двести Гривен"))
            if value[0] == "500":
                sound1 = SoundLoader.load("audio/sound500.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пятьсот Гривен"))
            else :
                sound1 = SoundLoader.load("error.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Ошибка"))

            self.change()

    def camera_callback(self, filepath):
        if(exists(self.filepath)):
            if __name__ == "__main__":
                value = recognize.Main("known_people","one.jpg",1,0.5,True)
            print(value)
            if value[0] == "1":
                sound1 = SoundLoader.load("audio/sound1.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Одна Гривна"))
            if value[0] == "5":
                sound1 = SoundLoader.load("audio/sound5.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пять Гривен"))
            if value[0] == "10":
                sound1 = SoundLoader.load("audio/sound10.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Десять Гривен"))
            if value[0] == "20":
                sound1 = SoundLoader.load("audio/sound20.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Двадцать Гривен"))
            if value[0] == "50":
                sound1 = SoundLoader.load("audio/sound50.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пятьдесят Гривен"))
            if value[0] == "100":
                sound1 = SoundLoader.load("audio/sound100.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Сто Гривен"))
            if value[0] == "200":
                sound1 = SoundLoader.load("audio/sound200.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Двести Гривен"))
            if value[0] == "500":
                sound1 = SoundLoader.load("audio/sound500.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Пятьсот Гривен"))
            else :
                sound1 = SoundLoader.load("audio/error.mp3")
                sound1.play()
                sm.add_widget(ResultScreen("Ошибка"))

            self.change()
        else:
            popup = MsgPopup("Could not save your picture!")
            popup.open()

class ResultScreen(Screen):
    def __init__(self,val):
        super(ResultScreen, self).__init__()
        self.label = Label(pos_hint = {'x': 0, 'center_y': .8},
            size_hint=( 1, .5),
            text =val,
            font_size = 70,
            font_name = "font/Raleway-Bold.ttf")
        self.add_widget(self.label)
        self.name = "result"
        self.cwd = getcwd() + "/"
        self.filepath = self.cwd + "eboi.jpg"


    def do_capture(self):

        ext = splitext(self.filepath)[-1].lower()

        try:
            camera.take_picture(filename=self.filepath,
                                on_complete=self.camera_callback)
        except NotImplementedError:
            if __name__ == "__main__":
                value = recognize.Main("known_people","hmqual.jpg",1,0.5,True)
                print(value)
                print(value)
            print(value[0])
            if value[0] == "1":
                sound1 = SoundLoader.load("audio/sound1.mp3")
                sound1.play()
                self.label.text = "Одна Гривна"
            if value[0] == '5':
                sound1 = SoundLoader.load("audio/sound5.mp3")
                sound1.play()
                self.label.text = "Пять Гривен"
            if value[0] == "10":
                sound1 = SoundLoader.load("audio/sound10.mp3")
                sound1.play()
                self.label.text = "Десять Гривен"
            if value[0] == "20":
                sound1 = SoundLoader.load("audio/sound20.mp3")
                sound1.play()
                self.label.text = "Двадцать Гривен"
            if value[0] == "50":
                sound1 = SoundLoader.load("audio/sound50.mp3")
                sound1.play()
                self.label.text = "Пятьдесят Гривен"
            if value[0] == "100":
                sound1 = SoundLoader.load("audio/sound100.mp3")
                sound1.play()
                self.label.text = "Сто Гривен"
            if value[0] == "200":
                sound1 = SoundLoader.load("audio/sound200.mp3")
                sound1.play()
                self.label.text = "Двести Гривен"
            if value[0] == "500":
                sound1 = SoundLoader.load("audio/sound500.mp3")
                sound1.play()
                self.label.text = "Пятьсот Гривен"
            # else :
            #     #sound1 = SoundLoader.load("audio/error.mp3")
            #     #sound1.play()
            #     self.label.text = "Ошибка"
    def camera_callback(self, filepath):
        if(exists(self.filepath)):
                if __name__ == "__main__":
                    value = recognize.Main("known_people","five1.jpeg",1,0.5,True)
                if value[0] == "1":
                    sound1 = SoundLoader.load("audio/sound1.mp3")
                    sound1.play()
                    self.label.text = "Одна Гривна"
                if value[0] == "5":
                    sound1 = SoundLoader.load("audio/sound5.mp3")
                    sound1.play()
                    self.label.text = "Пять Гривен"
                if value[0] == "10":
                    sound1 = SoundLoader.load("audio/sound10.mp3")
                    sound1.play()
                    self.label.text = "Десять Гривен"
                if value[0] == "20":
                    sound1 = SoundLoader.load("audio/sound20.mp3")
                    sound1.play()
                    self.label.text = "Двадцать Гривен"
                if value[0] == "50":
                    sound1 = SoundLoader.load("audio/sound50.mp3")
                    sound1.play()
                    self.label.text = "Пятьдесят Гривен"
                if value[0] == "100":
                    sound1 = SoundLoader.load("audio/sound100.mp3")
                    sound1.play()
                    self.label.text = "Сто Гривен"
                if value[0] == "200":
                    sound1 = SoundLoader.load("audio/sound200.mp3")
                    sound1.play()
                    self.label.text = "Двести Гривен"
                if value[0] == "500":
                    sound1 = SoundLoader.load("audio/sound500.mp3")
                    sound1.play()
                    self.label.text = "Пятьсот Гривен"
                # else :
                #     #sound1 = SoundLoader.load("audio/error.mp3")
                #     #sound1.play()
                #     self.label.text = "Ошибка"
        else:
            popup = MsgPopup("Could not save your picture!")
            popup.open()




sm.add_widget(MenuScreen())

class CameraDemoApp(App):
    def __init__(self):
        super(CameraDemoApp, self).__init__()
        self.demo = None

    def build(self):
        self.demo = sm
        return self.demo

    def on_pause(self):
        return True

    def on_resume(self):
        pass
class MsgPopup(Popup):
    def __init__(self, msg):
        super(MsgPopup, self).__init__()
        self.ids.message_label.text = msg
class ImgPopup(Popup):
    def __init__(self, filepath):
        super(ImgPopup, self).__init__()
        self.ids.image_label.source = filepath

if __name__ == '__main__':
    CameraDemoApp().run()
