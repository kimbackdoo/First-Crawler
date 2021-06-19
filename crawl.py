import time
import web_driver_util as wdu
import file_dir as fd

from selenium.webdriver.common.keys import Keys

class Crawl:
    def __init__(self):
        webdriver = wdu.WebDriverUtil()
        self.driver = webdriver.driver

        self.filedir = fd.FileDir()

    def start(self, product_name_list):
        self.login()
        self.search_product(product_name_list)
        self.crawl_quit()

    def login(self):
        self.driver.find_element_by_name("main_id").send_keys("아이디") # 아이디
        self.driver.find_element_by_name("main_pwd").send_keys("비밀번호") # 비밀번호
        self.driver.find_element_by_class_name("submit_btn").click() # 로그인
        time.sleep(1.5) # 페이지 로딩될 때까지 1.5초 대기
        self.driver.get("https://shop.styleshare.kr/selleradmin/goods/catalog")

    def search_product(self, product_name_list):
        for product in product_name_list:
            print("=======================================================")
            print(product)

            hyphen_find = product.find("-") # 폴더 이름에 하이픈(-) 위치를 찾음
            supplier_name = product[:hyphen_find] # 폴더 이름에서 공급사 이름 슬라이싱
            product_name = product[hyphen_find+1:] # 폴더 이름에서 상품명 슬라이싱

            element = self.driver.find_element_by_name("keyword")
            element.clear()
            element.send_keys(product_name) # 검색창에 제품명 쓰기
            self.driver.find_element_by_xpath("//*[@class='sfk-td-btn']/button").send_keys(Keys.ENTER) # 클릭 에러 발생을 방지하기 위해 엔터키를 통해 제품 검색
            if self.driver.find_element_by_xpath("//*[@class='list-row']").text == "등록된 상품이 없습니다.":
                continue
            else:
                if self.filedir.mkdir(supplier_name, product_name): # 폴더가 없으면 폴더 생성 후 크롤링, 폴더가 있으면 continue
                    shop_click = self.driver.find_element_by_xpath("//*[@id='goodsForm']/table/tbody/tr[1]/td[5]/a") # 상품에 대한 a 태그 찾기
                    self.driver.execute_script("arguments[0].click();", shop_click) # 클릭 에러 발생을 방지하기 위해 스크립트로 클릭 이벤트 실행

                    tabs = self.driver.window_handles # 현재 열려있는 탭 리스트 저장
                    self.driver.switch_to_window(tabs[-1]) # 최근에 열린 탭을 활성화

                    text_list = self.driver.find_elements_by_xpath("//*[@class='LineCollapse__StyledText-isCgez eIHWnQ']") # 본문 텍스트 리스트
                    text = ""
                    for t in text_list: # 본문 텍스트 리스트의 텍스트들을 text 변수에 저장
                        text += t.text
                        text += "\n\n"
                    self.filedir.mktxt(product_name, text) # 텍스트를 파일로 저장

                    img_list = self.driver.find_element_by_xpath("//*[@class='Box-cYFAGx Collapsible__Panel-hlzKpm iuIKxE cdjJBn']").find_elements_by_tag_name("img") # 이미지 개수 구하기
                    for i in range(len(img_list)): # 이미지 개수만큼 for문을 돌면서 이미지 저장
                        self.filedir.img_download(img_list[i].get_attribute("src"), i+1)
                    self.driver.close()
                    self.driver.switch_to_window(tabs[0]) # 활성화 탭 스타일쉐어 어드민 페이지로 변환
                else:
                    continue
            print("=======================================================")

    def crawl_quit(self):
        self.driver.quit() # 셀레니움 종료