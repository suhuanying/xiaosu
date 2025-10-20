import streamlit as st
import pandas as pd
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

