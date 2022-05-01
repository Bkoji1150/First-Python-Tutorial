import os 
from pprint import pprint


def get_all_python():
    list_of_python = []
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file == "mysql":
                list_of_python.append(os.path.join(r, each_file))
    return list_of_python     

def display_mysql(home_config_files):
    for each_key in home_config_files.keys():
        print(f"Mysql home is:, {home_config_files[each_key][0]}")
        print(f"Mysql config file is: {home_config_files[each_key][1]}")
    return None

def main():
    print("List of python programs")
    count = 1
    home_config_files = {}
    python_path = get_all_python()
    for each_config_file in python_path:
        mysql_home= os.path.dirname(os.path.dirname(each_config_file))
        mysql_config_file = each_config_file
        home_config_files['mysql'+str(count)]= [mysql_home, mysql_config_file]
        count +=1
    display_mysql(home_config_files)
    return None

if __name__ == '__main__':
    main()