# ---------- ANDROID SAFE CONFIG ----------
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.core.window import Window
Window.size = (360, 640)

# ---------- IMPORTS ----------
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


# ---------- MAIN UI ----------
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation='vertical',
            padding=[20, 30, 20, 20],
            spacing=15,
            **kwargs
        )

        # Top spacer
        self.add_widget(Label(size_hint_y=0.2))

        # Input box (CENTER)
        self.input = TextInput(
            hint_text="Enter Consignor Name",
            size_hint=(1, None),
            height=48,
            multiline=False
        )
        self.add_widget(self.input)

        # Search button
        btn = Button(
            text="Search",
            size_hint=(1, None),
            height=48
        )
        btn.bind(on_press=self.search)
        self.add_widget(btn)

        # Middle spacer
        self.add_widget(Label(size_hint_y=0.1))

        # Result area (BOTTOM, SCROLLABLE)
        self.scroll = ScrollView(size_hint=(1, 1))
        self.result = Label(
            text="",
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        # Auto height & wrap text
        self.result.bind(
            texture_size=lambda i, s: setattr(i, 'height', s[1])
        )
        self.result.bind(
            width=lambda *x: self.result.setter(
                'text_size', (self.result.width, None)
            )
        )

        self.scroll.add_widget(self.result)
        self.add_widget(self.scroll)

    # ---------- SEARCH LOGIC ----------
    def search(self, instance):
        try:
            df = pd.read_excel("/storage/emulated/0/ConsignorApp/data.xlsx")
            name = self.input.text.strip()

            if not name:
                self.result.text = "Please enter consignor name"
                return

            filtered = df[df['Consignor'].str.contains(name, case=False, na=False)]

            if filtered.empty:
                self.result.text = "No data found"
                return

            output = ""
            for _, r in filtered.iterrows():
                output += (
                    f"GR No : {r['Goods Receipt No']}\n"
                    f"Date : {r['G.R. Date']}\n"
                    f"Destination : {r['Destination']}\n"
                    f"Branch : {r['Branch']}\n"
                    f"Consignee : {r['Consignee']}\n"
                    "----------------------------\n"
                )

            self.result.text = output

        except Exception as e:
            self.result.text = f"Error:\n{e}"


# ---------- APP ----------
class ConsignorApp(App):
    def build(self):
        return MainLayout()


# ---------- RUN ----------
ConsignorApp().run()
