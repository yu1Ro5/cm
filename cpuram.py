import psutil

def most_intensive_process():
    return max(psutil.process_iter(), key=lambda x: x.cpu_percent(0))

def most_RAM_usage():
    return max(psutil.process_iter(), key=lambda x: x.memory_info()[0])

x = most_intensive_process()
y = most_RAM_usage()

print(x.name)
print(y.name)