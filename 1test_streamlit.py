import streamlit as st
import time # 업로드 중 오류 방지위해 대기 시간 걸기
from PIL import Image
#from datetime import date
#today = date.today()

st.title(':blue[Deepfake Police] :cop:')
st.subheader('안녕하세요 딥페이크 잡는 경찰 DP 입니다')
#st.write(today)

deepcleansing = st.checkbox('DP의 서비스인 Deep Cleansing 사용 전에 안내문을 읽으시려면 체크해주세요')

if deepcleansing:
    st.markdown('**:blue[Deep Cleansing]** 서비스 사용 전에, 웹사이트의 **결과는 100% 정확하지 않을 수 있고**,')
    st.markdown('이에 따른 **모든 책임은 본인**에게 있음을 인지하셨으면 동의를 눌러주세요')
    agree = st.selectbox('동의하시나요?', (' ', '동의합니다', '동의하지 않습니다'))

    if agree == '동의합니다':
        st.subheader('영상을 업로드 해주세요 :video_camera:', divider='rainbow')

        file = st.file_uploader("영상 파일 선택(img or mp4 or avi)", type=['mp4','avi','jpeg','png'])

        if file is not None:
            ext = file.name.split('.')[-1]

            if ext in ["png", "jpg", "jpeg"]:
                # 이미지 파일 로드
                image = Image.open(file)
                # 출력
                st.image(image, caption=file.name)

            elif ext in ['mp4', 'avi']:
                # 영상 파일 로드
                video_file = open(file.name, 'rb')
                video_bytes = video_file.read()
                # 출력
                st.video(video_bytes)

    elif agree == '동의하지 않습니다':
        st.markdown('**:red[죄송합니다 :blue[Deep Cleansing] 서비스를 이용하실 수 없습니다]**')

#if deepcleansing:
#    st.markdown('**:blue[Deep Cleansing]** 서비스 사용 전에, 웹사이트의 **결과는 100% 정확하지 않을 수 있고**,')
#    st.markdown('이에 따른 **모든 책임은 본인**에게 있음을 인지하셨으면 동의를 눌러주세요')
#    agree = st.selectbox('동의하시나요?', (' ', '동의합니다', '동의하지 않습니다'))
#
#    if agree == '동의하지 않습니다':
#        st.markdown('**:red[죄송합니다 서비스를 이용하실 수 없습니다]**')
#
#    if agree == '동의합니다':
#        st.subheader('영상을 업로드 해주세요 :video_camera:', divider='rainbow')
#
#        file = st.file_uploader("영상 파일 선택(img or mp4 or avi)", type=['mp4','avi','jpeg','png'])
#
#        if file is not None:
#            ext = file.name.split('.')[-1]
#
#            if ext in ["png", "jpg", "jpeg"]:
#                # 이미지 파일 로드
#                image = Image.open(file)
#                # 출력
#                st.image(image, caption=file.name)
#
#            elif ext in ['mp4', 'avi']:
#                # 영상 파일 로드
#                video_file = open(file.name, 'rb')
#                video_bytes = video_file.read()
#                # 출력
#                st.video(video_bytes)
