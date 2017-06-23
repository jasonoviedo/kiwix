## Welcome to Kiwi's Self-Driving Kiwibot Simulator

This simulator provides students with a real challenge of being a self driving engineer at Kiwi data science division.

### Available Game Builbs (Precompiled builds of the simulator)

Instructions: Download the zip file, extract it and run (see How to Run) the execution file.

Version alpha, 6/21/17

[Linux]()
[Mac]()
[Windows]()


### How to run

In [Linux]() the zip file contains two [ELF files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) that for security reasons are not marked to be executable. To give a file a executable flag the procedure is

```bash
chmod a+x file
```
A short summary of `chmod` can be found on the man pages using `man chmod` or on the [web](https://explainshell.com/explain?cmd=chmod+a%2Bx+file).
Be sure to choose the corresponding architecture of your OS.

| File   | Recommended Architecture |
| ----   |:------------------------:|
| x86    | 32 Bit OS                |
| x86-64 | 64 Bit OS                |

![KiwiBot Challenge](./Challenge.png)

# Conda Enviroment Kiwi Enviroment

TODO explain conda and how to set up a new enviroment.

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
