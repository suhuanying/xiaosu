import streamlit as st
st.set_page_config(page_title='动物园', page_icon='🐶')
# 图片数组
images =[
    {
         'url':"https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg",
         'parm':'小型白犬'
     },
    {
         'url':"https://housing.com/news/wp-content/uploads/2023/07/Cute-dog-breeds-that-make-the-best-pets-f-686x400.jpg",
         'parm':'拉布拉多'
    },
    {
         'url':"https://wagbrag.com/wp-content/uploads/2016/04/dog-1194077_1280.jpg",
          'parm':'金毛'
    },
    {
         'url':"https://www.holidaysmart.com/sites/default/files/dailyimage/og/2022/cat-scottish-fold-day.jpg",
         'parm':'小猫'
    },
    {
         'url':"https://images2.alphacoders.com/121/1213770.jpg",
         'parm':'猫'
    }
]

#讲ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
if 'ind'not in st.session_state:
    st.session_state['ind']=0



#define:定义
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)
def prevImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(images)

#st.image()总共两个参数，url:图片地址 caption:图片的备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

#将一行分成两列
c1,c2=st.columns(2)

with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一张',on_click=prevImg,use_container_width=True)
with c2:    
#st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一张',on_click=nextImg,use_container_width=True)


