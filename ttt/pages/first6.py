import streamlit as st
import random
st.set_page_config(page_title='视频网站', page_icon='📺')


st.title('动画片🍒🍒🍒🦖🦖')

#视频网址
video_url=[{
    'url':'樱桃小丸子1.mp4',
    'title':'樱桃小丸子🍒',
    'episode':'1'
    },{
    'url':'樱桃小丸子2.mp4',
    'title':'樱桃小丸子🍒',
    'episode':'2'
    },{
    'url':'奶龙.mp4',
    'title':'奶龙🦖',
    'episode':'3'}
]

if'ind'not in st.session_state:
    st.session_state['ind']=0
st.header(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['episode']+'集')




# 显示当前集数的视频
st.video(video_url[st.session_state['ind']]['url'])

c1,c2,c3,c4=st.columns(4)


def play(arg):
    #点击哪个按钮，就播放第几集
   
    #将ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置

    st.session_state['ind'] = int(arg)

for i in range(len(video_url)):
    st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))





