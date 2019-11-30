echo True ansvers
grep "^-" begin.py |sed s/-/+/ | awk '{print "grep \"" $0 "\" lab1.txt"}' | bash |cat -n # True ansvers
echo False ansvers
grep "^-" begin.py | awk '{print "grep \"\\" $0 "\" lab1.txt"}' | bash |cat -n # True ansvers
#cat begin.py | awk '{print "grep \"\\" $0 "\" lab1.txt"}' | bash|cat -n   # False ansvers

