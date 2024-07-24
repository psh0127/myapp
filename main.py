import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import koreanize-matplotlib

# 데이터 불러오기
file_path = '202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(file_path, encoding='cp949')

# 중학생 연령대 (13~15세) 열 추출
middle_school_ages = ['2024년06월_계_13세', '2024년06월_계_14세', '2024년06월_계_15세']

st.title("지역별 중학생 인구 비율")

# 사용자로부터 지역 입력받기
region = st.text_input("지역을 입력하세요:", "서울특별시 종로구 (1111000000)")

if region:
    # 특정 지역의 데이터 필터링
    region_data = data[data['행정구역'] == region]
    
    if not region_data.empty:
        # 중학생 인구와 총인구 추출
        middle_school_population = region_data[middle_school_ages].sum(axis=1).values[0]
        total_population = region_data['2024년06월_계_총인구수'].values[0]

        # 중학생 인구 비율 계산
        middle_school_ratio = middle_school_population / total_population

        # 원 그래프 데이터
        labels = ['중학생 인구', '기타 인구']
        sizes = [middle_school_population, total_population - middle_school_population]
        colors = ['#ff9999', '#66b3ff']
        explode = (0.1, 0)  # 중학생 인구 비율 강조

        # 원 그래프 그리기
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # 원형 유지

        # 그래프 출력
        st.pyplot(fig1)
        st.write(f"지역: {region}")
        st.write(f"중학생 인구: {middle_school_population:,}명")
        st.write(f"총 인구: {total_population:,}명")
        st.write(f"중학생 인구 비율: {middle_school_ratio:.2%}")
    else:
        st.write("입력하신 지역에 대한 데이터가 없습니다.")
