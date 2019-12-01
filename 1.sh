sed s/"^[+-]"/\\n-/ lab1.txt |sed s/^*/#/ > tmp.py
rm begin.py
vim --cmd "vsplit tmp.py" begin.py
#vim -u vimrc.conf begin.txt
