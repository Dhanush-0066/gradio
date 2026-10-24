import gradio as gr
gr.close_all()

def greet(name):
  return "Hello, " + name + "!"

demo.Interface(
  fn=greet,
  input=gr.Textbook(label="Name:"),
  outputs=[gr.Textbox()],
)

demo.launch()
