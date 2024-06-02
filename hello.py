def hello_world():
    return "Hello World!"


def hello_world_n(N):
    greetings = ""
    for n in range(N):
        greetings += hello_world() + " "
    return greetings.rstrip()
