import configparser

configParser = configparser.RawConfigParser()

def get_git_config(key):
    configFilePath = r'src\git_credentials.cfg'
    configParser.read(configFilePath)
    return configParser.get('git-config', key)

