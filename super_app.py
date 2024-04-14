import streamlit as st
from faker import Faker

def app():
    st.title("HAGAKUREの凄いアプリです")
    st.image("hagakurekun.png",width=200)
    tab1,tab2 = st.tabs(["page1","職業探し"])
    with tab1:
        st.write("page1です")
        st.text("ここをチーム１が編集します!")
    with tab2:
        st.title("あなたの適職は？")
        fake = Faker("jp-JP")
        name = st.text_input("名前を入力してください")
        if name is not "":
            fakejob = fake.job()
            st.text(f"{name}さんの適職は、{fakejob}です。")
if __name__ == '__main__':
    app()