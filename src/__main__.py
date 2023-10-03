from crawler import login



driver = login.open_browser()

login.go_to_student_center(driver)

input("Press q to quit")

driver.quit()