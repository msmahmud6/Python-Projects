import os
import smtplib
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()


# To Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=en-US')
chrome_options.add_experimental_option("detach",True)

desired_amount = int(input("Price at which you should be notified :\n"))

driver = webdriver.Chrome(options=chrome_options)
experiment_link = "https://www.daraz.com.bd/products/tp-link-deco-e4-ac1200-router-whole-home-mesh-wi-fi-system-1-pack-i156550140-s1086146208.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A156550140%253Bsrc%253ALazadaMainSrp%253Brn%253A337a8b33217b6ee5cc1d236e2e5cca65%253Bregion%253Abd%253Bsku%253A156550140_BD%253Bprice%253A2825%253Bclient%253Adesktop%253Bsupplier_id%253A5885%253Bbiz_source%253Ahp_categories%253Bslot%253A10%253Butlog_bucket_id%253A470687%253Basc_category_id%253A128%253Bitem_id%253A156550140%253Bsku_id%253A1086146208%253Bshop_id%253A5641%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=2825&priceCompare=skuId%3A1086146208%3Bsource%3Alazada-search-voucher%3Bsn%3A337a8b33217b6ee5cc1d236e2e5cca65%3BoriginPrice%3A282500%3BdisplayPrice%3A282500%3BsinglePromotionId%3A50000028132010%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1738528851346&ratingscore=4.801418439716312&request_id=337a8b33217b6ee5cc1d236e2e5cca65&review=706&sale=3347&search=1&source=search&spm=a2a0e.searchlistcategory.list.10&stock=1"
experiment_link2 = "https://www.daraz.com.bd/products/kitkat-2-119gm-35-i374907429-s1876292084.html?scm=1007.51610.379274.0&pvid=cc0e77e3-1a14-417e-bb30-8dd25b04bbfa&search=flashsale&spm=a2a0e.tm80335411.FlashSale.d_374907429"
experiment_link3 = "https://www.daraz.com.bd/products/rgb-35-i339755176-s1663893189.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A339755176%253Bsrc%253ALazadaMainSrp%253Brn%253A44b564d1110e5ac748da345b19391883%253Bregion%253Abd%253Bsku%253A339755176_BD%253Bprice%253A791%253Bclient%253Adesktop%253Bsupplier_id%253A700508877343%253Bbiz_source%253Ah5_external%253Bslot%253A15%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7847%253Bitem_id%253A339755176%253Bsku_id%253A1663893189%253Bshop_id%253A198124%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=791&priceCompare=skuId%3A1663893189%3Bsource%3Alazada-search-voucher%3Bsn%3A44b564d1110e5ac748da345b19391883%3BoriginPrice%3A79100%3BdisplayPrice%3A79100%3BsinglePromotionId%3A50000028602116%3BsingleToolCode%3AflashSale%3BvoucherPricePlugin%3A0%3Btimestamp%3A1738532724314&ratingscore=5.0&request_id=44b564d1110e5ac748da345b19391883&review=3&sale=142&search=1&source=search&spm=a2a0e.searchlistcategory.list.15&stock=1"
# user_link = input("Enter Any Product Link from Daraz :")
driver.get(experiment_link3)

#Product Name
product_name = driver.find_element(By.CLASS_NAME, value="pdp-mod-product-badge-title").text
print(product_name)
#Price
product_price = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div[3]/div[2]/div/div[1]/div[10]/div/div/span')
product_price_text = product_price.text
price = product_price_text.replace('\u09f3','0') #Exceptinally Handling this '৳' unicode problem

driver.quit()
mod_price = price[2:]
if ',' in mod_price:
    split_price = mod_price.split(',',1)
    total_price = int(split_price[0]+split_price[1])
else:
    total_price = int(mod_price)

print(total_price)

msg_body = f"{product_name} is Now only {total_price} Tk. Hurry up before getting out of stock!"

if total_price<=desired_amount:
    print(msg_body)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(os.environ["my_email"],os.environ["password"])
    s.sendmail(from_addr=os.environ["my_email"],to_addrs=['msmahmud64@gmail.com','abdullatif420mahbub@gmail.com'],msg=f"Subject:Price Dropped on {product_name[:45]}...\n\n{msg_body}")
    s.quit()
