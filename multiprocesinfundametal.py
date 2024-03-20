import multiprocessing
import time


def cpu_bound_task(n):
    result = 0
    for _ in range(n):
        result += sum([i * i for i in range(10000)])
    return result

if __name__ == "__main__":
   
    num_tasks = 4

   
    start_time = time.time()

  
    processes = []
    for _ in range(num_tasks):
        process = multiprocessing.Process(target=cpu_bound_task, args=(100,))
        process.start()
        processes.append(process)

  
    for process in processes:
        process.join()

 
    end_time = time.time()

    
    execution_time = end_time - start_time
    print("Total execution time using multiprocessing:", execution_time)
