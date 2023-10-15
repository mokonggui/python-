# 操控浏览器
from selenium import webdriver
# 保存爬取数据csv格式
import csv
def paQufun(a):
    # 输入查找内容
    #a = input("请输入要查找的内容：")
    f = open('./data/' + a + '.csv', mode='a', encoding='utf-8', newline='')
    data = csv.DictWriter(f, fieldnames=['招聘职业', '地区', '公司', '薪资', '工作经验要求', '学历要求', '工作介绍', '公司福利', '详情页'])
    # 写入表头
    data.writeheader()
    # 实例化浏览器
    driver = webdriver.Chrome()
    #driver.get('https://www.zhaopin.com/nanchang/')
    driver.get('https://www.zhipin.com/web/geek/job?query=&city=101240100')
    # 隐式等待
    driver.implicitly_wait(10)
    find = driver.find_element('css selector', ' .search-input-box .input')
    driver.find_element('css selector', ' .search-input-box .input').send_keys(a)
    # 点击搜索
    driver.implicitly_wait(10)
    driver.find_element('css selector', '.search-btn').click()
    # css选择器直接定位元素
    # 两次提取，第一次获取li标签内容
    lists = driver.find_elements('css selector', '.search-job-result li.job-card-wrapper')
    # 返回列表，列表里元素
    for li in lists:
        # 招聘职业
        job = li.find_element('css selector', ' .job-name').text
        # 地区
        area = li.find_element('css selector', ' .job-area').text
        # 公司
        company = li.find_element('css selector', ' .company-name').text
        # 薪资
        salary = li.find_element('css selector', ' .salary').text
        # 工作经验学历要求
        yao = li.find_element('css selector', ' .job-info.clearfix .tag-list').text
        lines = yao.split("\n")
        # 工作经验要求
        line1 = lines[0]
        # 学历要求
        line2 = lines[1]
        # 工作介绍
        jie = li.find_element('css selector', ' .job-card-footer.clearfix  .info-desc').text
        # 公司福利
        fuLi = li.find_element('css selector', '  .job-card-footer.clearfix  .tag-list').text
        # 详情页链接
        href = li.find_element('css selector', '  .job-card-left').get_attribute('href')
        # 创建字典写入数据
        dit = {
            '招聘职业': job,
            '地区': area,
            '公司': company,
            '薪资': salary,
            '工作经验要求': line1,
            '学历要求': line2,
            '工作介绍': jie,
            '公司福利': fuLi,
            '详情页': href,
        }
        # 保存数据到data.csv
        data.writerow(dit)
        # 控制台查看爬取的数据
        print(job, area, company)
        print(salary, line1, line2, jie, fuLi, href)
        print('\n')
