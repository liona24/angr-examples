import angr

p = angr.Project("test0")
state = p.factory.entry_state(stdin=angr.SimFile)

while True:
    succ = state.step()
    if len(succ.successors) != 1:
        break
    state = succ.successors[0]

s1, s2 = succ.successors
input_so_far = s1.posix.stdin.load(0, state.posix.stdin.size)

print("I propose the following input:")
print(s1.solver.eval(input_so_far, cast_to=bytes))

