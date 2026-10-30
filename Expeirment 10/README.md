
# Experiment No. 10

## Aim
To write a C program to demonstrate process
creation and synchronization using fork()
and wait() system calls in Linux.

## Software Used
Ubuntu Linux

## Language
C Programming

## Description
This program demonstrates parent and child
process execution in Linux.

- fork() creates a new child process.
- getpid() returns the process ID.
- sleep(2) pauses the child for 2 seconds.
- wait(NULL) makes the parent wait until
  the child terminates.
- exit(0) terminates the child successfully.

## Result
The program was executed successfully.
The parent process waited for the child
process to terminate.

## Output
![Program Output](output.jpg)

