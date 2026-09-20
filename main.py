from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
import arabic_reshaper
from bidi.algorithm import get_display

class ChatScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط علوي يحتوي على زر الانتقال للكاميرا والإعدادات
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        
        camera_btn = Button(
            text=self.format_arabic("الكاميرا 📷"),
            font_name=self.font_path,
            font_size="16sp",
            size_hint_x=0.3
        )
        camera_btn.bind(on_press=self.go_to_camera)
        
        settings_btn = Button(
            text=self.format_arabic("الإعدادات ⚙️"),
            font_name=self.font_path,
            font_size="16sp",
            size_hint_x=0.3
        )
        settings_btn.bind(on_press=self.go_to_settings)
        
        top_bar.add_widget(camera_btn)
        top_bar.add_widget(settings_btn)
        layout.add_widget(top_bar)
        
        # سجل المحادثة
        initial_text = self.format_arabic("مرحباً بك في تطبيق المراسلة\n")
        self.chat_history = Label(
            text=initial_text, 
            size_hint_y=0.7,
            font_name=self.font_path,
            font_size="20sp"
        )
        layout.add_widget(self.chat_history)
        
        # حقل إدخال النص
        hint_txt = self.format_arabic("اكتب رسالتك هنا...")
        self.user_input = TextInput(
            hint_text=hint_txt, 
            size_hint_y=0.1,
            font_name=self.font_path,
            halign="right",
            font_size="18sp"
        )
        layout.add_widget(self.user_input)
        
        # زر الإرسال
        btn_txt = self.format_arabic("إرسال")
        send_btn = Button(
            text=btn_txt, 
            size_hint_y=0.1,
            font_name=self.font_path,
            font_size="18sp"
        )
        send_btn.bind(on_press=self.send_message)
        layout.add_widget(send_btn)
        
        self.add_widget(layout)

    def go_to_camera(self, instance):
        self.manager.current = 'camera_screen'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

    def send_message(self, instance):
        text = self.user_input.text
        if text:
            username = self.manager.get_screen('settings').username
            formatted_user = self.format_arabic(f"{username}: ")
            formatted_msg = self.format_arabic(text)
            self.chat_history.text += f"\n{formatted_user}{formatted_msg}"
            self.user_input.text = ""

class CameraScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # عنصر تشغيل الكاميرا من Kivy بدقة مناسبة للهواتف
        self.cam = Camera(resolution=(640, 480), play=False, size_hint_y=0.8)
        layout.add_widget(self.cam)
        
        # أزرار التحكم بالكاميرا
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10)
        
        self.toggle_btn = Button(
            text=self.format_arabic("تشغيل الكاميرا ▶️"),
            font_name=self.font_path,
            font_size="16sp"
        )
        self.toggle_btn.bind(on_press=self.toggle_camera)
        
        back_btn = Button(
            text=self.format_arabic("رجوع للدردشة ↩️"),
            font_name=self.font_path,
            font_size="16sp"
        )
        back_btn.bind(on_press=self.back_to_chat)
        
        buttons_layout.add_widget(self.toggle_btn)
        buttons_layout.add_widget(back_btn)
        layout.add_widget(buttons_layout)
        
        self.add_widget(layout)

    def toggle_camera(self, instance):
        # تشغيل أو إيقاف استعراض الكاميرا الحية
        if self.cam.play:
            self.cam.play = False
            self.toggle_btn.text = self.format_arabic("تشغيل الكاميرا ▶️")
        else:
            self.cam.play = True
            self.toggle_btn.text = self.format_arabic("إيقاف الكاميرا ⏸️")

    def back_to_chat(self, instance):
        self.cam.play = False  # إغلاق الكاميرا عند الرجوع للحفاظ على البطارية
        self.toggle_btn.text = self.format_arabic("تشغيل الكاميرا ▶️")
        self.manager.current = 'chat'

class SettingsScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        self.username = "أنت"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text=self.format_arabic("إعدادات التطبيق ⚙️"), font_name=self.font_path, font_size="24sp", size_hint_y=0.2)
        layout.add_widget(title)
        
        input_label = Label(text=self.format_arabic("تغيير اسم المستخدم:"), font_name=self.font_path, font_size="16sp", size_hint_y=0.1)
        layout.add_widget(input_label)
        
        self.name_input = TextInput(text=self.username, font_name=self.font_path, size_hint_y=0.1, halign="right", font_size="16sp", multiline=False)
        layout.add_widget(self.name_input)
        
        save_btn = Button(text=self.format_arabic("حفظ والعودة للدردشة 💾"), font_name=self.font_path, font_size="18sp", size_hint_y=0.15)
        save_btn.bind(on_press=self.save_and_return)
        layout.add_widget(save_btn)
        
        layout.add_widget(Label(size_hint_y=0.45))
        self.add_widget(layout)

    def save_and_return(self, instance):
        if self.name_input.text.strip():
            self.username = self.name_input.text.strip()
        self.manager.current = 'chat'

class ChatApp(App):
    def format_arabic(self, text):
        if not text:
            return ""
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)

    def build(self):
        self.font_path = "Amiri-Regular.ttf"
        sm = ScreenManager()
        sm.add_widget(ChatScreen(self.format_arabic, self.font_path, name='chat'))
        sm.add_widget(SettingsScreen(self.format_arabic, self.font_path, name='settings'))
        sm.add_widget(CameraScreen(self.format_arabic, self.font_path, name='camera_screen'))
        return sm

if __name__ == '__main__':
    ChatApp().run()
