# 8 piece puzzle

## Input Format

The accepted input is column-wise, i.e. 147258360 will correspond to the following state

```
+-+-+-+
|1|2|3|
+-+-+-+
|4|5|6|
+-+-+-+
|7|8|0|
+-+-+-+
```

## Run the code
Run the following command to run the code with default input 147028356

``` python3.5 8puzzle.py```

To run the code with custom initial state

``` python3.5 8puzzle.py --initial_state <initial_state>```

## Output

The command above generates the following three text files:

1. nodePath.txt - contains nodes that form the solution, starting from initial node to goal node. 
2. NodesInfo.txt - contains the information of child node and parent node. The first column corrsponds to the child node and the second colunm corresponds to parent node. 
3. Nodes.txt - contains a list of all the explored states

## Libraries used
This code uses the following libraries:
1. numpy - for saving the output to a text file
2. collections.deque - to implement queue
3. argparse - to read commandline arguments 
