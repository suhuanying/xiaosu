import streamlit as st
import pandas as pd
import numpy as np

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
