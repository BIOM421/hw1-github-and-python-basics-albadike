def hello_world():
    return "Hello World!"


def hello_world_n(N):
    greetings = ""
    # for n in range(N):
    #     greetings += hello_world() + " "
    # greetings = " ".join([hello_world() for _ in range(N)])
    
    greetings = (hello_world() + " " ) * N
    return greetings.rstrip()
