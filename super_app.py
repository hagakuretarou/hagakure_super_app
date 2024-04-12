import streamlit as st
def app():
    st.title("HAGAKUREの凄いアプリです")
    st.image("hagakurekun.png",width=200)
    tab1,tab2 = st.tabs(["page1","page2"])
    with tab1:
        st.write("page1です")
        st.text("ここをチーム１が編集します!")
    with tab2:
        st.write("page2です")
        st.text("ここをチーム２が編集します!")
if __name__ == '__main__':
    app()