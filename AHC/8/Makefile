
.PHONY: run
run:
	FOR /L %%i IN (0, 1, 9) DO tester.exe C:\Users\horis\AppData\Local\Microsoft\WindowsApps\python3.exe a.py < in\000%%i.txt > out\000%%i.txt 2> score\000%%i.txt 
	FOR /L %%i IN (10, 1, 99) DO tester.exe C:\Users\horis\AppData\Local\Microsoft\WindowsApps\python3.exe a.py < in\00%%i.txt > out\00%%i.txt 2> score\00%%i.txt
	python sum_score.py

.PHONY: run-small
run-small:
	FOR /L %%i IN (0, 1, 9) DO tester.exe C:\Users\horis\AppData\Local\Microsoft\WindowsApps\python3.exe a.py < in\000%%i.txt > out\000%%i.txt 2> score\000%%i.txt 
	python sum_score.py

