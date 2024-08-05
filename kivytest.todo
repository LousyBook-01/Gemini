from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from google.generativeai import GenerativeModel

class GeminiUI(BoxLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'vertical'
    self.padding = 20

    # API Key Input
    self.api_key_label = TextInput(text="Enter your Gemini API Key", font_size=16)
    self.add_widget(self.api_key_label)

    # Prompt Input
    self.prompt_input = TextInput(multiline=True, hint_text="Enter your prompt here", font_size=16)
    self.add_widget(self.prompt_input)

    # Generation Button
    self.generate_button = Button(text="Generate Text", on_press=self.generate_text, font_size=16)
    self.add_widget(self.generate_button)

    # Response Output
    self.response_scroll = ScrollView()
    self.response_output = TextInput(text="", _editable=False, font_size=16)
    self.response_scroll.add_widget(self.response_output)
    self.add_widget(self.response_scroll)

    # Customize look and feel using Kivy properties (refer to Kivy documentation for options)
    # self.background_color = (0.8, 0.8, 1, 1)  # Change background color

    # Initialize generative model (replace with your API key)
    self.model = GenerativeModel("YOUR_API_KEY")

  def generate_text(self, instance):
    prompt = self.prompt_input.text
    response = self.model.generate_content(prompt)
    self.response_output.text = response.text

class GeminiApp(App):
  def build(self):
    return GeminiUI()

if __name__ == "__main__":
  GeminiApp().run()