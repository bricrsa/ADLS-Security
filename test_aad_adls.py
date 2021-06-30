from aad_adls import *
from file_credentials import *

#################################
# set up vars for storage account, file sys
# dirs and creds
#################################

storage_account_name = "hookdatalake"
file_system_name = "raw"
directory_name = "source-a/object-1"
load_creds('cred99')
#load_master_creds(storage_account_name)
initialize_storage_account_ad_sp(storage_account_name)
#initialize_storage_account_ad(storage_account_name)
#create_directory_with_child_files(file_system_name,directory_name)
#list_directory_contents(file_system_name, directory_name)
list_file_systems_and_paths()
#access_control_sample(file_system_name, directory_name)





#load_master_creds(storage_account_name)
#master_key_operations() #needs master creds


# set up the service client with the credentials from the environment variables

#print ('STORAGE_ACCOUNT_NAME' , os.getenv('STORAGE_ACCOUNT_NAME'))
#initialize_storage_account_ad_sp(storage_account_name)
#list_file_systems()
#list_directory_contents(file_system_name)




