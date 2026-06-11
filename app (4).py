
import gradio as gr

def hello(name):
    return "Hello " + name

app = gr.Interface(fn=hello, inputs="text", outputs="text")

app.launch()
