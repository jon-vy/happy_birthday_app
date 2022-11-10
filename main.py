from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class HappyBirthday(App):
    def build(self):
        self.window = GridLayout()  # Создал окно
        self.window.cols = 1  # количество столбцов
        self.window.add_widget(
            Image(source="source/logo.png")  # фоновая картинка
        )

        self.conngratulate = Label(
            text="Введите имя:",
            font_size=48,
            color="#FF8C00"
        )
        self.window.add_widget(self.conngratulate)
        self.input_name = TextInput(
            size_hint=(1, 0.3),  # Высота строки 20% от текущей
            multiline=False,  # Отключить многострочный ввод
            padding=20
        )
        self.window.add_widget(self.input_name)

        self.button = Button(
            text="Поздравить",
            size_hint=(1, 0.3),
            background_color="#FF8C00",
            background_normal=""
        )
        self.button.bind(on_press=self.change_text)
        self.window.add_widget(self.button)

        return self.window

    def change_text(self, instance):
        self.conngratulate.text = "Поздравляю " + self.input_name.text



if __name__ == '__main__':
    HappyBirthday().run()


