import justpy as jp
from design.definition import Definition

class Dictionary:

    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-100 cols-2')
        jp.Div(a=div, text='Instant Dictionary Page!', classes='text-4xl m-2 p-2')
        jp.Div(a=div, text='Get the definition of any English word instantly '
                           'as you type!', classes='text-lg m-2 p-2')
        input_div = jp.Div(a=div, classes = 'grid grid-cols-2 p-4')
        input_box = jp.Input(a=input_div, placeholder='Type in a word here....',
                 classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded-full "
                           " w-64 focus:bg-white focus:outline-none focus:border-purple-500 "
                           " py-2 px-4")

        div2 = jp.Div(a=wp, classes= 'bg-gray-200 h-40')
        outputdiv = jp.Div(a=div2, classes='m-2 p-2 text-lg border-5 border-black-400')

        jp.Button(a=input_div, text='Get Definition!',
                  classes='border-1 py-2 px-1 w-64 '
                          ' border-black-400 bg-red-100 '
                          ' rounded-full hover:bg-red-500',
                  click=cls.get_definition, outputdiv=outputdiv, inputbox=input_box)

        print(cls, req)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        d = Definition(widget.inputbox.value).get()
        widget.outputdiv.text = " ".join(d)



