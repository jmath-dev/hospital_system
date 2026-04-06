import random
import time
import os
import sys

size1 = random.randint(1, 20)
size2 = random.randint(1, 20)
size3 = random.randint(1, 10)

# Initialize random queue sizes for normal and priority users
normal_queue1 = list(range(1, size1+1))
normal_queue2 = list(range(1, size2+1))
preferential_queue = list(range(1, size3+1))


# User selects priority or standard service
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
time.sleep(4)

# Map queues to machine numbers and initialize machine timers
queues_dict = {1: normal_queue1,
               2: normal_queue2,
               3: preferential_queue}
user_queue = queues_dict[queue]

machines_dict = {1: [1, 2, 3],
              2: [1, 2, 3],
              3: [4, 5]}
user_machine = machines_dict[queue]

time_dict = {1: 0,
             2: 0,
             3: 0,
             4: 0,
             5: 0}  

# Simulate ticket processing at each machine, handling potential bottlenecks
# (queues may wait if machines are busy, mimicking real-life service flow)
while user_queue != []:
    for machine in user_machine:
        if time_dict[machine] == 0:
            if user_queue:
                os.system("clear")
                ticket = user_queue.pop(0)
                show = f"Current ticket {ticket}. Machine {machine}"
                print(f"\n{'Please wait to be called and go to the machine.':^148}")
                print(f"{show:^148}")
                time_dict[machine] = random.randint(7, 16)
        else:
            time.sleep(0.2)
            time_dict[machine] -= 1

os.system("clear")


# Patient registration and age/allergy checks
print("Welcome to AutoPharma!\n\nPlease, follow the instructions.")

name = input("\nWhat is your name? ").strip().title()

age = int(input("\nHow old are you? "))
if age < 18:
    print(f"{name}, please ask a staff member for assistance.\n")
    sys.exit()
else:
    print(f"Thank you, {name}. Let's continue.\n")

allergy = input("\n\nDo you have any allergies to medications? (yes/no) ").strip().lower()
if allergy == "yes":
    print("For safety, please consult a pharmacist.\n")
    sys.exit()
elif allergy == "no":
    time.sleep(1)
    os.system("clear")
    print("No allergies noted. Proceeding to symptom check.\n")
else:
    print("Invalid response")
    sys.exit()

# Dictionary of symptoms and corresponding treatments
symptoms = {1: "Headache",
            2: "Fever",
            3: "Cough",
            4: "Sore throat",
            5: "Runny nose",
            6: "Stomach ache",
            7: "Rash",
            8: "Fatigue",
            9: "Nausea",
            10: "Diarrhea",
            11: "Muscle pain",
            12: "Dizziness"}

print("\nPlease review and enter the number corresponding to your main symptom below:\n")
for i in symptoms:  
    print(f"{i}. {symptoms[i]}")
evaluation = int(input("\nEnter here: "))
if evaluation<1 or evaluation>12:
    print("Invalid response")
    sys.exit()

treatment = {"Headache": "Paracetamol or Ibuprofen.",
            "Fever": "Paracetamol or Ibuprofen.",
            "Cough": "Cough syrup (type depends on cough).",
            "Sore throat": "Lozenges or throat spray.",
            "Runny nose": "Antihistamine or decongestant.",
            "Stomach ache": "Antacid or light pain relief.",
            "Rash": "Calming cream (if mild) or consult a doctor.",
            "Fatigue": "Rest, hydration, nutrition.",
            "Nausea": "Mild antiemetic or ginger tea.",
            "Diarrhea": "Oral rehydration or mild control medicine.",
            "Muscle pain": "Topical or oral analgesic, gentle stretching.",
            "Dizziness": "Hydration and rest, consult a doctor if persistent."}


# Show suggested treatment based on symptom
print("Please wait while the system evaluates your symptoms...\n")
print("For symptoms that may be severe or need evaluation (Rash, Dizziness, intense Fatigue), please consult a doctor.")
time.sleep(3)
os.system("clear")
name_symptom = symptoms[evaluation]
name_treatment = treatment[name_symptom]
print(f"\nThe suggested treatment for your symptom is: {name_treatment}")

print(f"\n\n{'Thank you for using AutoPharma! We wish you a speedy recovery.':^150}")

