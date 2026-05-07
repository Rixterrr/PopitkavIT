from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout



class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        title = Label(text='Вход в систему', font_size='24sp')
        nickname_label = Label(text='Никнейм:', font_size='16sp', size_hint=(1, 0.2))
        self.nickname_input = TextInput(text='', multiline=False, size_hint=(1, 0.2))
        
        # Поле для пароля
        password_label = Label(text='Пароль:', font_size='16sp', size_hint=(1, 0.2))
        self.password_input = TextInput(text='', multiline=False, password=True, size_hint=(1, 0.2))
        
        # Кнопка входа
        login_button = Button(text='Войти', size_hint=(1, 0.3))
        login_button.bind(on_press=self.on_login_press)
        
        # Метка для вывода результата
        self.result_label = Label(text='', font_size='14sp')
        
        # Собираем всё вместе
        layout.add_widget(title)
        layout.add_widget(nickname_label)
        layout.add_widget(self.nickname_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.result_label)
        
        return layout
    
    def on_login_press(self, instance):
        nickname = self.nickname_input.text
        password = self.password_input.text
        
        # Простая проверка (замените на свою логику)
        if nickname == "admin" and password == "12345":
            self.result_label.text = f"Добро пожаловать, {nickname}!"
            self.result_label.color = (0, 1, 0, 1)  # Зелёный текст
        else:
            self.result_label.text = "Неверный никнейм или пароль!"
            self.result_label.color = (1, 0, 0, 1)  # Красный текст

if __name__ == '__main__':
    MyApp().run()