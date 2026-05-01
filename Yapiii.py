from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Создаём контейнер для виджетов
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        
        # Добавляем текст
        label = Label(text='Добро пожаловать в Kivy!', font_size='20sp')
        
        # Добавляем кнопку
        button = Button(text='Нажми меня', size_hint=(1, 0.3))
        button.bind(on_press=self.on_button_press)
        
        # Собираем всё вместе
        layout.add_widget(label)
        layout.add_widget(button)
        
        return layout
    
    def on_button_press(self, instance):
        print("Кнопка была нажата!")
        instance.text = "Нажато!"

if __name__ == '__main__':
    MyApp().run()