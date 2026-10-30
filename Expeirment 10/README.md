
<div align="center">

# 🖥️ Operating System Laboratory
### 🧪 Experiment No. 10

**Process Creation and Synchronization**

![C](https://img.shields.io/badge/Language-C-blue)
![Ubuntu](https://img.shields.io/badge/OS-Ubuntu-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

</div>

## 🎯 Aim
To demonstrate process creation and synchronization
using `fork()` and `wait()` system calls in Linux.

## 📚 Experiment Details

| Detail | Information |
|--------|-------------|
| Experiment | No. 10 |
| Subject | Operating System |
| Course Code | COM-302 |
| Language | C |
| Platform | Ubuntu Linux |
| Compiler | GCC |

## 📖 Description

This program demonstrates how a parent process
creates a child process using `fork()`.

The child executes its instructions while the
parent waits for its termination using `wait()`.

## ⚙️ System Calls Used

| Function | Purpose |
|----------|---------|
| `fork()` | Creates a child process |
| `getpid()` | Gets the process ID |
| `sleep()` | Delays execution |
| `wait()` | Waits for child termination |
| `exit()` | Terminates a process |

## 💻 Source Code

📄 [Click Here to View Program](program.txt)

## ▶️ How to Execute

Compile the program:

```bash
gcc -x c program.txt -o experiment10
```

Run the program:

```bash
./experiment10
```

## 📸 Output

The following image illustrates the program
execution in the Ubuntu terminal.

![Experiment 10 Output](output.jpg)

## ✅ Result

The C program demonstrates process creation
using `fork()` and synchronization using `wait()`.

The parent process waits until the child
process terminates successfully.

---

<div align="center">

### 🎓 Operating Systems Lab
**COM-302 | Experiment 10**

*Process Management in Linux*

</div>

