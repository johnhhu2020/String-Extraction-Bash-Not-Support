class Str_Ext:
    '''
    Str_Extraction: 
    # This class and its function will help you extract desired string part from complex string with dymbols like ', ", !, [, (, *, . 
    # Which you cant make it in your terminal and passing parameters you wish, because Bash not support old string with !, ' symbols in it

    str_file:
        location in file system like: pwd appened file name
        the file containing complec string lines like this one: /home/me/file1.txt
          "![+++'s ++++ *** x.](+++/Pictures/+++ consideration.png)"
    processed_file: 
        the empty file in which you want to keep your cleaned strings line by line 
    delimit1: 
        something unique enough and universal which can help you identify and extract all the desired string parts
        the 1st delimit, the "Pictures/" if we want to extract "+++ consideration.png"
    delimit2: 
        the 2ed delimit, the ")" if we want to extract "+++ consideration.png"
    '''
    
    
    def __init__(self):
        # , str_file, processed_file, delimit1, delimit2
        
        import sys
        self.str_file = sys.argv[1]
        self.processed_file = sys.argv[2]
        self.delimit1 = sys.argv[3]
        self.delimit2 = sys.argv[4]

        #self.str_file = str_file
        #self.processed_file = processed_file
        #self.delimit1 = delimit1
        #self.delimit2 = delimit2
    
    def ext(self):
        with open(self.str_file, "r") as input: 
            
            with open(self.processed_file, "w") as output: 
                
                for line in input: 
                    str = line.split(self.delimit1)[-1]
                    str = str.split(self.delimit2)[0]

                    output.write(str + '\n')




if __name__ == "__main__":
    Ext = Str_Ext()
    Ext.ext()


# Not doing it here, but passing parameters in bash, makes it more useful
# This code works I just want to use it in Bash
#Ext = Str_Ext("+++_names.txt", "+++_Processed_names.txt", "Pictures/", ")")
#Ext.ext()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
