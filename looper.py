import argparse
import subprocess

parser = argparse.ArgumentParser(prog="Looper",description="Program that loops commands for a given list", usage="looper.py -l .\list.txt -c 'New-Item $var -ItemType \"directory\"' -s powershell")
parser.add_argument('-l', '--list', help="a list of items (seperated by linebreak) that should be looped", required=True)
parser.add_argument('-c', '--command', help="command to be exeuted for each item in list; Surrounded by single quotes ''; Items from list can used as parameters with $var", required=True)
parser.add_argument('-s', '--shell', choices=['cmd','powershell'], help='specify the shell to use (cmd or powershell)', default="powershell", required=False)
parser.add_argument('-c2', '--command2', help="second command to be exeuted for each item in list", required=False)
args = parser.parse_args()
print(args.list, args.command)

with open(args.list) as file:
    var = [line.rstrip() for line in file]
    print(var)
file.close()

for v in var:
    command= args.command.replace(r"$var", v)
    print(f"# Executing command: {command}")
    if args.shell == "cmd":
        subprocess.call(command, shell=True)
    else:
                subprocess.call(["powershell.exe", "-command", command], shell=True)
    
    # Check if argument command2 is used
    if args.command2 is not None:
        command2= args.command2.replace(r"$var", v)
        print(f"# Executing command: {command2}")
        if args.shell == "cmd":
            subprocess.call(command2, shell=True)
        else:
            subprocess.call(["powershell.exe", "-command", command2], shell=True)








