import angr
import claripy

"""
This example demonstrates some of the memory API.
The goal is to make the example binary exit with
code 0.
"""

p = angr.Project("test2", auto_load_libs=False)

flag_addr = p.loader.find_symbol("flag").rebased_addr
print("Flag @", hex(flag_addr))

flag_size = 0xd

# use unicorn for faster simulation
init_state = p.factory.entry_state(add_options=angr.options.unicorn)

# setup symbolic memory for our flag ..
flag = [ claripy.BVS("flag_%d" % i, 8) for i in range(flag_size) ]
# .. add some constraints to enforce ASCII characters ..
for c in flag:
    init_state.solver.add(c < 0x7f)
    init_state.solver.add(c > 0x20)
flag = claripy.Concat(*flag)

# .. and store it into the state
init_state.memory.store(flag_addr, flag)

# run the simulation until completion
sm = p.factory.simulation_manager(init_state)
sm.run()

final_state = sm.deadended[0]

# enforce exit code
final_state.solver.add(final_state.regs.dil == 0)

result = final_state.solver.eval(flag, cast_to=bytes)
print("The flag is", result)

