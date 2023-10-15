import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def chuLifun(a):
    # 设置中文字体
    font = FontProperties(fname='仿宋_GB2312.ttf', size=14)
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文字体为宋体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    #a = input("请输入要处理内容名字：")
    # 读取要处理CSV文件
    df = pd.read_csv('./data/' + a + '.csv', encoding='utf-8')

    # 计算每个类别的总数
    counts = df['薪资'].value_counts()
    # 创建一个饼图 counts 是数据， counts.index 是标签，autopct = '%1.1f%%' 表示显示百分比
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
    # 添加标题
    plt.title('Salary Distribution')
    # 保存图形
    plt.savefig('./image/' + a + '工资扇形图.png')
    # 显示图形
    plt.show()

    # 绘制学历要求柱形图
    counts = df['学历要求'].value_counts()
    plt.bar(counts.index, counts.values)
    # 添加标题和标签
    plt.title('Salary')
    plt.xlabel('学历要求', fontproperties=font)
    plt.ylabel('个数', fontproperties=font)
    # 保存图形
    plt.savefig('./image/' + a + '学历要求.png')
    # 显示图形
    plt.show()

    # 绘制薪资柱形图
    counts = df['薪资'].value_counts()
    plt.bar(counts.index, counts.values)
    # 添加标题和标签
    plt.title('Salary')
    plt.xlabel('薪资', fontproperties=font)
    plt.ylabel('个数', fontproperties=font)
    # 保存图形
    plt.savefig('./image/' + a + 'salary.png')
    # 显示图形
    plt.show()

    # 将所有文本合并为一个字符串
    text = ' '.join(df['招聘职业'].tolist())
    # 创建词云对象
    wordCloud = WordCloud(font_path='仿宋_GB2312.ttf', width=800, height=800, background_color='white',
                          min_font_size=10).generate(text)
    # 绘制词云
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordCloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    # 保存图形
    plt.savefig('./image/' + a + '词云.png')
    plt.show()
