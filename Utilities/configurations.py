import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read("D:/Backendautomationpractice/restful-booker/Utilities/properties.ini")
    return config
