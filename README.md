For all these tasks python & pip needs to be installed in the machine
# Task A
Input will be taken from command prompt.
```
Sample Input:
2
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000

Sample Output:
88200
25200
```
# Task B
Running Details:
Step 1) pip install requirements.txt
Step 2) python app.py
Step 3) A browser needs to be opened and following link should be accessed http://127.0.0.1:5000
		A text file named input.txt is present as input sample for the task.
```
Sample Input:
2
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000

Sample Output:
{"message": "Success", value:[88200,25200]}
```
# Task C
docker build -t taskBL:latest
docker run -d -p 5000:5000 taskBL