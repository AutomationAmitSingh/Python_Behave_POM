from selenium import webdriver
# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()
import shutil
#import zipfile
import os

import time
import logging
#from features.lib.pagefactory import on


def before_all(context):
    print("<-- Before all method execution started -->")
    print("<-- Before all method execution ended -->")


def before_feature(context, feature):
    print("<-- Before feature method execution started -->\n")
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('Concert Web Client Logs')
    hdlr = logging.FileHandler('./CWC.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.INFO)
    print("<-- Before feature method execution ended -->\n")
# Scenario level objects are popped off context when scenario exits


def before_scenario(context, scenario):
    print("<-- Before scenario method execution started -->\n")
    print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    # For some reason, python doesn't have switch case -
    # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    print("<-- Before scenario method execution ended -->\n")


def after_scenario(context, scenario):
    print("<-- After scenario method execution started -->")
    print(scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

    context.browser.quit()
    print("<-- After scenario method execution ended -->")


def after_feature(context, feature):
            print("\n<-- After feature method execution started -->")
            print("\n<-- After feature method execution ended -->")


def after_all(context):
    print("\n<-- After all method execution started -->")
    print(os.getcwd())
    parent_path = os.path.dirname(os.getcwd())
    os.chdir(parent_path)
    print(os.getcwd())
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(time.strftime("%d_%m_%Y_%H_%M_%S"), 'zip', "failed_scenarios_screenshots")
    print("\n<-- After all method execution ended -->")

