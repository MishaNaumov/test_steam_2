from selenium import webdriver


class WebDriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(WebDriver, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def get_driver(options):
        return webdriver.Chrome(options)
