from selenium import webdriver
import random
from selenium.webdriver.firefox.options import Options
from pandas import *

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920x1080")

driver = webdriver.Firefox(options=firefox_options)

# driver = webdriver.Firefox()


def to_normal_text(selenium_object):
    return str(selenium_object.text)


option_labels = list('abcdefghijklmnopqrstuvwxyz')
form_data = {}


# for i in options:
#     print(i.text)
# for i in questions:
#     print(i.text)
def first_time_form_init(form_link):
    driver = webdriver.Firefox()
    driver.get(form_link)
    items = driver.find_elements_by_class_name('freebirdFormviewerViewItemsItemItem')
    count = 1
    for i in items:
        question = i.find_element_by_class_name('freebirdFormviewerViewItemsItemItemTitleContainer')
        form_data[count] = {}
        option_box = i.find_element_by_class_name('freebirdFormviewerViewItemsRadioChoicesContainer')
        options = option_box.find_elements_by_class_name('freebirdFormviewerViewItemsRadioOptionContainer')
        for i in range(len(options)):
            form_data[count][option_labels[i]] = options[i]
        count+=1

def starting_the_form(form_link):
    driver.get(form_link)
    return driver

def filling_up_form(driver, form_data):
    for i in form_data:
        form_data[i]['a'].click()
        submit = driver.find_element_by_class_name('freebirdFormviewerViewNavigationButtons')
        submit.click()
        
    

def generating_responses_for_questions(no_of_responses):
    xls = ExcelFile('Book2.xlsx')
    df = xls.parse(xls.sheet_names[0])
    option_percentages = df.to_dict()
    answers = {}
    for i in range(len(option_percentages['A'])):
        answers[i] = []
        a = [0]*(no_of_responses*int(option_percentages['A'][i])//100)
        b = [1]*(no_of_responses*int(option_percentages['B'][i])//100)
        c = [2]*(no_of_responses - (no_of_responses*int(option_percentages['A'][i])//100) - (no_of_responses*int(option_percentages['B'][i])//100))
        answers[i].extend(a)
        answers[i].extend(b)
        answers[i].extend(c)
    
    return answers

def answering_n_times(form_link, no_of_responses, answers):
    original = int(no_of_responses)
    while no_of_responses!= 0:
        driver.get(form_link)
        items = driver.find_elements_by_class_name('freebirdFormviewerViewItemsItemItem')
        count = 0
        for i in items:
            option_box = i.find_element_by_class_name('freebirdFormviewerViewItemsRadioChoicesContainer')
            options = option_box.find_elements_by_class_name('freebirdFormviewerViewItemsRadioOptionContainer')
            options[answers[count][0]].click()
            del(answers[count][0])
            count+=1
        submit = driver.find_element_by_class_name('freebirdFormviewerViewNavigationButtons')
        submit.click()
        no_of_responses-=1
        print("Submitted {} successfully".format(original-no_of_responses))
        # driver.implicit_wait(3)
        # driver.find_element_by_class_name('freebirdFormviewerViewResponseLinksContainer').click()
    
    # submit = driver.find_element_by_class_name('freebirdFormviewerViewNavigationButtons')
    # submit.click()
    # driver.quit()

# count = 50
# while count != 0: 
#     first_time_form_init()
#     count-=1  
# count = 1
# first_time_form_init('https://docs.google.com/forms/d/e/1FAIpQLSfDjdSnpPywLBpZi6NasdW6t5XE7cMMnRilyo6nZQDTWLLkQQ/viewform')
# updated_driver = starting_the_form('https://docs.google.com/forms/d/e/1FAIpQLSfDjdSnpPywLBpZi6NasdW6t5XE7cMMnRilyo6nZQDTWLLkQQ/viewform')
# while count != 0:
#     filling_up_form(updated_driver, form_data)
#     count-=1

# answers = generating_responses_for_questions(500)
# answering_n_times(
#     'https://docs.google.com/forms/d/e/1FAIpQLSfDjdSnpPywLBpZi6NasdW6t5XE7cMMnRilyo6nZQDTWLLkQQ/viewform',
#     500,
#     answers
# )


def random_answering_n_times(form_link, no_of_responses):
    original = int(no_of_responses)
    while no_of_responses!= 0:
        driver.get(form_link)
        items = driver.find_elements_by_class_name('freebirdFormviewerViewItemsItemItem')
        count = 0
        for i in items:
            option_box = i.find_element_by_class_name('freebirdFormviewerViewItemsRadioChoicesContainer')
            options = option_box.find_elements_by_class_name('freebirdFormviewerViewItemsRadioOptionContainer')
            choice = random.randint(0, len(options)-1)
            options[choice].click()
        submit = driver.find_element_by_class_name('freebirdFormviewerViewNavigationButtons')
        submit.click()
        no_of_responses-=1
        print("Submitted {} successfully".format(original-no_of_responses))

random_answering_n_times(
    'https://forms.gle/uk2GiApQmwv76eaG6',
    50
)