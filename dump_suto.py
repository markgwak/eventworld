import undetected_chromedriver as uc
import time

driver = uc.Chrome(headless=False)
driver.get("https://www.suto.co.kr/cpevent/622753")
time.sleep(5)

with open("suto_detail_dump.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("덤프 저장 완료!")
driver.quit()