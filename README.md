# Looper

Looper is a simple python script that uses a list of items (e.g. System names) as input to execute one or multiple commands in a loop.

## Getting Started

### Usage
The tool can be used with several arguments, at least `--list` and `--command`.

```bash
looper.py -l .\list.txt -c 'New-Item $var -ItemType \"directory\"'
```

### Options
  `-h`, `--help` | show this help message and exit<br>
  `-l LIST`, `--list LIST` | a list of items (seperated by linebreak) that should be looped<br>
  `-c COMMAND`, `--command COMMAND` | command's to be exeuted for each item in list; surrounded by single quotes ''; Items from list can used as parameters with `$var`; Parameter can be used multiple times for more than one command.<br>
  `-f SCRIPTFILE, '--scriptfile SCRIPTFILE` | loads a file containing the commands that sould be executed. Items from list can used in the script with `$var`<br>
  `-s {cmd,powershell}`, `--shell {cmd,powershell}` | specify the shell to use (cmd or powershell)<br>

### Examples
Execute a combined PowerShell command
```bash
python looper.py -l ./list.txt -c 'mkdir $var; $files = Get-ChildItem -Path . -Filter "$var*" -File; $files | ForEach-Object { Move-Item -Path $_.FullName -Destination .\$var }; rmdir $var' -s powershell
```

Execute multiple seperate commands
```bash
python looper.py -l ./list.txt -c 'mkdir $var' -c '$files = Get-ChildItem -Path . -Filter "$var*" -File; $files | ForEach-Object { Move-Item -Path $_.FullName -Destination .\$var }' -c 'rmdir $var' -s powershell
```

Use a scriptfile for execution instead of a command
```bash
 python looper.py -l list.txt -f .\script.txt -s powershell
 ```