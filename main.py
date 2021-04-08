from selenium import webdriver
from selenium.webdriver.support.ui import Select

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#로그인창 접속
LOTTO_URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(LOTTO_URL)

#동행복권 아이디, 비번 입력
yourID = ''
yourPW = ''
elem_login = driver.find_element_by_id('userId')
elem_login.send_keys(yourID)

elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys(yourPW)

#로그인 버튼 클릭
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element_by_xpath(LOGIN_XPATH).click()

#로또 구매창 이동
driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')

#자동번호 발급
driver.switch_to.frame('ifrm_tab')
driver.find_element_by_xpath('//*[@id="num2"]').click()

#로또 구매 개수 선택
select = Select(driver.find_element_by_xpath('//*[@id="amoundApply"]'))
select.select_by_value('5')

#구매 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnSelectNum"]').click()

#구매하기
driver.find_element_by_xpath('//*[@id="btnBuy"]').click()

#확인 버튼
alert = driver.switch_to.alert
alert.accept()

#종료
driver.close()
