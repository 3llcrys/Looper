# Looper

Looper is a simple python script that uses a list of items (e.g. System names) as input to execute commands in a loop.

## Getting Started

### Usage
The tool can be used with several arguments, at least `--list` and `--command`.

```bash
looper.py -l .\list.txt -c 'New-Item $var -ItemType \"directory\"'
```

### Options
  `-h`, `--help` | show this help message and exit
  `-l LIST`, `--list LIST` | a list of items (seperated by linebreak) that should be looped
  `-c COMMAND`, `--command COMMAND` | command to be exeuted for each item in list; surrounded by single quotes ''; Items from list can used as parameters with `$var`
  `-s {cmd,powershell}`, `--shell {cmd,powershell}` | specify the shell to use (cmd or powershell)
  -`c2 COMMAND2`, `--command2 COMMAND2` | second command to be exeuted for each item in list

### Examples
Execute a combined PowerShell command
```bash
python looper.py -l ./list.txt -c 'mkdir $var; $files = Get-ChildItem -Path . -Filter "$var*" -File; $files | ForEach-Object { Move-Item -Path $_.FullName -Destination .\$var }' -s powershell
```

Execute a two seperate commands
```bash
python looper.py -l ./list.txt -c 'mkdir $var' -c2 '$files = Get-ChildItem -Path . -Filter "$var*" -File; $files | ForEach-Object { Move-Item -Path $_.FullName -Destination .\$var }' -s powershell
```