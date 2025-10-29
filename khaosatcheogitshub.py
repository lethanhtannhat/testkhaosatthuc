from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import csv
from selenium.common.exceptions import TimeoutException
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
def fill(name,stt):
    xpaths = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div[1]/div/div[1]/input'.format(stt+1),
        #//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div[1]/div[2]/textarea'.format(stt+1)
        #//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea
    ]

# Biến để lưu phần tử tìm thấy
    element = None

    # Thử từng XPath
    for xpath in xpaths:
        try:
            # Chờ tối đa 10 giây để phần tử với xpath này xuất hiện
            element = WebDriverWait(driver, 0.2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            break
        except TimeoutException:
            continue
    element.send_keys(name) 

def filla(name):
    xpaths = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'
    ]

# Biến để lưu phần tử tìm thấy
    element = None

    # Thử từng XPath
    for xpath in xpaths:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            break  # Nếu tìm thấy phần tử, thoát vòng lặp
        except:
            continue
    

    if element is None:
        raise Exception("Không tìm thấy phần tử phù hợp với bất kỳ XPath nào.")
    element.send_keys(name)
def tn(ques1,stt,number_answers):
    vitri = 1
    my_string = []
    radio_buttons = []
    
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/div/span/div/div[{i}]/label/div/div[1]/div')

        radio_buttons.append(WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1]))
        ))
        
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == ques1 or str(vitri) == ques1:
                driver.execute_script("arguments[0].click();", radio)
        vitri += 1
def mntx(ques1,stt,number_answers):

    
    k=3
    vitri=1                
    radio2_select = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div[1]/div[1]'))) #lấy xpath ô chọn
    for radio2 in radio2_select:
        driver.execute_script("arguments[0].click();", radio2)
    time.sleep(1)
    my_string = []
    radio_buttons = []
    for i in range(1, number_answers+1):
        my_string.append(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[2]/div[{k}]')   
                        #/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt}]/div/div/div[2]/div/div[1]/div[1]/div[1]
        
        #câu trắc nghiệm 
        radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1])))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == ques1 or str(vitri) == ques1:
                driver.execute_script("arguments[0].click();", radio)
                return
        vitri=vitri+1
        k=k+1
def hk(*args, stt):

    compare_values = list(args)
    number_answers = len(compare_values)  # Số câu trả lời sẽ tự động bằng số lượng tham số
    vitri=1
    my_string = []
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/div[{i}]/label/div/div[1]')
                        #/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[1]
        #câu trắc nghiệm 
        radio_buttons = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1]))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons:
            for value in compare_values[i-1]:
                if radio.get_attribute("data-answer-value")[0] == value[0] or str(vitri) == value:
                    driver.execute_script("arguments[0].click();", radio)
                    break
def day(month, date, year,stt):

    #ngày tháng năm/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    month_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath tháng
    date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath ngày
    year_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath năm
    input_array = [month_input,date_input,year_input]
    for i in range(len(input_array)):
        input_array[i].clear()
        input_array[i].send_keys([month,date, year][i])
def gio(hour, minute,stt):
    hour_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))) #xpath giờ
    minute_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))) #xpath phút
    input_array = [hour_input,minute_input]
    for i in range(len(input_array)):
        input_array[i].clear()
        input_array[i].send_keys([hour, minute][i])
def pvtt(a,stt,number_answers):   
    my_string = []
    radio_buttons = []
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/span/div/label[{i}]/div[2]/div/div')
        
        
        #câu trắc nghiệm 
        radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1])))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == a:
                driver.execute_script("arguments[0].click();", radio)
def hk_grid(*args, stt, colums):
    compare_values = [list(arg) for arg in args]  # Chia thành các hàng (số câu hỏi)
    rows = len(compare_values)
    vitri=1
    k=2
    my_string = []
    radio_buttons = []
    for j in range(1, rows + 1):
        for i in range(1, colums +1):
            index = (j-1) * colums + (i-1)
            my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div/div[{k}]/span/div[{i+1}]/div/div')
            radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[index])))) #lấy xpath ô trắc nghiệm 1
            for radio in radio_buttons[index]:
                for value in compare_values[j-1]:
                    if radio.get_attribute("data-value") == value  or str(vitri) == value:
                        driver.execute_script("arguments[0].click();", radio)
                        break
            vitri=vitri+1                        
        vitri=1
        k=k+2
def hk_luoi(*args, stt, rows, colums):
    compare_values = [list(args[i:i + colums]) for i in range(0, len(args), colums)]  # Chia thành các hàng
    vitri = 1
    k = 2
    my_string = []
    radio_buttons = []
    
    
    vitri=1
    k = 2
    my_string = []
    for j in range(1, rows+1):
        radio_buttons = []
        for i in range(1, colums + 1):
            index = (j-1) * colums + (i-1)
            my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div/div[{k}]/label[{i}]/div/div')
            radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[index])))) 
            for radio in radio_buttons[i-1]:
                for value in compare_values[j-1]:
                    if radio.get_attribute("data-answer-value") == value  or str(vitri) == value:
                        driver.execute_script("arguments[0].click();", radio)
                        break
            vitri=vitri+1                        
        vitri=1
        k += 2

def fill_form(name,stt):
    fill(name,stt)

def tracnghiem(ques1, stt, number_answers):
    tn(ques1,stt,number_answers)

def menuthaxuong(ques1, stt, number_answers):
    mntx(ques1,stt,number_answers)

def hopkiem(*args, stt):
    hk(*args, stt=stt)

def date(month, date, year,stt):
    day(month, date, year,stt)

def hour(hour, minute,stt):
    gio(hour, minute,stt)
    
def phamvituyentinh(a,stt,number_answers):
    pvtt(a,stt,number_answers)
          
def luoitracnghiem(*args, stt, colums):
    hk_grid(*args, stt=stt, colums=colums)

def luoihopkiem(*args, stt, rows, colums):
    hk_luoi(*args, stt=stt, rows=rows, colums=colums)




try:
    # Lấy index từ tham số dòng lệnh (ví dụ: python script.py 5)
    if len(sys.argv) > 1:
        index = int(sys.argv[1])
    else:
        # Nếu không có tham số (trường hợp chạy tay), mặc định index = 0
        index = 0
    print(f"Bắt đầu điền form cho index: {index}")

except Exception as e:
    print(f"Lỗi đọc index từ tham số: {e}. Dùng index = 0.")
    index = 0



# Mở và đọc đúng dòng trong CSV
with open("test.csv", encoding="utf-8-sig") as file:
    reader = list(csv.reader(file))
    total_rows = len(reader)

    if total_rows == 0:
        print("File CSV rỗng!")
        driver.quit() # Thêm driver.quit() để đảm bảo đóng driver
        exit()

    # KHÔNG CẦN DÒNG RESET: if index >= total_rows: index = 0
    
    if index >= total_rows:
        print(f"Index {index} vượt quá số dòng {total_rows}. Hoàn thành chu kỳ.")
        driver.quit() # Đóng driver
        exit()

    row = reader[index]
time.sleep(1)

driver.get('')
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
driver.execute_script("arguments[0].click();", next_button)

time.sleep(0.6)
time.sleep(random.randint(60,180))
driver.quit()
