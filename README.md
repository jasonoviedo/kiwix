## Welcome to Kiwi's Self-Driving Kiwibot Simulator

This simulator provides students with a real challenge of being a self driving engineer at Kiwi data science division.

![KiwiBot Challenge](./Challenge.png)

### Available Game Builds (Precompiled builds of the simulator)

Instructions: Download the zip file, extract it and run (see How to Run) the execution file.

Version alpha, 6/21/17

[Linux](https://drive.google.com/open?id=0BwDN7B4kVM12SnBYWVp2NXJoeHc)
[Mac](https://drive.google.com/open?id=0BwDN7B4kVM12S1otYm1yN2JIbmM)
[Windows](https://drive.google.com/open?id=0BwDN7B4kVM12VFZwN21lb21hRDA)


### How to run

#### Linux

In [Linux](https://drive.google.com/open?id=0BwDN7B4kVM12SnBYWVp2NXJoeHc) the zip file contains two [ELF files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) that for security reasons are not marked to be executable. To give a file a executable flag the procedure is

```bash
chmod a+x file
```
A short summary of `chmod` can be found on the man pages using `man chmod` or on the [web](https://explainshell.com/explain?cmd=chmod+a%2Bx+file).
Be sure to choose the corresponding architecture of your OS.

| File   | Recommended Architecture |
| ----   |:------------------------:|
| x86    | 32 Bit OS                |
| x86-64 | 64 Bit OS                |

#### Mac

In [Mac](https://drive.google.com/open?id=0BwDN7B4kVM12S1otYm1yN2JIbmM) a single app package is provided, is independent of the architecture. Any problem, please submit a issue report to this repository.

#### Windows

In [Windows](https://drive.google.com/open?id=0BwDN7B4kVM12VFZwN21lb21hRDA) only a 64 bit version is provided, if you are interested on a 32 build, please open an issue on the issue tracker.

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
| Steering   | TBA               |
| throttle  | TBA                |




# Conda Enviroment Kiwi Enviroment

We suggest (not a requirement) to use the following conda environments so you can start building your own AutoPilot on python.


TODO explain conda and how to set up a new enviroment.

### Linux

```bash
conda env create -f enviroment.yml
```





# Kiwi Auto Pilot

The Kiwi Auto Pilot is a minimalist project completly based on  a strip down version of [Donkey](https://github.com/wroscoe/donkey)
written by night-selfdriver [Will Roscoe](https://github.com/wroscoe)

## Instructions to train

TBA

TODO: Export

Donkey instructions TBA

## Instructions to SelfDriving

TBA

Do we add a SelfDriving Pilot?

![Kiwibot](./KIWIBOT.png)
