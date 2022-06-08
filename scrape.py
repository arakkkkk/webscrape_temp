import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import traceback
import re
import os
import copy
import sys
import datetime


# https://qiita.com/motoki1990/items/a59a09c5966ce52128be
def run_scrape(d_today, path):
    scrape_url = ''
    for i in range(0, 6):
	    options = webdriver.ChromeOptions()
	    # デフォルトダウンロードフォルダを変更する
	    options.add_experimental_option(
	        "prefs", {"download.default_directory": path + 'data'})
	    # 自動テストソフトウェアによって制御されていますというメッセージを非表示にする
	    options.add_experimental_option("excludeSwitches", ["enable-automation"])
	    # 拡張機能の自動更新をさせない（アプリ側の自動アップデートとドライバーの互換性によるエラーを回避）
	    options.add_experimental_option('useAutomationExtension', False)
		# ヘッドレスモードの設定
		option.add_argument('--headless')
	    driver = webdriver.Chrome()
        driver.get('https://google.com')
	    try:
	        driver.implicitly_wait(5)
	        driver.get(scrape_url)
	        driver.find_element_by_tag_name('body').click()
	        for i in range(5):
	            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
	        time.sleep(3)
	        # JavaScrptの実行
	        # # downloadのdropdownをクリックして開く
	        # elements = driver.find_elements_by_xpath(
	        #     '//*[@id="Download"]/div/div[2]')
	        # elements[0].click()
	        time.sleep(10)
	    except:
	        traceback.print_exc()
	        driver.quit()
	        return
	    finally:
	        driver.quit()


if __name__ == "__main__":
    d_today = str(datetime.date.today())
    path = '/Users/Kouiti/local_file/glycovid/'
    run_scrape(d_today, path)
