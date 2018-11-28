import time
import datetime
def main():

    f= open("testtxt.txt" , "a+")
    f.write("testtesttesttest\n")
    timestamp = datetime.datetime.now().strftime("[%m/%d/%y - %I:%M:%S]")
    f.write(timestamp)
    f.close
    
if __name__=="__main__":
    main()

