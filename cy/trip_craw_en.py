from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
import csv
n=0
'''url_str = "https://www.tripadvisor.co.kr/Restaurant_Review-g294197-d1174982-Reviews-or"
url_num = str(0)
url_keyword = "-Tosokchon_Samgyetang-Seoul.html"
total_url = url_str + url_num + url_keyword

driver = webdriver.Chrome("C:/Users/gkxmr/py_workspace/chromedriver.exe")
driver.get(total_url) # 위에서 url을 지정해주었다
time.sleep(3)
driver.find_elements(By.CSS_SELECTOR,".ulBlueLinks")[0].click()'''
#https://www.tripadvisor.co/Hotel_Review-g294197-d659341-Reviews-Yeouido_Park_Centre_Seoul_Marriott_Executive_Apartments-Seoul.html
#https://www.tripadvisor.com/Attraction_Review-g294197-d4798715-Reviews-or10-Yeouido_Hangang_Park-Seoul.html
csvFile = open("reviews_Tosokchon.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['Score','Review'])
#https://www.tripadvisor.com/Attraction_Review-g294197-d1379963-Reviews-or10-Bukchon_Hanok_Village-Seoul.html
#https://www.tripadvisor.com/Attraction_Review-g294197-d1379963-Reviews-or10-Bukchon_Hanok_Village-Seoul.html
for i in range(0,5):
    k=0
    url_str = "https://www.tripadvisor.com/Restaurant_Review-g294197-d1174982-Reviews-or"
    url_num = str(n)
    url_keyword = "-Tosokchon_Samgyetang-Seoul.html"
    total_url = url_str + url_num + url_keyword

    '''url_str = "https://www.tripadvisor.com/Attraction_Review-g294197-d1379963-Reviews-or"
    url_num = str(n)
    url_keyword = "-Bukchon_Hanok_Village-Seoul.html"
    total_url = url_str + url_num + url_keyword'''
    driver = webdriver.Chrome("C:/Users/gkxmr/py_workspace/chromedriver.exe")
    driver.get(total_url) # 위에서 url을 지정해주었다
    time.sleep(3)
    #rating_code = reviews[k].find_element(By.CSS_SELECTOR,".ui_bubble_rating")
    driver.find_elements(By.CSS_SELECTOR,".ulBlueLinks")[0].click()

    #f=open("C:/Users/gkxmr/py_workspace/yeouido_park.txt","a",encoding="utf-8")
    print("hi")
    n=n+15
    for j in range(0,14):
        time.sleep(10)
        reviews = driver.find_elements(By.CSS_SELECTOR,".review-container")
        #평점
        rating_code = reviews[k].find_element(By.CSS_SELECTOR,".ui_bubble_rating")
        cls_attr = rating_code.get_attribute("class")
        cls_attr = str(cls_attr).split("ui_bubble_rating bubble_")
        reviews[0].find_element(By.CSS_SELECTOR,".ui_bubble_rating").get_attribute("class")

        score = str(cls_attr[1])
        print(score)

        time.sleep(3)
        #리뷰네
        Temp_review = reviews[k].find_element(By.CSS_SELECTOR,".partial_entry").text
        time.sleep(3)
        review = Temp_review.replace("\n"," ")
        print(review)

        #f.write("평점"+score)
        #f.write("\n\n")
        #f.write("리뷰: "+review)
        csvWriter.writerow((score,review))
        k=k+1

#f.close()
