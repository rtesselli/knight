# Knight problem
## Definition

Implement a program that finds the shortest path a knight can take between two points on a standard 8x8 chessboard.

In chess, knights move in an L-shape: 2 squares along one dimension, 1 square along the other. See the
[Wikipedia explanation](https://en.wikipedia.org/wiki/Knight_(chess)#Movement)

### Functional Requirements

-----------------------

  - Write a command-line executable that reads instructions from standard input (stdin).

  - Instructions are lines (separated by newlines) in the following format:

```

D4 G7

D4 D5

```

  - The first of the space-separated values is the knight's starting position, the second is the knight's target
    position.

  - For each line in the input, your program should print (to standard out) the shortest path it found. So for the
    example above, it should print e.g.:

```

D4 F5 G7

D4 E2 F4 D5

```

### Notes

-----

  - Use language you are most comfortable with.

  - Feel free to use supporting libraries (but write the algorithm yourself).

  - Provide instructions for running your code and installing dependencies.

  - Document assumptions and decisions in readme file.

  - Apply development practices you would use to write production code.

  - It should be possible to run your program on Linux or macOS.

  - Please provide us with access to git repo with code when you're done.

## Setup
### With virtual environment
Create an environment with Python3.9 (e.g. with `conda create -n knight python=3.9 -y && conda activate knight`).

Go to the project root folder and run

```
pip install .
```

If you are a developer run:

```
pip install -e .[test]
```

Notice that if you are using zsh you need to escape square brackets with a backslash.

### With Docker
Go to the project root folder and run

```
docker build -f knight.dockerfile -t knight . && docker run --rm -it knight
``` 

## Run
The program reads the input from stdin, for example you can do:

from project root folder:

```
echo "D4 F6" | python -m knight.main
```

## Considerations
### Packaging
When I develop a new Python project I prefer to create an installable package, it makes easy to have your code available
in your Python environment.

Usually in local I create a Python virtual env with `conda`. In this case I've decided
to use Python3.9 since I do not have any particular constraint on dependencies.

If I plan to release my project somewhere, I usually take advantage of `bump2version` which makes easy to update the
package version. For this reason you will find the file `.bumpversion.cfg`.

Just to make it simpler to run this project, I've decided also to provide a dockerfile.

### Data model
I usually take advantage of Pydantic library, this library allows you to define rich data types and provide practical
functions to validate the inputs. This library has one limitation in which the data types defined with `BaseModel` are
not hashable objects, so you have to define your custom hash function in order to take advantage of other perks, such as
use your data models within sets.

I haven't put any constraint in ChessCoordinate about the size of the board, since the board can virtually be of any
dimension (see next paragraph).

### Parsing
I've decided to decouple the parse logic from the function which reads from input (in this case stdin). This makes
easier to switch input in the future.

### Logic
The problem required to find the solutions within a 8x8 chessboard, but in the future we could have boards of different
size, like 16x16. For this reason I've created the class ChessBoard to have a variable size.

I've decided to go with the BFS algorithm to find the solutions, since BFS is a general purpose algorithm I've
written the generic algorithm which can be used for different tasks. In order to apply it on the chess problem it is
sufficient to define the custom neighbors functions.

### Output
I've decided to decouple the presentation layer from the logic, so in the future it is easy to change a new output
function (which does not necessarily print in stdout).