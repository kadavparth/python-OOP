from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import time
from filestack import Client

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = current_time + ".png"
        self.ids.camera.export_to_png(self.filename)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filename

class ImageScreen(Screen):

    def create_link(self):
        filepath = App.get_running_app().root.ids.camera_screen.filename
        print(filepath)
        self.ids.link.text = filepath

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

class Fileshare:

    def __init__(self,filepath,api_key="AuOwGEnunQTy8i3yQ2QJ5z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

MainApp().run()
