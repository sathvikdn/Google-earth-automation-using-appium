# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
#Test count
passcount = 0
totaltest = 0

#Setting Up Desired Capabilities of Appium for Automation
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "11"
caps["deviceName"] = "Pixel 4a"
caps["automationName"] = "Appium"
caps["appPackage"] = "com.google.earth"
caps["appActivity"] = "com.google.android.apps.earth.EarthActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)

#Test 1 (check if right package  is selected )

totaltest += 1
pakkage =str(driver.current_package);
if(( pakkage == 'com.google.earth' ) ):
    passcount = passcount + 1
    print("\n test 1 : checking if correct pakkage is oppened  \n test has passed \n")




#Test 2 (check if right activity is selected )

totaltest += 1
activity = str(driver.current_activity);
if( activity == 'com.google.android.apps.earth.EarthActivity' ) :
    passcount = passcount + 1
    print("\n test 2 : checking if correct activity is oppened  \n test has passed \n")




#Test 3 (selecting an account )

totaltest += 1
el1 = driver.find_element_by_id("com.google.earth:id/og_apd_ring_view")
el1.click()
sleep(.5)
el2 = driver.find_element_by_accessibility_id("Use Sathvik D N sathvik.dn@gmail.com")
el2.click()
sleep(.5)


#checking if the profile is selected 
el3 = driver.find_element_by_id("com.google.earth:id/og_apd_ring_view")
el3.click()
el = driver.find_element_by_id('com.google.earth:id/account_display_name')
if (el.text == "Sathvik D N"):
    passcount = passcount + 1
    print("\n test 3  : selecting an account \n test has passed \n")
el4 = driver.find_element_by_accessibility_id("Close")
el4.click()




#Test 4 (Testing I'm feeling lucky)

totaltest += 1
sleep(.5)
el5 = driver.find_element_by_accessibility_id("I'm Feeling Lucky")
el5.click()
TouchAction(driver)   .press(x=588, y=2074)   .move_to(x=571, y=1556)   .release()   .perform()
el7 = driver.find_element_by_id("com.google.earth:id/knowledge_card_title")
TouchAction(driver).tap(x=73, y=225).perform()
if (el7.text != "Kumano"):
    passcount = passcount + 1
    print("\n test 4  : Testing I'm feeling lucky \n test has passed \n")
    
    


#Test 5 ( Testing search )

totaltest += 1
el8 = driver.find_element_by_accessibility_id("Open navigation drawer")
el8.click()
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.CheckedTextView")
el9.click()
el10 = driver.find_element_by_id("com.google.earth:id/search_text_view")
el10.set_text("Mangalore")
driver.execute_script('mobile: performEditorAction', {'action': 'search'})
sleep(6)
el11 = driver.find_element_by_id("com.google.earth:id/knowledge_card_title")
if (el11.text == "Mangalore"):
    passcount = passcount + 1
    print("\n test 5  : Testing search \n test has passed \n")
sleep(3) 

   



#Test 6 ( Testing for  Invalid element id ))

totaltest += 1
el8 = driver.find_element_by_accessibility_id("Open navigation drawer")
el8.click()
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.CheckedTextView")
el9.click()
el10 = driver.find_element_by_id("com.google.earth:id/search_text_view")
el10.set_text("Bangalore")
driver.execute_script('mobile: performEditorAction', {'action': 'search'})
sleep(6)
try:
  el11 = driver.find_element_by_id("com.doogle.earth:id/knowledge_card_title")  #wrong id 
  if (el11.text == "Bengaluru"):
      passcount = passcount + 1
      print("\n test 6  : Testing search \n test has passed \n")
      sleep(3) 
except:
  print("\n test 6  : Testing search \n test has Failed \n")





print("\n total number of cases          :  "+  str(totaltest))
print("\n total number of cases passed   :  "+ str(passcount))
print("\n total number of cases failed   :  "+ str(totaltest - passcount ))


driver.quit()