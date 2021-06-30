import os
import json


def set_env_var(env_var, env_var_value):
    os.environ[env_var] = env_var_value
    if env_var.upper().find('SECRET') < 0:
        print(f'Check {env_var} is {os.environ.get(env_var)}')


def load_creds(credname):

    filename = credname + '.id'
    # Open JSON file
    with open('creds/'+ filename, 'r') as openfile: 
        json_object = json.load(openfile)

    set_env_var('AZURE_TENANT_ID', json_object["tenant"])
    set_env_var('AZURE_CLIENT_ID', json_object["appId"])
    set_env_var('AZURE_CLIENT_SECRET', json_object["password"])


def load_master_creds(storage_account_name):
    filename = storage_account_name + '.id'
    # Open JSON file 
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile) 

    set_env_var('STORAGE_ACCOUNT_NAME', json_object["storage_acc_name"])
    set_env_var('STORAGE_ACCOUNT_KEY', json_object["key"])
