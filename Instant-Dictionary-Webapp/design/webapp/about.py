import justpy as jp

class About:
    path = "/about"
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes = 'bg-gray-200 h-screen')
        jp.Div(a=div, text = 'This is the about page!', classes = 'text-4xl m-2')
        jp.Div(a=div, text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo'
                             'd tempor incididunt ut labore et dolore magna aliqua. Ut enim a'
                             'd minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliqui'
                             'p ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cill'
                             'um dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia de'
                             'serunt mollit anim id est laborum.',
               classes = "text-lg")
        return wp

