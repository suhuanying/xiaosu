import streamlit as st
import random
st.set_page_config(page_title='音乐播放器', page_icon='🎼')
st.title("🎼简易音乐播放器")
st.text("使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

images=[
    {
        'title':'专辑封面',
        'name':'屋顶',
        'artist':'周杰伦',
        'duration':'5:19',
        'url':'https://p2.music.126.net/81BsxxhomJ4aJZYvEbyPkw==/109951165671182684.jpg?param=180y180',
        'audio':'https://music.163.com/song/media/outer/url?id=5257138.mp3'
    },
    {   'title':'专辑封面',
        'name':'不将就',
        'artist':'李荣浩',
        'duration':'5:12',
        'url':'https://p1.music.126.net/e-Uc6W3Kug-HFHJ5nvCUPg==/109951166562828988.jpg?param=180y180',
        'audio':'https://music.163.com/song/media/outer/url?id=31654343.mp3'
    },
    {   'title':'专辑封面',
        'name':'他不懂',
        'artist':'张杰',
        'duration':'3:55',
        'url':'https://p1.music.126.net/mW53BkMgGy37I7yVrUg-aQ==/109951163117902077.jpg?param=180y180',
        'audio':'https://music.163.com/song/media/outer/url?id=28059417.mp3'
    }
]
#讲ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
if 'ind'not in st.session_state:
    st.session_state['ind']=1

#define:定义
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)
def prevImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(images)


def random_song():
    # 用for循环筛选，实现随机播放
    current_ind = st.session_state["ind"]
    available_inds = [i for i in range(len(images)) if i != current_ind]
    st.session_state["ind"] = random.choice(available_inds)
    

a1, a2 = st.columns([1,2])
with a1:
    #st.image()总共两个参数，url:图片地址 caption:图片的备注
    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['title'])

with a2:
    st.header(images[st.session_state['ind']]['name'])
    st.subheader(f"歌手：{images[st.session_state['ind']]['artist']}")
    st.caption(f"时长：{images[st.session_state['ind']]['duration']}")
    st.audio(images[st.session_state['ind']]['audio'])
    

#将一行分成两列
c1,c2,c3=st.columns(3)

with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('⏪上一首',on_click=prevImg,use_container_width=True)
with c2:    
#st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('⏩下一首',on_click=nextImg,use_container_width=True)
with c3:    
#st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button("🔀随机播放", on_click=random_song)
