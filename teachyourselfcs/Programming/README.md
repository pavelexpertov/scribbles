# Programming Module

## How to get scheme REPL environment
Use docker [image](https://hub.docker.com/r/sritchie/mit-scheme#).

## How to run scheme so a local directory is mounted into the docker container?
Make sure you got the script of `mit-scheme.sh`
Then run `./mit-scheme.sh`

## How to load files into scheme REPL?
Use this procedure and replace the absolute path with your one (i.e. Basically use `pwd` command and/or expand '~' as necessary). Example:
```scheme
(load "/home/pavel/learning/Programming/Chapter_1/exercise_1.3.scm")
```
**Note**: If you type `echo $(pwd)/exercise.1.7.scm` and use __Tab__ key after just the closing round bracket, that should ease the process of generating abosulte paths easily.
