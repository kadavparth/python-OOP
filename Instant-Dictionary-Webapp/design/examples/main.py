import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

    div1 = jp.Div(a=div, classes = 'grid grid-cols-3 gap-4 p-4')
    in1 = jp.Input(a=div1, placeholder='Enter First Value',
             classes='form-input')
    in2 = jp.Input(a=div1, placeholder = 'Enter Second Value',
             classes='form-input')
    dout = jp.Div(a=div1, text= "Result goes here")
    jp.Div(a=div1, text="Another Div", classes = 'text-gray-600')
    jp.Div(a=div1, text="Another Div", classes = 'text-gray-600')


    div2 = jp.Div(a=div, classes = 'grid grid-cols-2 gap-4')
    jp.Button(a=div2, text='Calculate', click= sum_up, in1= in1, in2= in2, dout= dout,
              classes = 'border-4 py-2 px-4 m-2 rounded-full border-indigo-800 bg-red-100 hover:bg-red-500 hover:text-white')

    jp.Div(a=div2, text='I am a cool interactive div', mouseenter = mouse_enter, mouseleave= mouse_leaves,
           classes = 'hover:bg-red-500')
    return wp

def sum_up(widget,msg):
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.dout.text = sum

def mouse_enter(widget,msg):
    widget.text = "A mouse enters the house!"

def mouse_leaves(widget,msg):
    widget.text = "The mouse leaves the house!"

jp.justpy()