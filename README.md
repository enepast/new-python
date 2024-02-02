# Python Program Generator

## Overview

This Python script serves as a program generator, automating the creation of basic Python scripts equipped with argparse functionality for command-line argument parsing. The primary aim is to streamline the process of initializing Python programs.

Disclaimer: This script draws inspiration from Ken Youens-Clark's book, offering a practical approach to script generation.


## How to Use

1. Clone the Repository:

Clone the repository containing the script generator.

```
git clone <repository_url>
```

2. Navigate to the Script Generator:

Change your working directory to the script generator folder.

```
cd <new.py folder>
```

3. Run the Script Generator:

Execute the script generator, providing the desired program name and optional details.

```
./new.py my_program -n "Your Name" -e "your.email@example.com" -p "Specify the purpose"
```

4. Review and Confirm:

The script will prompt you with the generated program. Review the details and confirm if you want to overwrite an existing file.

5. Generated Script:

The new Python script will be created in the current working directory, based on the provided details.


## Script Structure

The generated Python script consists of the following sections:

### Docstring
The script starts with a docstring containing the author's name, email (if provided), the current date, and the specified purpose of the script.

### Command-line Arguments
The `get_args` function uses the `argparse` module to define and parse command-line arguments. It includes positional arguments, named string and integer arguments, a readable file argument, and a boolean flag.

### Main Function
The `main` function verifies the existence of the specified file, prompts for confirmation if the file already exists, and writes the script based on the provided details. Additionally, it sets executable permissions on non-Windows systems.

### Body Template
The `body` function returns a string representing the template for the main body of the Python script. It includes a shebang line (`#!/usr/bin/env python3`) and imports the `argparse` module.


## Additional Functions

`get_defaults`: Retrieves default values from `~/.new.py` if available.


## Customization

Modify Defaults: You can customize default values by editing the `~/.new.py` file.
Extend Functionality: The script can be extended to include additional functionality based on specific requirements.


## Important Notes

Ensure the script generator (`script_generator.py`) is executable (`chmod +x script_generator.py`).
Review the generated script to ensure it meets your requirements before execution.

Feel free to adapt and enhance the script generator based on your needs. Happy coding!
