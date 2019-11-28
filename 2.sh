sed s/-/+/ result.txt | awk '{print "grep \"" $0 "\" lab1.txt"}' | bash

