import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("所有实训作业")
tab1, tab2, tab3 ,tab4,tab5,tab6= st.tabs(["数字档案", "南宁美食数据仪表", "相册","音乐播放器","视频网站","个人简历生成器"])
with tab1:
    st.title("👍学生 小苏-数字档案👩‍🎓")
    st.header("🕶基础信息",help="这是我的基本信息")
    st.image("https://cdn.pixabay.com/photo/2016/02/18/18/37/puppy-1207816_1280.jpg")
    st.text("学号：23031310137")
    st.markdown("**注册时间：**:green[2023-9-1]")
    st.markdown("**班级：**:green[23高本数管1班]")
    st.markdown("**当前教室：**:green[实训楼204]|**安全等级：**:green[绝密]")

    st.header("🗺技能矩阵",help="C语言")
    import streamlit as st # 导入Streamlit并用st代表它
    import pandas as pd

    st.subheader("🕶技能")
    # 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="5%", delta="2%")
    c2.metric(label="python", value="70%", delta="5%")
    c3.metric(label="java", value="3%", delta="2%", delta_color="off")


    st.subheader('😄😄😄Streamlit课程进度')
    st.metric(label="Streamlit课程进度", value="30%", delta="10", label_visibility='hidden')


    # 定义数据,以便创建数据框
    data = {
        '日期':['2025-10-01','2025-10-15','2025-10-20'],
        '任务':['学生数字档案','课程管理系统','数据图表展示'],
        '状态':['完成✔️','进行中','未完成❎'],
        '难度':['🟡🟡','🟡','🟡🟡🟡']
    }

    # 定义数据框所用的索引
    index = pd.Series(['0', '1', '2'], name='  ')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.subheader('任务日志👒')
    st.table(df)
    st.header("最新代码成果")
    str='''
    a=30
    b=20
    print(a+b)
    '''
    st.code(str,language=None)
    st.caption("这是一段python代码")
    st.code(str,language="python",line_numbers=True)

    st.markdown('****************************')
    st.markdown("#### **现状态：混乱中**")
    st.markdown(':green[>>>SYSTEH MESSAGE:]下一个任务目标')
    st.markdown(':green[>>>TARGET:]课程管理系统')
    st.markdown(':green[>>>COUNTDOWN:]2025年10月20日11:55:54')
    st.markdown("#### **连接状态：已加密**")

with tab2:
    st.title("🍹南宁奶茶探索🔍")
    st.text("探索广西南宁最受欢迎的奶茶地点！选择你感兴趣的奶茶类型，查看评分和位置")
    st.header("📍南宁奶茶地图")

#准备地图坐标点数据(latitude纬度，longitute经度)
    map_data = {
        'latitude': [22.839794,22.869532,22.814561,22.822034,22.807240],
        'longitude': [108.245544,108.291550,108.322884,108.327341,108.335710]
        }

    st.map(pd.DataFrame(map_data))
# 定义数据,以便创建数据框
    data = {
        '蜜雪冰城':[15,25,4,10,13,18,11,12,16,20,6,9],
        '古茗':[12,10,15,25,19,17,14,12,16,20,18,23],
        '沪上阿姨':[11,10,20,16,18,14,17,19,25,23,12,15],
        '霸王茶姬':[23,26,28,25,31,35,67,18,22,18,19,28],
        '瑞幸':[20,15,18,25,22,19,28,16,13,23,26,30]
    }
# 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
# 定义数据框所用的新索引
    index = pd.Series(['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'], name='月份')
# 将新索引应用到数据框上
    df.index = index

#展示数据
    st.dataframe(df)
    st.table(df)

#折线图
    st.header("💰不同类型奶茶价格")
    st.line_chart(df)

    st.header("⏱️用餐高峰时段")
    peak_hours = pd.DataFrame({
         '时段': ['10点', '12点', '14点', '16点', '18点', '20点', '22点'],
          '蜜雪冰城': [50, 80, 40, 60, 120, 90, 30],
          '古茗': [40, 70, 35, 55, 110, 85, 25],
         '沪上阿姨': [35, 65, 30, 50, 100, 80, 20],
         '霸王茶姬': [45, 75, 40, 60, 115, 95, 35],
         '瑞幸': [55, 85, 45, 65, 125, 100, 40]
         }).set_index('时段')           
    st.area_chart(peak_hours)

#柱状图
    st.header("⭐奶茶店评分")
    st.bar_chart(df)

    st.header("🥂奶茶店铺详情")
    def my_format_func(option):
        return f"店铺:{option}"

    milktea=st.selectbox('选择奶茶店查看详情:',["蜜雪冰城", "古茗", "沪上阿姨", "霸王茶姬", "瑞幸"],format_func=my_format_func,index=2)    
# 奶茶店数据
    restaurants_data = {
        "店铺": ["蜜雪冰城", "古茗", "沪上阿姨", "霸王茶姬", "瑞幸"],
        "类型": ["奶茶", "奶茶", "奶茶", "奶茶", "咖啡"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.839794,22.869532,22.814561,22.822034,22.807240],
        "longitude": [108.245544,108.291550,108.322884,108.327341,108.335710]
    }
    restaurants_df = pd.DataFrame(restaurants_data).set_index('店铺')
    st.dataframe(restaurants_df.loc[milktea])

    st.subheader('🚶当前拥挤程度')

    st.header("🎲今日奶茶推荐")

with tab3:
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

with tab4:
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

with tab5:
    st.title('动画片🍒🍒🍒🦖🦖')

#视频网址
    video_url=[{
        'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title':'樱桃小丸子🍒',
        'episode':'1'
        },{
        'url':'https://www.w3schools.com/html/movie.mp4',
        'title':'樱桃小丸子🍒',
        'episode':'2'
        },{
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
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
        st.button(f'第{i+1}集',use_container_width=True,on_click=play,args=([i]))


with tab6:
    st.title("🎨个人简历生成器")

#分两栏
    a1,a2 = st.columns([1, 2])
    with a1:
        st.subheader("个人信息表单")
        st.markdown("---")

        name = st.text_input("姓名")
        gender=st.radio('性别',['男','女','其他'],index=0)

        phone = st.text_input("电话")
        email = st.text_input("邮箱")
        job = st.text_input("职位")
        dob=st.text_input("出生日期")

        position=st.selectbox("位置", ["对抗路", "中路", "发育路"])
        education_options=st.selectbox('学历',['高中','本科','硕士','博士','其他'])

#自定义format_func函数,多选
        def my_format_func(option):
            return f'{option}'
        lang_options= st.multiselect('语言能力',['中文','英语','日语','意大利语','其他'])

        def my_format_func(option):
            return f'{option}'
        skill_options= st.multiselect('技能',['治愈微笑','绽放之舞','甜蜜恋风','星华缭乱'])


        age = st.slider("年龄", min_value=18, max_value=90, value=25)
        job_experience = st.slider("工作经验", min_value=18, max_value=60, value=25)

        st.subheader("个人简介")
        introduction = st.text_area("请输入你的个人简介（如技能、经历等）", height=100)
    
        from datetime import datetime, time
        w1 = st.time_input("每日最佳联系时段")
        st.write("你选择时间1是:", w1)


        photo=st.file_uploader('上传个人照片')
        if photo is not None:
            bytes_data=photo.getvalue()
    

    with a2:
        st.subheader("简历实时预览")
        st.markdown("---")  # 分隔线

        c1,c2 = st.columns([1, 1])
        with c1:
            st.markdown(f"### {name}")
            if photo:
                st.image(photo,width=300)
            st.markdown(f"- 职位：{job}")
            st.markdown(f"- 性别：{gender}")
            st.markdown(f"- 年龄：{age} 岁")
            st.markdown(f"- 电话：{phone}")
            st.markdown(f"- 邮箱：{email}")
        with c2:
            st.markdown(f"- 学历：{education_options}")
            st.markdown(f"- 位置：{position}")
            st.markdown(f"- 工作经验：{job_experience}")
            skill_text = ', '.join(skill_options) if skill_options else "无"
            st.write('技能：', skill_text)
        
        # 语言能力：用逗号分隔
            lang_text = ', '.join(lang_options) if lang_options else "无"
            st.write('语言能力：', lang_text)
       
        

        st.markdown("------")  # 分隔线
        st.subheader("👧个人简介")
        if introduction:
            st.markdown(introduction.replace("\n", "<br>"), unsafe_allow_html=True)  # 支持换行
        else:
            st.markdown("（请在左侧填写个人简介）")
     


    



    
     
