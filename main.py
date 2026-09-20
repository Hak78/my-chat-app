from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display

class ChatApp(App):
    # دالة مساعدة لتصحيح النصوص العربية وعرضها بشكل مترابط وصحيح
    def format_arabic(self, text):
        if not text:
            return ""
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # تحديد ملف الخط العربي الذي قمنا برفعه في المجلد الرئيسي
        self.font_path = "Amiri-Regular.ttf"
        
        # إعداد النص البرمجي الأولي وتمرير الخط العربي له
        initial_text = self.format_arabic("مرحباً بك في تطبيق المراسلة\n")
        self.chat_history = Label(
            text=initial_text, 
            size_hint_y=0.8,
            font_name=self.font_path,
            font_size="20sp"
        )
        layout.add_widget(self.chat_history)
        
        # حقل إدخال النص مع تعيين محاذاة لليمين والخط العربي
        hint_txt = self.format_arabic("اكتب رسالتك هنا...")
        self.user_input = TextInput(
            hint_text=hint_txt, 
            size_hint_y=0.1,
            font_name=self.font_path,
            halign="right",
            font_size="18sp"
        )
        layout.add_widget(self.user_input)
        
        # زر الإرسال بالخط العربي
        btn_txt = self.format_arabic("إرسال")
        send_btn = Button(
            text=btn_txt, 
            size_hint_y=0.1,
            font_name=self.font_path,
            font_size="18sp"
        )
        send_btn.bind(on_press=self.send_message)
        layout.add_widget(send_btn)
        
        return layout

    def send_message(self, instance):
        text = self.user_input.text
        if text:
            # دمج النص وتصحيح صياغته العربية بالكامل قبل عرضه في سجل المحادثة
            new_message = f"أنت: {text}"
            formatted_message = self.format_arabic(new_message)
            
            self.chat_history.text += f"\n{formatted_message}"
            self.user_input.text = ""

if __name__ == '__main__':
    ChatApp().run()
