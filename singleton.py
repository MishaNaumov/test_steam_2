from selenium import webdriver


class WebDriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = webdriver.Chrome(*args)
        return cls.__instance

    @classmethod
    def get_driver(cls):
        return cls.__instance

    @classmethod
    def quit(cls):
        cls.__instance.quit()
        cls.__instance = None
