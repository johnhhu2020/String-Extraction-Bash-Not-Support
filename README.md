# String-Extraction-Bash-Not-Support <br />

## When string contains Apostrophe ' and Exclamation mark !, those will not be recognized by Linux and passing to grep, awk or sed programs, this Python class can help <br />


## Example usage: <br />
$ echo '' >  /home/+++/+++_Processed_names.txt <br />
$ head /+++/+++_Processed_names.txt <br />

$ python3 Str_Ext.py "+++/+++_images_names.txt" "+++/+++_Processed_names.txt" "Pictures/" ")" <br />
$ head /+++/+++_Processed_names.txt <br />
yankees +++.png <br />
oakland +++.png <br />
$ head /home/+++/+++_image_names.txt <br />
![image here](+++/+++/+++/Pictures/yankees +++.png) <br />
![image here](+++/+++/+++/Pictures/oakland +++.png) <br />
