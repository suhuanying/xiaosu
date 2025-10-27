import streamlit as st
st.set_page_config(page_title="个人简历生成器", page_icon='👩‍🎨')
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
     
