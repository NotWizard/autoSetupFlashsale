#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Jie Xiang'

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import datetime
# import requests
startTime = ['10',  '13',  '16']

productsID = "12612 12555 12520 6669 8615 12473 12514 12161 11921"


def cutUpID(IDString):
    doneString = IDString.split(" ")
    return doneString


def setEventAndEveryTime(eventTime):
    # 新增活动
    chromeBrowser.find_element_by_xpath(
        '//*[@class="operator-container"]/button').click()

    time.sleep(1)
    # 设定名称和日期
    # 获取当前日期
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-input el-input--medium"]/input').send_keys(
            str(tomorrow))
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-form-item__content"]/div/input').send_keys(
            str(tomorrow))

    # 点击折叠日期span
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-form-item is-required"]/label').click()

    time.sleep(1)
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-dialog__footer"]/span/button[2]/span').click()

    for i in eventTime:
        # 点击添加活动时段
        time.sleep(2)
        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr/td[4]/div/button'
        ).click()
        time.sleep(1)

        # 设置开始时间
        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-date-editor el-input el-input--prefix el-input--suffix el-date-editor--time"]/input'
        ).click()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-date-editor el-input el-input--prefix el-input--suffix el-date-editor--time"]/input'
        ).clear()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-date-editor el-input el-input--prefix el-input--suffix el-date-editor--time"]/input'
        ).send_keys(('%s:00' % i))
        time.sleep(1)

        # 点击确定折叠开始时间的span
        chromeBrowser.find_element_by_xpath(
            '//*[@class="filter-container"]/div[3]/div/div[2]/div/form/div/label'
        ).click()
        time.sleep(1)

        # 设置结束时间
        chromeBrowser.find_element_by_xpath(
            '//*[@class="filter-container"]/div[3]/div/div[2]/div/form/div[2]/div/div/input'
        ).click()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="filter-container"]/div[3]/div/div[2]/div/form/div[2]/div/div/input'
        ).clear()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="filter-container"]/div[3]/div/div[2]/div/form/div[2]/div/div/input'
        ).send_keys('23:59')
        time.sleep(1)

        # 点击确认
        chromeBrowser.find_element_by_xpath(
            '//*[@class="filter-container"]/div[3]/div/div[3]/span/button[2]'
        ).click()
        time.sleep(1)


def setProductsInTimePoints(products):

    products1_3 = products[:3]
    products4_6 = products[3:6]
    products7_9 = products[6:]
    for i in range(1, len(products1_3) + 1):
        # 折叠打开最新活动
        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-table el-table--fit el-table--border el-table--enable-row-transition"]/div[3]/table/tbody/tr/td/div/div'
        ).click()
        time.sleep(1)

        if i == 1:
            # 点击商品管理
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[2]/td/div/div[2]/button[2]'
            ).click()
            time.sleep(2)
            for j in range(1, len(products7_9) + 1):
                # 点击新增
                chromeBrowser.find_element_by_xpath(
                    '//*[@class="app-container"]/div/div/button').click()
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="editGoodsGounp"]/form/div/div/div/input'
                ).send_keys(products7_9[j-1])
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="filter-container"]/div[2]/div/div[3]/span/button[2]'
                ).click()
                time.sleep(2)

            chromeBrowser.back()
            time.sleep(2)

        elif i == 2:
            # 点击商品管理
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[2]/td/div[%s]/div[2]/button[2]'
                % i).click()
            time.sleep(2)

            for k in range(1, len(products4_6) + 1):
                # 点击新增
                chromeBrowser.find_element_by_xpath(
                    '//*[@class="app-container"]/div/div/button').click()
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="editGoodsGounp"]/form/div/div/div/input'
                ).send_keys(products4_6[k-1])
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="filter-container"]/div[2]/div/div[3]/span/button[2]'
                ).click()
                time.sleep(2)

            chromeBrowser.back()
            time.sleep(2)

        else:
            # 点击商品管理
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[2]/td/div[%s]/div[2]/button[2]'
                % i).click()
            time.sleep(2)

            for l in range(1, len(products1_3) + 1):
                # 点击新增
                chromeBrowser.find_element_by_xpath(
                    '//*[@class="app-container"]/div/div/button').click()
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="editGoodsGounp"]/form/div/div/div/input'
                ).send_keys(products1_3[l-1])
                time.sleep(1)

                chromeBrowser.find_element_by_xpath(
                    '//*[@class="filter-container"]/div[2]/div/div[3]/span/button[2]'
                ).click()
                time.sleep(2)

            chromeBrowser.back()
            time.sleep(2)


if __name__ == "__main__":

    chromeBrowser = webdriver.Chrome()
    # chromeBrowser.get('https://admin.fingo.shop/#/operation/timeLimitList')
    chromeBrowser.get('https://admin.fingo.shop')
    time.sleep(2)

    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div/div/div/input').send_keys(
            'Dean')
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[2]/div/div/input').send_keys(
            'fingo666')
    # 点击登陆
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[3]/div/button').click()

    time.sleep(3)

    # 点击折叠打开运营管理
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[8]/div').click()

    time.sleep(1)
    # 跳转限时特价
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[8]/ul/li[6]/a/span').click()
    time.sleep(1)

    setEventAndEveryTime(startTime)

    setProductsInTimePoints(cutUpID(productsID))
