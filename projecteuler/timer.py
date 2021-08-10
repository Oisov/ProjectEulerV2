import timeit
import multiprocessing

"""
A generic method for timing project euler files
"""


def time_euler_file(command):
    start_time = timeit.time()
    eval(command)
    return timeit.time() - start_time


# > I've written my program but should it take days to get to the answer?
# >
# > Absolutely not! Each problem has been designed according to a "one-minute
# > rule", which means that although it may take several hours to design a
# > successful algorithm with more difficult problems, an efficient
# > implementation will allow a solution to be obtained on a modestly powered
# > computer in less than one minute.
#
# Source: https://projecteuler.net/about
PROJECT_EULER_TIMELIMIT = 1


def within_project_euler_timelimit(fun, parameters=None):
    p = multiprocessing.Process(target=fun, args=(parameters,))
    p.start()

    # Wait for the function to finish or PROJECT_EULER_TIMELIMIT seconds
    p.join(PROJECT_EULER_TIMELIMIT)

    # If thread is still active
    if p.is_alive():
        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()
        p.join()
        return False
    return True


def euler_timer(setup, code, repeats=5, exec_format=max):
    timer = timeit.Timer(setup=setup, stmt=code)
    loops = 0
    # If (one execution does not timeout) time the function else inf
    if within_project_euler_timelimit(timer.timeit, 1):
        # find the number of loops such that time < 0.2s
        loops = timer.autorange()[0]
        times = timer.repeat(repeats, number=loops)
        times = [time / loops for time in times]
    else:
        times = [float("Inf")] * repeats
    return exec_format(times)


if __name__ == "__main__":
    pass
