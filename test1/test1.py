import angr

p = angr.Project("test1")

# This program takes test0 one step further by "encrypting" the input first
# In order to find the correct input, we will simply hook the instruction
# which would be hit when we would enter the correct password
# We then simply solve for the input

@p.hook(p.loader.main_object.min_addr + 0x8df)
def my_hook(state):
    inp = state.posix.stdin.load(0, state.posix.stdin.size)
    print("I would propose the following input:")
    print(state.solver.eval(inp, cast_to=bytes))

init_state = p.factory.entry_state(stdin=angr.SimFile)

sm = p.factory.simulation_manager(init_state)
sm.run()

