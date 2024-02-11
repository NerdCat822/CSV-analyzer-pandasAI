from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use("TkAgg")

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)

st.title("CSV 파일 분석기 with PandasAI")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요. (csv 파일형식만 지원)", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt = st.text_area("프롬프트를 입력하세요:")

    if st.button("답변 생성"):
        if prompt:
            with st.spinner("응답을 생성중입니다..."):
                st.write(pandas_ai.run(df, prompt=prompt))
        else:
            st.warning("프롬프트를 다시 입력하세요.")