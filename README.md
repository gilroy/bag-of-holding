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


## Reconaissance

### Port Scanning
full TCP scan
> sudo nmap -sC -sV -O --open -p- -oA nmap/full [targets]

full UDP scan
> sudo nmap -sU -p- -oA nmap/udp [targets]

scripts w/ ports
> sudo nmap --scripts vuln,safe,discovery -p \[ports] [targets]

### Directory Enumeration

### Header Analysis

## Exploitation
## Post-Exploitation
## Privilege Escalation 

### Linux Privesc

First and foremost, [g0tmi1k's blog](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation) is more comprehensive than the commands I will list here.

### Windows Privesc

[FuzzySecurity's blog post](https://www.fuzzysecurity.com/tutorials/16.html)

[Tib3rius's Windows PrivEsc course](https://www.udemy.com/course/windows-privilege-escalation/)
