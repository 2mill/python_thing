# Python Thing
A quick script for me to organize port information data.


## CSV information
CSV files should be split as such
`Room Number,Box Label,Port Count,Used,Patch Panel,Patch Port,Parent Room,Comments`.
The program will fail, or crash if it is not met. More information to be added later.
## Objects

Terminal

The Terminal object is the box that at most four ports. These ports are labeled for the specific panel side. Each Terminal has a PORT

- Port Objects

    As stated previously, each terminal has multiple ports which are connected to a side of the patch panel. 

    The port information should include if it is being used or not which it gathers from the initial CSV file.

    I should also have an object that parses CSV file rows for information that it needs? Yes and no, the file should be parsed and data separated logically before it is used to build the data structure.

Patch Panel

A patch panel is an array of ports that hold a patch for a port. 

Each patch panel should have a reference to a port.

Therefore, the program should be going through the files, and placing ports into an array. Each port will have a reference to its terminal box. Each terminal box as a result will have a reference to its room information etc.

The following tasks need to be completed in order to meet these goals:

- [ ]  CSV processing
    - [ ]  Gather CSV file data from CLI commands.
    - [ ]  Processes USED information into something more understandable for the computer(this should already be relatively finished.
    - [ ]  Split Patch Panel information into its own data sheet.
    - [ ]  Split Port information properly.
- [ ]  Continue with writing tasks for Ports and Terminals after CSV processor is completed.