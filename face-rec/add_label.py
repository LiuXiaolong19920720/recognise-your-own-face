#!/usr/bin/env python  
  
import sys  
import os.path  
 
if __name__ == "__main__":  
  
    #if len(sys.argv) != 2:  
    #    print "usage: create_csv <base_path>"  
    #    sys.exit(1)  
  
    #BASE_PATH=sys.argv[1]  
    BASE_PATH="G:/att_faces"        
    SEPARATOR=";"    
    fh = open("at.txt",'w')  
  
    for dirname, dirnames, filenames in os.walk(BASE_PATH):  
        for subdirname in dirnames:  
            subject_path = os.path.join(dirname, subdirname)  
            for filename in os.listdir(subject_path):
                subdirname2 = subdirname[::-1]
                subdirname3 = subdirname2[:-1]
                subdirname4 = subdirname3[::-1]
                
                #print subdirname2[:-1]
                label = int(subdirname4)           
                abs_path = "%s/%s" % (subject_path, filename)  
                print "%s%s%d" % (abs_path, SEPARATOR, label)  
                fh.write(abs_path)  
                fh.write(SEPARATOR)  
                fh.write(str(label))  
                fh.write("\n")        
            label = label + 1  
    fh.close()  