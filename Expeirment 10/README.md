
<div align="center">

# 🖥️ OPERATING SYSTEM LAB
### Experiment No. 10

![Language](https://img.shields.io/badge/Language-C-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Ubuntu_Linux-orange?style=for-the-badge)
![Subject](https://img.shields.io/badge/Subject-COM--302-green?style=for-the-badge)

### Process Creation and Synchronization
**Using `fork()` and `wait()` System Calls**

---

</div>

## 🎯 Aim

To write and execute a C program that demonstrates
**process creation and synchronization** in Linux
using the `fork()` and `wait()` system calls.

## 📖 Introduction

In an Operating System, a process is a program
under execution. Linux provides system calls
to create and manage processes.

This experiment demonstrates how a parent process
creates a child process and waits for its completion.

## ⚙️ System Calls Used

| System Call | Description |
|-------------|-------------|
| `fork()` | Creates a new child process |
| `getpid()` | Returns the current process ID |
| `sleep(2)` | Pauses execution for 2 seconds |
| `wait(NULL)` | Waits for a child to terminate |
| `exit(0)` | Terminates the process successfully |

## 🔄 Working Principle

1. The program starts execution.
2. `fork()` creates a child process.
3. The child displays its Process ID (PID).
4. The child waits for 2 seconds using `sleep()`.
5. The child terminates using `exit(0)`.
6. The parent uses `wait(NULL)` to wait for the child.
7. After the child terminates, the parent displays
   the terminated child's PID.

## 💻 Source Code

The complete C program is available here:

📄 **[View Program](program.txt)**

## ▶️ Compilation and Execution

**Step 1:** Compile the C program.

```bash
gcc experiment10.c -o experiment10
```

**Step 2:** Execute the compiled program.

```bash
./experiment10
```

## 📸 Output Screenshot

The following screenshot shows the program's
execution in the Ubuntu terminal.

![Experiment 10 Output](output.jpg)

## ✅ Result

The C program was successfully executed in
Ubuntu Linux, demonstrating process creation
using `fork()` and synchronization using `wait()`.

The parent process waits until the child process
terminates before displaying its completion message.

---

<div align="center">

**Operating Systems Laboratory | COM-302**

*Experiment No. 10 — Process Management*

</div>


