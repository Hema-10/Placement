import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
t1.join()
t2.join()
