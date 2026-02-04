# Introduction to Python for DevOps

import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the cpu threshold:"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu usage:", current_cpu)
    
    if current_cpu > cpu_threshold:
        print("Alert on email")
    else:
        print("safe")
check_cpu_threshold()

Output:

PS C:\Users\Satish_More\Documents\Josh-pythondevops\Day-01\practice> python .\cpu_usage.py       
Enter the cpu threshold:20                                                                       
current cpu usage: 3.2
safe
