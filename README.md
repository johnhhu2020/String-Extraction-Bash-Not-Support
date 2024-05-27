# String-Extraction-Bash-Not-Support

## When string contains Apostrophe ' and Exclamation mark !, those will not be recognized by Linux and passing to grep, awk or sed programs, this Python class can help


## Example usage: 
$ echo '' >  /home/+++/RMd_Processed_image_names.txt
$ head /+++/+++_names.txt

$ python3 Str_Ext.py "+++/+++_names.txt" "+++/+++_Processed_names.txt" "Pictures/" ")"
$ head /+++/+++_Processed_names.txt
yankees +++.png
oakland +++.png
$ head /home/+++/RMd_image_names.txt 
![image here](+++/+++/+++/Pictures/yankees +++.png)
![image here](+++/+++/+++/Pictures/oakland +++.png)
