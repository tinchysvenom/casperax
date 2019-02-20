# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:55:45 2019

@author: USER
"""


import re
import gc
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def post_summarizer(article):
    stopWords = ['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't",
    'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how',
    'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
    're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very',
    'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
    art_words = re.split("\W", article)
    sentence_list = article.split('.')
    #sentence_list = re.split(r"\.\s*", article)

    xab = {}
    for i in art_words:
        if i.lower() not in stopWords:
            if i not in xab.keys():
                xab[i] = 1
            else:
                xab[i] += 1 
        else:
            continue
    
    max_weight = max(xab.values())
    xac = {}
    for i in xab.keys():
        xac[i] = xab[i]/max_weight
    
    xad = {}
    for i in sentence_list:
        xae = 0
        split_k = re.split("\s|,", i)
        for l in split_k:
            if l in xac.keys():
                xae += xac[l]
            else: pass
        xad[i] = xae
    
    maxy = sorted(xad.values())
    maxx = maxy[-1]
    
    summary_list = []
    for i in xad.keys():
        if xad[i] == maxx:
            summary_list.append(i)
        else: pass

    summary = summary_list[-1]
    return(summary)
    del article, stopWords, art_words, sentence_list, i, xab, max_weight, xac, xad, l, xae, split_k, maxy, maxx, summary_list, summary
    gc.collect()
    
    
#3509, 3653, 3901, 3671, 3917, 3677, 3923, 3709, 3953, 3733, 3973, 3743, 3989, 3749, 3991   
post_targets = [2509, 2751, 2517, 2761, 2523, 2763, 2529, 2769, 2539, 2781, 2547, 2793, 2557, 2803, 2643, 2889]
post_var = 0
todays_post_target = post_targets[post_var]
sec_intervals = (54000/todays_post_target)
completed = 0
landage = 0
pager = 0
serum = False

while time.localtime()[3] <= 22 and time.localtime()[3] >= 7:
    tata = 0
    try:
        chrome_options = Options() #the code to open/connect to the site starts here, the code to handle the login goes here
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
        driver = webdriver.Chrome(executable_path="chromedriver",   options=chrome_options)
        driver.get("https://wakanda.ng/login")
        time.sleep(5)
            
        while tata < 5: #log in
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'nameField')))
                username = driver.find_element_by_id('nameField')
                ActionChains(driver).move_to_element(username).perform()
                username.click()
                username.clear()
                username.send_keys('Tinchysvenom')
                
                passiv = driver.find_element_by_id('passwordField')
                ActionChains(driver).move_to_element(passiv).perform()
                passiv.click()
                passiv.clear()
                passiv.send_keys('audaceusfortunaiuvat456')
                    
                logbut = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[1]/div/div/form/div[4]/button')
                ActionChains(driver).move_to_element(logbut).perform()
                logbut.click()
                break
            
            except:
                print('error at login section')
                try:
                    driver.switch_to.alert.dismiss()
                except:
                    driver.refresh()
                    tata += 1
                continue
        
        time.sleep(5)
        del username, passiv, logbut
        gc.collect()
        
        if tata >= 5:
            driver.quit()
            time.sleep(200)
            continue
        else: 
            tata = 0
            
        while tata < 5: #click post
            try:
                if serum == False:
                    first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                    la_herd = first_post_box.find_elements_by_class_name('item-details')
                    first_post = la_herd[completed].find_element_by_tag_name('a')
                    first_post.click()
                    time.sleep(2.5)
                    driver.refresh()
                else:
                    if pager == 0:
                        first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                        la_herd = first_post_box.find_elements_by_class_name('item-details')
                        first_post = la_herd[completed].find_element_by_tag_name('a')
                        first_post.click()
                        time.sleep(2.5)
                        driver.refresh()
                    else:
                        noci = 0
                        while noci < pager:
                            username = driver.find_element_by_class_name('blog')
                            passiv = username.find_elements_by_tag_name('a')
                            logbut = passiv[-1]
                            ActionChains(driver).move_to_element(logbut).perform()
                            logbut.click()
                            noci += 1
                                
                        del username, passiv, logbut, noci
                        gc.collect()
                
                        first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                        la_herd = first_post_box.find_elements_by_class_name('item-details')
                        first_post = la_herd[landage].find_element_by_tag_name('a')
                        first_post.click()
                        time.sleep(2.5)
                        driver.refresh()
                break
            except:
                print('error at click post section')
                try:
                    driver.switch_to.alert.dismiss()
                except:
                    driver.refresh()
                    tata += 1
                continue

        time.sleep(5)
        del first_post_box, la_herd, first_post
        gc.collect()
        
        if tata >= 5:
            driver.quit()
            time.sleep(200)
            continue
        else: 
            tata = 0 
            
        while completed < todays_post_target and tata <=5: 
            try: #read post and send reply
                try:
                    driver.switch_to.alert.dismiss()
                except:
                    pass
                
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'topic-content')))
                try:
                    username = driver.find_element_by_class_name('plan2-recommended')
                    username = username.text
                except:
                    username = driver.find_element_by_class_name('float-left')
                    username = username.text[0:-10]
                
                start_time = time.time()
                end_time = start_time + (sec_intervals/2)                   
                while time.time() <= end_time: #this section find the post needed and summarize it scroll down to the comments section and post the summary, scroll back up and hover over some ads
                    try:
                        passiv = driver.find_element_by_class_name('topic-content') #find the post and needed and summarize it
                        try:
                            logbut = passiv.find_elements_by_tag_name('p')
                            first_post_box = [note.text for note in logbut]
                            la_herd = ''.join(first_post_box)
                        except:
                            try:
                                logbut = passiv.find_element_by_tag_name('p')
                                noci = logbut.find_elements_by_tag_name('span')
                                first_post_box = [note.text for note in noci]
                                la_herd = ''.join(first_post_box)
                            except:
                                la_herd = ' '       
                        try:
                            summary_comment = post_summarizer(la_herd)
                        except:
                            summary_comment = username
                        
                        try:
                            username = driver.find_element_by_id('editor') #scroll down to the comments section and post the summary
                        except:
                            break
                        ActionChains(driver).move_to_element(username).perform()
                        passiv = username.find_element_by_tag_name('iframe')
                        driver.switch_to.frame(passiv)
                        logbut = driver.find_element_by_tag_name('p')
                        ActionChains(driver).move_to_element(logbut).perform()
                        logbut.click()
                        driver.execute_script("arguments[0].innerText = arguments[1] ", logbut, summary_comment)
                        driver.switch_to.default_content()
                        first_post_box = driver.find_element_by_id('ReplyButton')
                        ActionChains(driver).move_to_element(first_post_box).perform()
                        first_post_box.click()
                        if end_time > time.time():
                            time.sleep(end_time-time.time())
                        else: pass
                    except:
                        print('error at the section to read and post summary only')
                        driver.refresh()
                        time.sleep(2)
                        continue
            except:
                print('error at read and summarize section')
                driver.refresh()
                time.sleep(2.5)
                continue
            
            del start_time, end_time, username, passiv, logbut, la_herd, first_post_box, summary_comment
            gc.collect()
            
            landage += 1
            completed += 1
            driver.execute_script("window.history.go(-2)")
            
            while tata < 5:  #go to the next post
                try:
                    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blog')))
                    username = driver.find_element_by_class_name('blog') #find all elements that represent an article
                    passiv = username.find_elements_by_class_name('item-details')
                    
                    if landage >= len(passiv): #if the landage variable is greater than the number of articles present go to the next page on the pagination
                        landage = 0 #set the landage variable to 0
                        serum = True
                        pager += 1
                        logbut = username.find_elements_by_tag_name('a')
                        first_post_box = logbut[-1]
                        ActionChains(driver).move_to_element(first_post_box).perform()
                        first_post_box.click()#click the next button
                        
                        pass
                        la_herd = driver.find_element_by_class_name('blog-list-details') #find all elements that represent an article
                        first_post = la_herd.find_elements_by_class_name('item-details')
                        noci = first_post[landage].find_element_by_tag_name('a') #use landage variable to select one page
                        ActionChains(driver).move_to_element(noci).perform()
                        noci.click() #open the selected page
                        driver.implicitly_wait(sec_intervals/4)
                        driver.refresh()
                
                        del logbut, first_post_box, la_herd, first_post, noci
                        gc.collect()
                    else:
                        noci = passiv[landage].find_element_by_tag_name('a') #use landage variable to select one page
                        ActionChains(driver).move_to_element(noci).perform()
                        noci.click() #open the selected page
                        driver.implicitly_wait(sec_intervals/4)
                        del noci
                        gc.collect()
                        
                    if completed <=5:
                        print('No of posts:', completed)
                    elif completed % 10 == 0:
                        print('No of posts:', completed)
                    else: pass
                    break
                except:
                    print('error at go to next post section')
                    driver.refresh()
                    try:
                        driver.switch_to.alert.dismiss()
                    except:
                        driver.refresh()
                        tata += 1
                    continue
                
            del username, passiv
            gc.collect()
            
            if tata >= 5:
                tata += 2
            else: pass
        
            if time.localtime()[3] > 22 or completed == todays_post_target:
                post_var += 1
                completed = 0
                landage = 0
                driver.quit()
                print('about to sleep')
                break
            else: continue
        
        if tata > 5:
            driver.quit()
            time.sleep(200)
            continue
        else: pass
    
    except:
        print('error at connection section')
        serum = True
        driver.quit()
        continue
    
    time.sleep(35000)
    continue
        


