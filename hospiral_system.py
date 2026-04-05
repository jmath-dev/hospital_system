import random
import time

size1 = random.randint(1, 40)
size2 = random.randint(1, 40)
size3 = random.randint(1, 20)


normal_queue1 = list(range(1, size1+1))
normal_queue2 = list(range(1, size2+1))
preferential_queue = list(range(1, size3+1))

while True:
    priority_level = int(input("\n Welcome.\n For priority service, press 1.\n For standard service, press 2.\n  : "))

    if priority_level == 1:
        queue = 3
        new_user = max(preferential_queue)
        preferential_queue.append(new_user+1)
        print(f"\nPriority service.\nYour ticket is {new_user+1}. Please wait to be called.\n")
        break

    elif priority_level == 2:
        queue = random.randint(1, 2)
        if queue == 1:
            new_user = max(normal_queue1)
            normal_queue1.append(new_user+1)
            print(f"\nStandard service.\nYour ticket is {new_user+1}. Please wait to be called.\n")
            break

        else:
            new_user = max(normal_queue2)
            normal_queue2.append(new_user+1)
            print(f"\nStandard service.\nYour ticket is {new_user+1}. Please wait to be called.\n")
            break

    else:
        print("Incorrect key")

queues_dict = {1: normal_queue1,
               2: normal_queue2,
               3: preferential_queue}


def attend_patient(queue):
    user_queue = queues_dict[queue]
    while user_queue != []:
        segundo = random.uniform(0.01, 6)
        time.sleep(segundo)
        print(f"Ticket {user_queue.pop(0)}")

room_dict = {1: [1, 2],
             2: [1, 2],
             3: [3, 4]}





attend_patient(queue)