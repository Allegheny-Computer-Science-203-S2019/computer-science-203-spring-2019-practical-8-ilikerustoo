# Reflection by Mohammad Khan

## Explain in detail the steps to take to compile and install the plugins

After fixing up `compute_tf_plugins.py`, we ran the shell script file contained in the`plugins-src` folder. This script contains several commands. The first command compiles the plugin and the second makes a `plugins` directory that contains the `.pyc` files. These are python configuration files which contain various essential configuration settings to get the plugin to work. After that it was a matter of running the same commands we have always been running for each practical.

## What are the benefits associated with adopting the plugin programming style?

This `plugins` style is was made around allowing others to build off your work. The way it works is that this programming style separates itself from the main program and leaving it as a `shell` and this case it executes the two frequency functions which are partitioned into two different steps. This partioning allows us to choose how we want to adjust or modify the implementation any way a programmer wants. This may be ideal for situations where others need to expand on work that is not their own.

## Explain the challenges that you encountered and how you overcame them

One challenge I encountered was understanding the style why python files needs to compiled. After some reading of the `Exercises in Programming Style` book, I understood that the style is meant to used as being able to customize implementation by making it separate from the main program and partitioning steps. The other challenge I still face is understand the point of the `pyc` files which I will do more reading for to understand better. Overall the practical was not difficult and required minimal addition to the code.
