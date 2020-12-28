import Constants
from time import sleep


def login(driver, user, password):
    driver.get('https://myflye.flyefit.ie/login')

    user_login = driver.find_element_by_xpath("//*[@id='email_address']")
    user_login.send_keys(user)

    pass_login = driver.find_element_by_xpath("//*[@id='password']")
    pass_login.send_keys(password)

    login_button = driver.find_element_by_xpath("/html/body/div[1]/form/div/div/div[2]/div/div[3]/div[2]/input")
    login_button.click()

    sleep(2)


def navigation(driver):
    book_workout_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/b/div/div/div/a")
    book_workout_button.click()

    next_day_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[3]/div/div[3]/a/img")
    next_day_button.click()

    get_time_of_day_button = driver.find_element_by_xpath("//p[@data-course-time='19:00 - 20:15']")
    get_time_of_day_button.click()

    sleep(1)


def bookWorkout(driver):
    confirm_booking_button = driver.find_element_by_xpath("//*[@id='book_class']")
    confirm_booking_button.click()

    sleep(1)

    close_popup = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[1]/button/span/img")
    close_popup.click()

    sleep(1)


def logout(driver):
    logout_button = driver.find_element_by_xpath("")
    logout_button.click()

    sleep(1)


def bookGym(driver):
    for user, password in zip(Constants.USERS, Constants.PASS):
        try:
            login(driver, user, password)
            navigation(driver)
            bookWorkout(driver)
            #logout(driver)
        except:
            print("An error has occurred")
        else:
            print("User: " + user + " has been succesfully booked!")
