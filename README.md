# File_to_File_Data_Processing

The overall concept of this exercise is straight forward, write python code to read raw data from a file and output it to another file.  What is the twist cause it can't be that simple? It is not much of one, the scripting will be broken up into two parts.  The first part will be the processing of the information from the file and setting it up to go into the output and the second part will be the handling the reading and writing to the files.

Where will some of this come up in industry?  Data Export from one data system to another is one example.  Many software suites collect and maintain their information/data internally in a proprietary format but to export it, you have to go down to a least common factor method, a straight text file.  One system will export the text file and the other system will import the text file.  The may be the need to "clean" or "sanitize" the data during the process as not all exports are clean.

You are to design and implement a class in Python.  That is one that can be import or used by a script much like you have in the Scripting class previous.  The class is to have all the functionality to process and prepare the incoming data for export to a new file.  The class will not read from files, just process data given to it.

An example might be the line of data read in contains several "fields" of date like a address City.   The Script will send the line of data to the Module and in the module the City field information is found and copied and then returned to the script.  Then when the script has used this to pull all the information, it will send all the extracted information back into the module to be created into a single line which is then put into the output file by the Script.

What processing might happen or changes?  Maybe the State in in coming information is a full blown state name but in the output file, it has to be the 2 letter postal abbreviation.  That type of information will be in the documents provided but you will need to do the logic on how it happens.

Then you are to write a script file that will use the class to process a data file and output a new data file in a new format that would be "acceptable" for a different system based on the specs given.  File control and file input and output are the responsibility of this script.  Any data cleansing or sanitation may happen here in the future.

Your class will need to be extensively documented so that it can be handed off to another person to use on a project.  The user should not have to contact you for how to use your class.  All the documentation they need should be in the class itself.  This means a lot of comments and use of the docstring functionality of Python.  The class and all functions in the class need to have documentation so that help(function name) can be employed. 
