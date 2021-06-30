from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
from azure.storage.filedatalake import (
    DataLakeServiceClient,
)
# from azure.storage.filedatalake import DataLakeServiceClient

import os
import random
import uuid


def set_env_var(env_var, env_var_value):
    os.environ[env_var] = env_var_value
    print(f'Check {env_var} is {os.environ.get(env_var)}')


def authenticate_device_code():
    """
    Authenticate the end-user using device auth.
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = 'placeholder-tenant-id'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.azure.com/'
    client_id = 'placeholder-app-id'

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    code = context.acquire_user_code(resource_uri, client_id)
    print(code['message'])
    mgmt_token = context.acquire_token_with_device_code(resource_uri, code, client_id)
    credentials = AADTokenCredentials(mgmt_token, client_id)
    # print (mgmt_token)
    return credentials


def initialize_storage_account_ad(storage_account_name):

    set_env_var('AZURE_USERNAME', 'placeholder-email-address')
    # authenticate_device_code()
    try:  
        global service_client
        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=credential)
   
    except Exception as e:
        print(e)


def initialize_storage_account_ad_sp(storage_account_name):

    active_directory_tenant_id = os.getenv("AZURE_TENANT_ID")
    
    active_directory_application_id = os.getenv("AZURE_CLIENT_ID") # ACTIVE_DIRECTORY_APPLICATION_ID
    active_directory_application_secret = os.getenv("AZURE_CLIENT_SECRET")

    try:  
        global service_client
        token_credential = ClientSecretCredential(
            active_directory_tenant_id,
            active_directory_application_id,
            active_directory_application_secret
        )
        
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=token_credential)
        
    except Exception as e:
        print(e)

def list_directory_contents_root(file_system_name):

    try:
        file_system_client = service_client.get_file_system_client(file_system=file_system_name)

        folder_name = ""
        paths = file_system_client.get_paths(path=folder_name)

        for path in paths:
            print(path.name + ' ' + str(path.size) + '\n')

    except Exception as e:
        print(e)

def list_paths_in_file_system(file_system_name):

    # Instantiate a FileSystemClient
    file_system_client = service_client.get_file_system_client(file_system_name)

    # [START get_paths_in_file_system]
    path_list = file_system_client.get_paths()
    for path in path_list:
        print(path.name + '\n')
    # [END get_paths_in_file_system]

def list_paths_in_file_system_i(file_system_name):

    # Instantiate a FileSystemClient
    file_system_client = service_client.get_file_system_client(file_system_name)

    # [START get_paths_in_file_system]
    path_list = file_system_client.get_paths()
    for path in path_list:
        print(path.name + '\n')
    # [END get_paths_in_file_system]

def list_file_systems():
    try:
        # Instantiate a FileSystemClient
        file_systems = service_client.list_file_systems()
        for file_system in file_systems:
            print(file_system.name)
            
    except Exception as e: 
        print(e)

def list_file_systems_and_paths():
    try:
        # Instantiate a FileSystemClient
        file_systems = service_client.list_file_systems()
        for file_system in file_systems:
            print(file_system.name)
            list_paths_in_file_system_i(file_system.name)

    except Exception as e: 
        print(e)


def list_directory_contents(file_system_name, directory_name):
    try:
        
        file_system_client = service_client.get_file_system_client(file_system=file_system_name)

        paths = file_system_client.get_paths(path= directory_name)

        for path in paths:
            print(path.name + '\n')

    except Exception as e:
     print(e)

def create_directory_test_file(file_system_name):

    try:
        file_system_client = service_client.get_file_system_client(file_system=file_system_name)

        folder_name = ""
        paths = file_system_client.get_paths(path=folder_name)

        for path in paths:
            print(path.name + ' ' + str(path.size) + '\n')

    except Exception as e:
        print(e)

def access_control_sample(file_system_name, directory_name):


    print("Using file system '{}'.".format(file_system_name))
    filesystem_client = service_client.get_file_system_client(file_system_name)  

    print("Creating a directory named '{}'.".format(directory_name))
    directory_client = filesystem_client.create_directory(directory_name)
  
    # get and display the permissions of the parent directory
    acl_props = directory_client.get_access_control()
    print(acl_props)
    print(acl_props['owner'])
    print("Permissions of directory '{}' are {}.".format(directory_name, acl_props['permissions']))

    # set the permissions of the parent directory
    #new_dir_permissions = 'rwx------'
    # directory_client.set_access_control(owner='36ff457d-ba7c-4130-960c-32aa36809dcb') #         .set_access_control(permissions=new_dir_permissions)
    directory_client.set_access_control(owner='bb1de57a-a70b-4c56-84bb-4658f6a3cc2c') #         .set_access_control(permissions=new_dir_permissions)
    acl_props = directory_client.get_access_control()
    print(acl_props)
    print(acl_props['owner'])
    '''
    # get and display the permissions of the parent directory again
    acl_props = directory_client.get_access_control()
    print("New permissions of directory '{}' are {}.".format(dir_name, acl_props['permissions']))

    # iterate through every file and set their permissions to match the directory
    for file in filesystem_client.get_paths(dir_name):
        file_client = filesystem_client.get_file_client(file.name)

        # get the access control properties of the file
        acl_props = file_client.get_access_control()

        if acl_props['permissions'] != new_dir_permissions:
            file_client.set_access_control(permissions=new_dir_permissions)
            print("Set the permissions of file '{}' to {}.".format(file.name, new_dir_permissions))
        else:
            print("Permission for file '{}' already matches the parent.".format(file.name))
    '''


def create_directory_with_child_files(file_system_name, directory_name):


    print("Using file system '{}'.".format(file_system_name))
    filesystem_client = service_client.get_file_system_client(file_system_name)  

    print("Creating a directory named '{}'.".format(directory_name))
    directory_client = filesystem_client.create_directory(directory_name)

    create_child_files(directory_client,5)


def master_key_operations_create_fs():
    account_name = os.getenv('STORAGE_ACCOUNT_NAME')
    account_key = os.getenv('STORAGE_ACCOUNT_KEY')
    print(account_name)
    print(account_key)
    # set up the service client with the credentials from the environment variables
    service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https",
        account_name
    ), credential=account_key)

    # generate a random name for testing purpose
    fs_name = "testfs{}".format(random.randint(1, 1000))
    print("Generating a test filesystem named '{}'.".format(fs_name))

    # create the filesystem
    filesystem_client = service_client.create_file_system(file_system=fs_name)

    # invoke the sample code
    try:
        create_directory(filesystem_client)
        #access_control_sample(filesystem_client)
    finally:
        # clean up the demo filesystem
        # filesystem_client.delete_file_system()
        print("all_done")

def create_files():
    
    # generate a random name for testing purpose
    fs_name = "testfs{}".format(random.randint(1, 1000))
    print("Generating a test filesystem named '{}'.".format(fs_name))

    # create the filesystem
    filesystem_client = service_client.create_file_system(file_system=fs_name)

    # invoke the sample code
    try:
        create_directory(filesystem_client)
        #access_control_sample(filesystem_client)
    finally:
        # clean up the demo filesystem
        #filesystem_client.delete_file_system()
        print("all_done")


def create_child_files(directory_client, num_child_files):
    import concurrent.futures
    import itertools
    # Use a thread pool because it is too slow otherwise
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        def create_file():
            # generate a random name
            file_name = str(uuid.uuid4()).replace('-', '')
            directory_client.get_file_client(file_name).create_file()

        futures = {executor.submit(create_file) for _ in itertools.repeat(None, num_child_files)}
        concurrent.futures.wait(futures)
        print("Created {} files under the directory '{}'.".format(num_child_files, directory_client.path_name))
        