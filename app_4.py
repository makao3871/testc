import streamlit as st
import tkinter
from tkinter import filedialog
import pandas as pd
from ShiftScheduler import ShiftScheduler

st.sidebar.title("データのアップロード")

secect_file_cal=st.sidebar.file_uploader("カレンダー")
secect_file_staff=st.sidebar.file_uploader("スタッフ")

st.title("シフトスケジューリングアプリ")

tab_titles=["カレンダー情報","スタッフ情報","シフト表作成"]
tab1,tab2,tab3=st.tabs(tab_titles)

with tab1:
    st.header("カレンダー情報") 
    if secect_file_cal is not None:
        df_cal=pd.read_csv(secect_file_cal)
        st.write(df_cal)

with tab2:
    st.header("スタッフ情報")
    if secect_file_staff is not None:
        df_staff=pd.read_csv(secect_file_staff)
        st.write(df_staff)

with tab3:
    st.header("シフト表作成")