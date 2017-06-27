## Welcome to Kiwi's Self-Driving Kiwibot Simulator

This simulator provides students with a real challenge of being a self driving engineer at Kiwi data science division.

![KiwiBot Challenge](./Challenge.png)

### Available Game Builds (Precompiled builds of the simulator)

Instructions: Download the zip file, extract it and run (see How to Run) the execution file.

Version alpha, 6/21/17

### [Linux](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_LinuxUniversal.rar)

### [Mac](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_Mac.app.zip)

### [Windows](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_win64.rar)

### **Releases on** [Link](https://github.com/Davidnet/kiwix/releases)

### How to run

#### Linux

In [Linux](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_LinuxUniversal.rar) the zip file contains two [ELF files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) that for security reasons are not marked to be executable. To give a file a executable flag the procedure is

```bash
$ chmod a+x file
```
A short summary of `chmod` can be found on the man pages using `man chmod` or on the [web](https://explainshell.com/explain?cmd=chmod+a%2Bx+file).
Be sure to choose the corresponding architecture of your OS.

| File   | Recommended Architecture |
| ----   |:------------------------:|
| x86    | 32 Bit OS                |
| x86-64 | 64 Bit OS                |

After giving the executable bits to the file, recall that for executing the file, use
```bash
$ ./file
```


#### Mac

In [Mac](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_Mac.app.zip) a single app package is provided, is independent of the architecture. Any problem, please submit a issue report to this repository.

#### Windows

In [Windows](https://github.com/Davidnet/kiwix/releases/download/v0.1/KiwiGame_win64.rar) only a 64 bit version is provided, if you are interested on a 32 build, please open an issue on the issue tracker.

### General Recommendations

Is recommendable that if you don't have a GPU available on your system, please run the unity executable on low settings.

### General Controls

You can use any joystick supported by your OS, in the keyboard the following controls are provided (standard wasd mapping):

| keyboard   | Action |
| ----   |:------------------------:|
| wasd  | Control motion             |
| Space  | Break                |
| ESC    | Open close main menu |
|  C     | Change camera |
|  R     | Start recording |
|  P     | Begin AutoPilot connection |

### AutoPilot Communication

As you can observe in the communication tab, you can select a port, IP address to send images at a customizable size. A server script (TODO) is provided to give you a sketch to work on.

The program is accepting the following format (example in python provided):

```python
'{ "steering" : "%f", "throttle" : "%f" }' % (steering, throttle)
```

The possible values are on the range:

| Value   | Range |
| ----   |:------------------------:|
| Steering   |  {-1,1}                |
| throttle  | {-1,1}                |




# Conda Kiwi Enviroment

Conda is a package manager application that quickly installs, runs, and updates packages and their dependencies. Conda is also an environment manager application. A conda environment is a directory that contains a specific collection of conda packages


We suggest (not a requirement) to use the following conda environments so you can start as soon as possible to build your own AutoPilot on python.


### Linux (ONLY CPU)

```
$ conda env create -f environment_linux_nogpu.yml
```
Main packages provided: Tensorflow with GPU support, Keras and OpenCV.


### Linux (GPU with CUDA ENABLED)

```bash
$ conda env create -f environment_linux_gpu.yml
```

Main packages provided: Tensorflow with GPU support, Keras and OpenCV.


# Kiwi Auto Pilot

The Kiwi Auto Pilot is a minimalist project completely based on  a strip down version of [Donkey](https://github.com/wroscoe/donkey)
written by night-selfdriver [Will Roscoe](https://github.com/wroscoe)

A server.py and NeuronalNetwork.py is provided to give you a mock up to guide you.

![Kiwibot](./KIWIBOT.png)

# Contributors


Project by: [Carlos Zubieta](https://www.linkedin.com/in/carlos-zubieta-52217875/), [Jason Oviedo](https://www.linkedin.com/in/jason-oviedo-46611914/), and [David Cardozo](https://www.linkedin.com/in/davidcardozo/).

Kiwi Campus 2017
