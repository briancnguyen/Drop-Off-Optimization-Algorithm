# Drop Off Buddies Algorithm

## Problem Statement
Brian, Akash, and their buddies are chilling at Brian's home late at night. Brian offers to drive and drop his buddies off closer to their homes so that they can get back home safe. Since the roads are long in his area, Brian would also like to get back home as soon as as he can. Can you plan transportation so that everyone can get home as efficiently as possible?

## Run this Short Command to Generate Every Output
### Command Layout
- python3 shortcut.py `directory_to_inputs` `directory_to_outputs`

### Example
- `python3 shortcut.py inputs outputs`

## Solver Commands (Advanced)
### Command Layout
- python3 solver.py `path_to_input_file` `directory_to_outputs` `algorithm` `input_file_size`
- python3 solver.py --all `directory_to_inputs` `directory_to_outputs` `algorithm` `input_file_size`

### Argument Values
- algorithm = ILP, ANT, TSP
- input_file_size = 50, 100, 200, ALL

### Example
- `python3 solver.py inputs/text.in outputs TSP 200`
- `python3 solver.py --all inputs outputs TSP 200`