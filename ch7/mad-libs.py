# mad-libs.py
# Searches a text file for keywords, asks a user for replacement for keyword, write results to file results.txt

import sys, re

def print_usage():
    ''' This function will print the usage information if too few command-line arguments are given '''
    print(f'Usage:')
    print(f'python mad-libs.py <filename> - Reads the contents of <filename> for keywords to replace Mad-Libs style.')

def get_contents(filename):
    ''' This function will read the input file contents in chunks and then return a list of the words in the file

        Argument: name of file to open and read from
        Returns: List of words in the file
    '''

    try:
        with open(filename, 'r') as f:
            
            size_to_read = 10
            chunk = f.read(size_to_read)
            lines = chunk
            
            while len(chunk) > 0:
                chunk = f.read(size_to_read)
                lines += chunk
            
            return lines.split(' ')
    
    except EnvironmentError:
        print(f'Unable to open file {filename}')

def replace_items(contents):
    ''' Take a list of strings and replace the string if it matches the regex NOUN, VERB, ADJECTIVE
        Argument: list of strings
        Returns: List of strings
    '''

    # Use regex to find NOUN, VERB, or ADJECTIVE
    regex = re.compile(r'ADJECTIVE|NOUN|VERB')

    for i in range(len(contents)):
        match = regex.match(contents[i])
        
        # If a match is found ask user to replace it
        if match:
            to_replace = match.group(0)
            contents[i] = regex.sub(input(f'Please enter a {to_replace.lower()}: '), contents[i])
    
    return contents

def print_results(contents):
    ''' Print a joined list contents to the screen
        Argument: a list of strings
    '''
    print(' '.join(contents))

def write_results(contents):
    ''' Write contents to a file named results.txt
        Argument: a list of strings
    '''

    try:
        with open('results.txt', 'w') as wf:
            to_write = ' '.join(contents)
            wf.write(to_write)
            print(f'Contents written to results.txt successfully')
    except EnvironmentError:
        print(f'Unable to write to file.')    

if len(sys.argv) <= 1:
    print_usage()
else:
    contents = get_contents(sys.argv[1])        # Get the contents of the file
       
    contents = replace_items(contents)          # Search contents for keywords and return replacements

    print_results(contents)                     # Print the results to the screen

    write_results(contents)                     # Write the results to a file