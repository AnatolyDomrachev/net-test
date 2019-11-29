echo True ansvers
sed s/-/+/ result.txt | awk '{print "grep \"" $0 "\" lab1.txt"}' | bash |cat -n # True ansvers
echo False ansvers
cat result.txt | awk '{print "grep \"\\" $0 "\" lab1.txt"}' | bash|cat -n   # False ansvers

