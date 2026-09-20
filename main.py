from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle
import arabic_reshaper
from bidi.algorithm import get_display

# فئة مخصصة لإنشاء خلفيات ملونة برمجياً للواجهات والأشرطة
class ColorBoxLayout(BoxLayout):
    def __init__(self, bg_color, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

# 💬 1. شاشة غرفة الدردشة الاحترافية
class ChatScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        self.send_sound = SoundLoader.load('msg_sound.wav')
        
        # الخلفية الأساسية للتطبيق (أزرق داكن خفيف مريح للعين)
        main_layout = ColorBoxLayout(bg_color=(0.11, 0.15, 0.21, 1), orientation='vertical', padding=10, spacing=10)
        
        # 🔝 شريط علوي أنيق باللون الأزرق الملكي
        top_bar = ColorBoxLayout(bg_color=(0.14, 0.27, 0.44, 1), orientation='horizontal', size_hint_y=0.12, padding=[8, 4], spacing=8)
        
        # أزرار الاتصال بتصميم عصري ملون
        audio_call_btn = Button(
            text=self.format_arabic("صوت 📞"), font_name=self.font_path, font_size="13sp", size_hint_x=0.22,
            background_normal='', background_color=(0.18, 0.49, 0.20, 1) # أخضر
        )
        audio_call_btn.bind(on_press=self.start_audio_call)
        
        video_call_btn = Button(
            text=self.format_arabic("فيديو 🎥"), font_name=self.font_path, font_size="13sp", size_hint_x=0.22,
            background_normal='', background_color=(0.0, 0.47, 0.84, 1) # أزرق فاتح
        )
        video_call_btn.bind(on_press=self.start_video_call)
        
        settings_btn = Button(
            text=self.format_arabic("⚙️"), font_name=self.font_path, font_size="14sp", size_hint_x=0.14,
            background_normal='', background_color=(0.4, 0.4, 0.4, 1)
        )
        settings_btn.bind(on_press=self.go_to_settings)
        
        title_lbl = Label(
            text=self.format_arabic("محادثة ذكية"), font_name=self.font_path, font_size="18sp", halign="right",
            color=(1, 1, 1, 1)
        )
        
        top_bar.add_widget(settings_btn)
        top_bar.add_widget(video_call_btn)
        top_bar.add_widget(audio_call_btn)
        top_bar.add_widget(title_lbl)
        main_layout.add_widget(top_bar)
        
        # 📜 منطقة الرسائل
        initial_text = self.format_arabic("مرحباً بك في تطبيق المراسلة المثالي 🚀\n")
        self.chat_history = Label(
            text=initial_text, size_hint_y=0.68, font_name=self.font_path, font_size="20sp",
            color=(0.9, 0.9, 0.9, 1), halign="center"
        )
        main_layout.add_widget(self.chat_history)
        
        # ⌨️ صندوق إدخال النصوص
        self.user_input = TextInput(
            hint_text=self.format_arabic("اكتب رسالتك هنا..."), size_hint_y=0.09, font_name=self.font_path,
            halign="right", font_size="16sp", background_color=(1, 1, 1, 0.95), cursor_color=(0,0,0,1)
        )
        main_layout.add_widget(self.user_input)
        
        # 📤 زر الإرسال العريض والأزرق
        send_btn = Button(
            text=self.format_arabic("إرسال الرسالة"), size_hint_y=0.09, font_name=self.font_path, font_size="16sp",
            background_normal='', background_color=(0.0, 0.47, 0.84, 1), color=(1, 1, 1, 1)
        )
        send_btn.bind(on_press=self.send_message)
        main_layout.add_widget(send_btn)
        
        self.add_widget(main_layout)

    def start_audio_call(self, instance):
        self.manager.get_screen('call_screen').setup_call_mode(video=False)
        self.manager.current = 'call_screen'

    def start_video_call(self, instance):
        self.manager.get_screen('call_screen').setup_call_mode(video=True)
        self.manager.current = 'call_screen'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

    def send_message(self, instance):
        text = self.user_input.text
        if text:
            username = self.manager.get_screen('settings').username
            formatted_user = self.format_arabic(f"[{username}]: ")
            formatted_msg = self.format_arabic(text)
            self.chat_history.text += f"\n{formatted_user}{formatted_msg}"
            self.user_input.text = ""
            if self.send_sound:
                self.send_sound.play()

# 📞 2. شاشة المكالمات الموحدة والمثالية
class CallScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        
        self.main_layout = ColorBoxLayout(bg_color=(0.08, 0.1, 0.14, 1), orientation='vertical', padding=20, spacing=15)
        
        self.status_label = Label(
            text=self.format_arabic("جاري الاتصال..."), font_name=self.font_path, font_size="22sp", size_hint_y=0.15,
            color=(0.18, 0.8, 0.44, 1)
        )
        self.main_layout.add_widget(self.status_label)
        
        self.media_container = BoxLayout(size_hint_y=0.65)
        self.cam = Camera(resolution=(640, 480), play=False)
        self.main_layout.add_widget(self.media_container)
        
        # زر إنهاء مكالمة بلون أحمر ناصع واحترافي
        self.end_btn = Button(
            text=self.format_arabic("قطع الاتصال ❌"), font_name=self.font_path, font_size="18sp", size_hint_y=0.2,
            background_normal='', background_color=(0.9, 0.22, 0.22, 1), color=(1, 1, 1, 1)
        )
        self.end_btn.bind(on_press=self.end_call)
        self.main_layout.add_widget(self.end_btn)
        
        self.add_widget(self.main_layout)

    def setup_call_mode(self, video=False):
        self.media_container.clear_widgets()
        if video:
            self.status_label.text = self.format_arabic("اتصال مرئي نشط 🎥")
            self.media_container.add_widget(self.cam)
            self.cam.play = True
        else:
            self.status_label.text = self.format_arabic("اتصال صوتي نشط 📞")
            self.media_container.add_widget(Label(text="🎙️", font_size="90sp", color=(1,1,1,1)))
            self.cam.play = False

    def end_call(self, instance):
        self.cam.play = False
        self.manager.current = 'chat'

# ⚙️ 3. شاشة إعدادات الدردشة والملف الشخصي الملونة
class SettingsScreen(Screen):
    def __init__(self, format_arabic_func, font_path, **kwargs):
        super().__init__(**kwargs)
        self.format_arabic = format_arabic_func
        self.font_path = font_path
        self.username = "أنت"
        
        layout = ColorBoxLayout(bg_color=(0.11, 0.15, 0.21, 1), orientation='vertical', padding=25, spacing=15)
        
        title = Label(text=self.format_arabic("إعدادات الدردشة ⚙️"), font_name=self.font_path, font_size="24sp", size_hint_y=0.15, color=(1,1,1,1))
        layout.add_widget(title)
        
        input_label = Label(text=self.format_arabic("تعديل اسم المستخدم الشخصي:"), font_name=self.font_path, font_size="16sp", size_hint_y=0.1, color=(0.7,0.7,0.7,1))
        layout.add_widget(input_label)
        
        self.name_input = TextInput(
            text=self.username, font_name=self.font_path, size_hint_y=0.09, halign="right", font_size="16sp",
            multiline=False, background_color=(1,1,1,1)
        )
        layout.add_widget(self.name_input)
        
        save_btn = Button(
            text=self.format_arabic("حفظ التغييرات والعودة 💾"), font_name=self.font_path, font_size="16sp", size_hint_y=0.12,
            background_normal='', background_color=(0.18, 0.49, 0.20, 1)
        )
        save_btn.bind(on_press=self.save_and_return)
        layout.add_widget(save_btn)
        
        layout.add_widget(Label(size_hint_y=0.54))
        self.add_widget(layout)

    def save_and_return(self, instance):
        if self.name_input.text.strip():
            self.username = self.name_input.text.strip()
        self.manager.current = 'chat'

# 🚀 4. مدير تشغيل التطبيق
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
        sm.add_widget(CallScreen(self.format_arabic, self.font_path, name='call_screen'))
        return sm

if __name__ == '__main__':
    ChatApp().run()
