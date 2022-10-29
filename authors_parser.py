from selenium import webdriver
from selenium.webdriver.common.by import By


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_title_author(driver):
    # title = driver.find_elements(By.ID, "project-title") # простой и не особо надежный вариант вытаскивания
    title = driver.find_element(By.XPATH, "//div[@id='project-info']/h1[@id='project-title']").text
    author = driver.find_element(By.XPATH, "//div[@id='project-head']/p[@class='subsubtitle']/b").text
    return title, author


def get_authors_dict():
    page = 5
    authors_dict = {}
    while page < 15:
        try:
            url = 'https://itr-projects.tpu.ru/?project=' + str(page)
            driver = get_html(url)
            title, author = get_title_author(driver)
            authors_dict[title] = author
            page += 1
        except:
            page += 1
            continue
    return authors_dict


def main():
    print(get_authors_dict())


if __name__ == '__main__':
    main()
