import argparse
import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser(prog="Looper",description="Program that loops commands for a given list", usage="looper.py -l .\list.txt -c 'New-Item $var -ItemType \"directory\"' -s powershell")
    parser.add_argument('-l', '--list', help="a list of items (seperated by linebreak) that should be looped", required=True)
    parser.add_argument('-c', '--command', action="append", help="command to be exeuted seperately for each item in list; Surrounded by single quotes ''; Items from list can used as parameters with $var")
    parser.add_argument('-f', '--scriptfile', help="loads a file containing the commands that sould be executed. Items from list can used in the script with $var")
    parser.add_argument('-s', '--shell', choices=['cmd','powershell'], help='specify the shell to use (cmd or powershell)', default="powershell", required=False)
    return parser.parse_args()

# open provided scriptfile
def open_scriptfile(file):
    with open(file, encoding='utf-8-sig') as scriptfile:
        scriptfile_commands = [line.strip() for line in scriptfile]
    return scriptfile_commands

# open provided list
def open_list(list):
    with open(list, encoding='utf-8-sig') as file:
        list_item = [line.strip() for line in file]
    return list_item

# replace list variable if needed from command
def replace_variable(command, list_item):
     command= command.replace(r"$var", list_item)
     return command

# execute command
def execute_command(replaced_command, shell):
    print(f"# Executing command: {replaced_command}")
    if shell == "cmd":
        subprocess.call(replaced_command, shell=True)
    else:
        subprocess.call(["powershell.exe", "-command", replaced_command], shell=True)

def main():
    args = parse_arguments()
    list = open_list(args.list)
    

    if (args.command is None) and (args.scriptfile is None):
        print("Either --command or --scripfile must be used")
    # execute every command for every list item
    if args.command is not None:
        for list_item in list:
            print(f"# Processing list item: {list_item}")
            for command in args.command:
                replaced_command = replace_variable(command, list_item)
                execute_command(replaced_command, args.shell)
     
    if args.scriptfile is not None:
        for list_item in list:
            print(f"# Processing list item: {list_item}")
            scriptfile_commands = open_scriptfile(args.scriptfile)
            for command in scriptfile_commands:
                        replaced_command = replace_variable(command, list_item)
                        print(replaced_command)
                        execute_command(replaced_command, args.shell)

if __name__ == "__main__":
    main()