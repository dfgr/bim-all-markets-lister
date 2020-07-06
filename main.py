from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
db = [] 
driver = webdriver.Chrome(ChromeDriverManager().install())
for y in range(82):
    if y != 0:
        driver.get("https://www.bim.com.tr/Categories/104/magazalar.aspx?CityKey="+str(y))
        time.sleep(1)
        driver.execute_script("""let optionCount = document.getElementById("GZoneOrtaAlanDegisken_BimFiltre_DrpCounty").length;let path = '//*[@id="GZoneOrtaAlanDegisken_BimFiltre_CustomUpdatePanel1"]/div[1]/p/span';let countE = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);countE.singleNodeValue.innerText = optionCount;let path1 = '//*[@id="form1"]/div[2]/div[2]/div/h2';box = document.getElementById("GZoneOrtaAlanDegisken_BimFiltre_DrpCity");let city = "";for(let i = 1; i != box.length; i++){if(box[i].getAttribute("selected") == "selected"){city = box[i].innerText}};let cityE = document.evaluate(path1, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);cityE.singleNodeValue.innerText = city;""")
        countRegion = driver.find_element_by_xpath('//*[@id="GZoneOrtaAlanDegisken_BimFiltre_CustomUpdatePanel1"]/div[1]/p/span').text
        city = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/h2').text
        db.append({"cityName":city,"licansePillate":y, "regions":[]})
        countRegion = int(countRegion) + 1 
        for x in range(int(countRegion)):
            if x != 0 and x != 1:
                region = driver.find_element_by_xpath('//*[@id="GZoneOrtaAlanDegisken_BimFiltre_DrpCounty"]/option['+str(x)+']')
                val = region.get_attribute("value")
                regText = region.text
                print(y)
                db[y-1]["regions"].append({"name":regText,"value":val,"markets":[]})
for z in db:
    for w in z["regions"]:
        no = w["value"]
        driver.get("https://www.bim.com.tr/Categories/104/magazalar.aspx?CountyKey="+str(no))
        time.sleep(1)
        marketNo = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/div[3]/div/div/div[1]/span[2]').text
        print(marketNo)
        for t in range(int(marketNo)+1):
            if t != 0 and t!= 1:
                nameMarket = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/div[3]/div/div/div['+str(t)+']/div/h3').text
                addressMarket = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/div[3]/div/div/div['+str(t)+']/div/p').text
                print(nameMarket)
                print(addressMarket)
                w["markets"].append({"name":nameMarket,"address":addressMarket})
            if marketNo == "1":
                nameMarket = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/h3').text
                addressMarket = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/p').text
                print(nameMarket)
                print(addressMarket)
                w["markets"].append({"name":nameMarket,"address":addressMarket})
            
print(db)
driver.close()