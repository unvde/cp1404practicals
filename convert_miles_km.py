from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = "0.0 km"
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.2f} km"

    def handle_increment(self, change):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()


MilesConverterApp().run()
