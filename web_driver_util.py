from selenium import webdriver

class WebDriverUtil:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking") # 팝업 무시
        options.add_argument("--disable-default-apps") # 기본앱 사용안함

        options.add_argument("headless") # Headless 모드 사용
        options.add_argument("--window-size=1920x1080") # Headless 모드에서 태그들을 정상적으로 인식하기 위해 window 사이즈 설정
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36") # Headless 모드인 것을 숨김
        options.add_argument("lang=ko_KR") # 한국어로 언어 설정

        options.add_argument("--disable-gpu") # GPU 사용 안함
        options.add_argument("--disable-infobars") # 알림막대 사용 안함
        options.add_argument("--disable-extensions") # 확장 도구 사용안함

        # 성능 향상을 위해 크롬 옵션 해제
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
                                                            'geolocation': 2, 'notifications': 2,
                                                            'auto_select_certificate': 2, 'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2, 'ppapi_broker': 2,
                                                            'automatic_downloads': 2, 'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2, 'durable_storage': 2}}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

        self.driver.implicitly_wait(10) # 페이지가 로드될 때까지 최대 10초 대기, 페이지가 로드되면 10초가 안지나도 대기 종료
        self.driver.get(url="https://shop.styleshare.kr/selleradmin/")