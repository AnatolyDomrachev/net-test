sed s/"^[+-]"/\\n-/ lab1.txt |sed s/^*/------------------------------------------------------\\n*/ > tmp.txt
vim --cmd "vsplit tmp.txt" begin.txt
#vim -u vimrc.conf begin.txt
