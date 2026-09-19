from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ChatApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.chat_history = Label(text="مرحباً بك في تطبيق المراسلة\n", size_hint_y=0.8)
        layout.add_widget(self.chat_history)
        
        self.user_input = TextInput(hint_text="اكتب رسالتك هنا...", size_hint_y=0.1)
        layout.add_widget(self.user_input)
        
        send_btn = Button(text="إرسال", size_hint_y=0.1)
        send_btn.bind(on_press=self.send_message)
        layout.add_widget(send_btn)
        
        return layout

    def send_message(self, instance):
        text = self.user_input.text
        if text:
            self.chat_history.text += f"\nأنت: {text}"
            self.user_input.text = ""

if __name__ == '__main__':
    ChatApp().run()
