import streamlit as st
import pandas as pd

st.set_page_config(page_title="医薬品名検索アプリ", page_icon="💊")

st.title("💊 医薬品名検索アプリ")
st.write("一般名または製品名を入力すると、対応する名前を表示します。")

# CSVを読み込む（ファイル名は必要に応じて変更）
@st.cache_data
def load_data():
    return pd.read_csv("med_list.csv")

df = load_data()

# ユーザーの入力
user_input = st.text_input("医薬品名を入力してください（一般名または製品名）", "").strip()

# 検索と表示
if st.button("検索"):
    if user_input:
        result = df[df["一般名"].str.contains(user_input, case=False, na=False)]
        if not result.empty:
            st.success("🔍 一般名でヒットしました！")
            for i, row in result.iterrows():
                st.write(f'💊 製品名：**{row["製品名"]}**（一般名：{row["一般名"]}）')
        else:
            result = df[df["製品名"].str.contains(user_input, case=False, na=False)]
            if not result.empty:
                st.success("🔍 製品名でヒットしました！")
                for i, row in result.iterrows():
                    st.write(f'💊 一般名：**{row["一般名"]}**（製品名：{row["製品名"]}）')
            else:
                st.error("該当する医薬品が見つかりませんでした。")
