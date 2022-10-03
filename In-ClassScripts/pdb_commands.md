# PDB Commands
#-------------

### Navigating Code --------------------------------

# Orientation
(l)ist - list 11 lines surrounding the current line
(w)here - display the file and number of current line

# Movement 
(n)ext     - step over and execute the next line
(s)tep     - if next line is a function, step in, else go to next line
(c)ontinue - continue until the next breakpoint
(r)eturn   - continue until the current functions return is encountered

### Controlling Execution ---------------------------------

(b)breakpoint - list breakpoints, and line numbers
(b #)         - set a breakpoint at line number #
(clear #)     - clear breakpoint at line number #
(h)elp - show help
(q)uit - quit debugger

### Interact ---------------------------------
p <name>     - print variable <name> contents
!<expr>      - execute Python code <expr>
run<args>    - restart pdb with arguments provided
q(uit)       - exit pdb

# Loading PDB before Python 3.7

```python
import pdb; pdb.set_trace()
```
# Loading PDB Python 3.7 and on

```python
breakpoint()
```

