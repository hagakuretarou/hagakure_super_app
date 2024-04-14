import streamlit as st
from faker import Faker
import streamlit as st
import requests
# import matplotlib.pyplot as plt

#チーム1
def fetch_weather_data(city_id):
    url = f"https://weather.tsukumijima.net/api/forecast/city/{city_id}"
    response = requests.get(url)
    data = response.json()
    return data

#チーム1
def display_weather(data):
    st.write(f"### {data['location']['city']} の天気予報")
    st.write(f"#### {data['title']}")
    for forecast in data['forecasts']:
        st.write(f"**{forecast['dateLabel']} ({forecast['date']}): {forecast['telop']}**")
        if forecast['temperature']['min'] or forecast['temperature']['max']:
            min_temp = forecast['temperature']['min']['celsius'] if forecast['temperature']['min'] else '不明'
            max_temp = forecast['temperature']['max']['celsius'] if forecast['temperature']['max'] else '不明'
            st.write(f"最低気温: {min_temp}°C, 最高気温: {max_temp}°C")

#チーム1
# def plot_temperature(data):
#     dates = [forecast['date'] for forecast in data['forecasts']]
#     min_temps = [float(forecast['temperature']['min']['celsius']) if forecast['temperature']['min'] else None for forecast in data['forecasts']]
#     max_temps = [float(forecast['temperature']['max']['celsius']) if forecast['temperature']['max'] else None for forecast in data['forecasts']]
#     plt.figure(figsize=(10, 5))
#     plt.plot(dates, min_temps, label='最低気温', marker='o')
#     plt.plot(dates, max_temps, label='最高気温', marker='o')
#     plt.xlabel('日付')
#     plt.ylabel('温度 (°C)')
#     plt.title(f"{data['location']['city']} の温度予測")
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     plt.tight_layout()
#     return plt

def app():
    st.title("HAGAKUREの凄いアプリです")
    st.image("hagakurekun.png",width=200)
    tab1,tab2 = st.tabs(["日本の天気予報アプリ","職業探し"])
    with tab1:
        st.write("page1です")
        st.text("ここをチーム１が編集します!")
        st.title('日本の天気予報アプリ')
        st.link_button('市町村コード一覧','https://weather.tsukumijima.net/primary_area.xml')
        city_id = st.text_input('市町村コードを入力', '400040')
        if st.button('天気を表示'):
            weather_data = fetch_weather_data(city_id)
            display_weather(weather_data)
            # plot_temperature(weather_data)
    with tab2:
        st.title("あなたの適職は？")
        fake = Faker("jp-JP")
        name = st.text_input("名前を入力してください")
        if name is not "":
            fakejob = fake.job()
            st.text(f"{name}さんの適職は、{fakejob}です。")
if __name__ == '__main__':
    app()