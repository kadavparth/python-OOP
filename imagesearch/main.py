from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        # get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        #get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        #download the image
        req = requests.get(image_link)
        filepath = 'files/image.jpg'
        with open(filepath,'wb') as file:
            file.write(req.content)
        self.manager.current_screen.ids.images.source = filepath


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()