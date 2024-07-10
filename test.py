import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtGui import QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.city_combobox = QComboBox()
        self.city_combobox.addItem("New York")
        self.city_combobox.addItem("Los Angeles")
        self.city_combobox.addItem("London")
        self.city_combobox.addItem("Tokyo")
        self.city_combobox.addItem("Bordeaux")
        
        self.weather_label = QLabel("Weather: ")
        self.icon_label = QLabel()
        
        layout.addWidget(self.city_combobox)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.icon_label)

        self.city_combobox.currentIndexChanged.connect(self.update_weather)

        self.setLayout(layout)
        
    def update_weather(self):
            selected_city = self.city_combobox.currentText()
            api_key = "a05023811057f42d3deaacb56db33dda"  # Replace with your OpenWeatherMap API key
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={selected_city}&appid={api_key}&units=metric"

            response = requests.get(api_url)
            data = response.json()

            if data["cod"] == 200:
                weather_description = data["weather"][0]["description"]
                icon_id = data["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"

                self.weather_label.setText(f"Weather: {weather_description}")
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(icon_url).content)
                self.icon_label.setPixmap(pixmap)
            else:
                self.weather_label.setText("Weather data not available")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.setWindowTitle("Weather App")
    window.show()
    sys.exit(app.exec_())