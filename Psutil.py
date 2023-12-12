# Script:                       ops301d10-challenge 11
# Author:                       Bryanna Fox
# Date of latest revision:      12/11/2023
# Purpose:                      Psutil 

import psutil

def get_system_info():
    # Time spent by normal processes executing in user mode
    user_time = psutil.cpu_times().user

    # Time spent by processes executing in kernel mode
    kernel_time = psutil.cpu_times().system

    # Time when system was idle
    idle_time = psutil.cpu_times().idle

    # Time spent by priority processes executing in user mode
    priority_user_time = psutil.cpu_times().nice

    # Time spent waiting for I/O to complete
    io_wait_time = psutil.cpu_times().iowait

    # Time spent for servicing hardware interrupts
    irq_time = psutil.cpu_times().irq

    # Time spent for servicing software interrupts
    softirq_time = psutil.cpu_times().softirq

    # Time spent by other operating systems running in a virtualized environment
    guest_time = psutil.cpu_times().guest

    # Time spent running a virtual CPU for guest operating systems
    # under the control of the Linux kernel
    guest_nice_time = psutil.cpu_times().guest_nice

    # Print the collected information
    print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")
    print(f"Time when system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {irq_time} seconds")
    print(f"Time spent for servicing software interrupts: {softirq_time} seconds")
    print(f"Time spent by other operating systems running in a virtualized environment: {guest_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_nice_time} seconds")


