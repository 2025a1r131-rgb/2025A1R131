<div align="center">🖥️ Operating Systems Laboratory
🧪 Experiment 10 · Process Creation & Synchronization
Understanding fork(), wait() and parent–child processes in Linux



</div>🎯 Aim
To write and execute a C program that demonstrates the creation of a child process using fork() and the synchronization of parent and child processes using wait() in Ubuntu Linux.
📌 Experiment at a Glance
Detail	Information
Experiment	No. 10
Subject	Operating Systems (COM-302)
Language	C
Environment	Ubuntu Linux
Concept	Process creation and synchronization
System calls / functions	fork(), getpid(), sleep(), wait(), exit()


🧠 Concept
A process is a program in execution. In this experiment, fork() creates a new child process. Both the parent and child then continue from the point of the fork() call, but take different branches of the program:
- Child process: Prints its process ID, sleeps for two seconds, and exits.
- Parent process: Prints a waiting message, calls wait(NULL), and then prints the PID of the child that terminated.
This shows how the parent can wait for its child to finish before proceeding.
🔄 Execution Flow
```mermaid
flowchart TD
    A([Program starts]) --> B[Call fork()]
    B --> C{Which process?}
    C -->|Child: p = 0| D[Display child PID]
    D --> E[Sleep for 2 seconds]
    E --> F[Exit child process]
    C -->|Parent: p > 0| G[Display waiting message]
    G --> H[Call wait(NULL)]
    F --> H
    H --> I[Display terminated child PID]
    I --> J([Program completes])
```
⚙️ Functions Used
Function	Purpose
fork()	Creates a child process
getpid()	Gets the PID of the calling process
sleep(2)	Suspends the child for two seconds
wait(NULL)	Makes the parent wait for a child to terminate
exit(0)	Ends the child process successfully


💻 Source Code
📄 [View the complete C program](program.txt)

The source code is stored as program.txt for submission.
▶️ How to Compile and Run
On Ubuntu, open a terminal in the directory containing program.txt and enter:
cp program.txt experiment10.c
gcc experiment10.c -o experiment10
./experiment10
Note: The parent and child's initial print messages can appear in either order because process scheduling varies. The PID will also differ between runs.

📸 Terminal Output
<div align="center"><img src="output.jpg" alt="Illustrative Ubuntu terminal output showing child process creation and parent waiting for child termination" width="900" />Illustrative sample of the expected Ubuntu terminal output.
</div>[!IMPORTANT]
This image is generated sample output, not a screenshot of an actual program execution. For a lab submission requiring execution evidence, replace output.jpg with a screenshot taken after running the code in your Ubuntu VM.

✅ Result
The program demonstrates process creation with fork() and parent–child synchronization with wait(). The parent prints the terminated child's PID after the child exits.
<div align="center">Operating Systems Lab · COM-302
Experiment 10 — Process Management
</div>


