import time

max_retries = 5
attampts = 0
wait_time = 1

while attampts<max_retries:
    print("this is you attampt no # ", attampts+1, " And you qait time is = ", wait_time, " Sec")
    attampts=attampts+1
    time.sleep(wait_time)
    
    wait_time = wait_time*2

    


