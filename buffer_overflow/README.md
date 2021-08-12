# Introduction
This guide is meant to serve as an introduction to buffer overflows. This is by no means an advanced guide on exploit development, but rather a starting point for understanding the basics for buffer overflows as required by the OSCP exam. The python files provided should be easily modifiable to fit the use case of most simple buffer overflows. This guide was made by following The Cyber Mentor's [tutorial on buffer overflows](https://www.youtube.com/watch?v=qSnPayW6F7U&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=1), using [vulnserver](https://github.com/stephenbradshaw/vulnserver) as the vulnerable application.

**Environment requirements:**
- A Linux distribution such as Kali Linux
- A Windows machine
- Vulnserver
- Immunity Debugger
- mona.py installed to C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands

# Table of Contents
1. Spiking
2. Fuzzing
3. Finding the offset
4. Overwriting the EIP
5. Finding bad characters
6. Finding the right module
7. Generating shellcode
