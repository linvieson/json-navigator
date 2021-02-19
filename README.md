# Json Navigator

## Description
This program gets the json file from the user. It asks a user, which part of
the json object he or she wants to see and outputs its value.

## Usage
``` python
import json_navigator.py
```

The program will run automatically. It will ask the user to enter a path to
the json file that he wants to see. Then it will output the available keys,
and the user can choose what values he or she wants to see. He or she can enter
ALL to see all the children of a key, or enter a specific key from the
available ones to see only that key value.

## Example of running
Start the program. It will ask a path to json file. The program outputs the
following:

![Output](/images/img1.png?raw=true "output")

For instance, if the user enters 'name', the program outputs the following:

![Output](/images/img2.png?raw=true "output")

If an object is a dictionary, the program asks to enter a children key. If an
object is a list, the program asks to enter a list index:

![Output](/images/img3.png?raw=true "output")

If the user enters 'ALL', the output the next:

![Output](/images/img4.png?raw=true "output")

The program ends its work.

## Results
The result of a program is a navigator through the json file, depicted as a
python dictionary. The user can see particular values he or she is interested
in, thus it creates a convenient environment of analyzing a json file.

## License
[MIT](https://github.com/linvieson/json-navigator/blob/main/LICENSE.txt)