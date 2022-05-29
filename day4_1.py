from selenium import webdriver

my_driver = webdriver.Chrome()
# executable_path="c:/Users/tkronfeld/Downloads/"

# Test for tip calculation
def calculate_tip(my_driver):
    my_driver.get("c:/Users/tkronfeld/Desktop/DevOps-Course/Session4-8-5-2022/tip_calc/index.html") # open dafdefan
    my_driver.find_element_by_id("billamt").send_keys("100")
    my_driver.find_element_by_id("serviceQual").send_keys("10")
    # my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"/option[3]").click()
    my_driver.find_element_by_id("peopleamt").send_keys("1")
    my_driver.find_element_by_id("musicQual").send_keys("5")
    my_driver.find_element_by_id("calculate").click()
    return my_driver.find_element_by_id("tip").text

# Test result itself
expected = "105.00"
actual = calculate_tip(my_driver)
assert expected == actual    # if <> through AssertionError

# if expected == actual:
 #   print("all good")
# else:
 #   print("you broke the test")




