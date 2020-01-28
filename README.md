# NDS Memory Lurker
Also known as: **Nintendo DS Memory Dump Address Reference Lurker**

A very short script in Python that simplified looking up values in Assembly in Mario Kart DS significantly.

The goal of the script is to load a DeSmuMe RAM dump and upon providing a memory address of a value in stack that interests us, trace it back to where it was initialized so that it can be looked up later on in Disassembly and instructions that reassign those values can be found.
## Usage
- Make a full 16MB Memory Dump using DeSmuMe and place it in the same folder as the script. Adjust the filename in the first line of the .py script.
- Using DeSmuMe's RAM Search or RAM Watch find a value in RAM that interests you. Take note of its address and edit the fourth line with the address of the value found in RAM.
- Run the script to trace back all the references back to the ARM9.bin area.
- Use a Disassembler to find instructions that either allocate structures or modify their values at a specific index.