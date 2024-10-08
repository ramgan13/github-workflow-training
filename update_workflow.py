import csv
import yaml
from pprint import pprint

# Read the CSV file and extract the first column values
services = []
with open('services/service_names.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    for row in reader:
        services.append(row[0])

print(services)
print("-------------------")

# Load the existing workflow file
with open('.github/workflows/choices.yaml', 'r') as file:
    workflow = yaml.safe_load(file)


print(workflow)
print(type(workflow))
print("-------------------")

# Ensure 'on' is treated as a string
def preserve_strings(data):
    if isinstance(data, dict):
        print({k: preserve_strings(v) for k, v in data.items()})
        return {k: preserve_strings(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [preserve_strings(i) for i in data]
    elif isinstance(data, str) and data.lower() in ['on', 'off', 'yes', 'no', 'true', 'false']:
        return f'"{data}"'
    return data


workflow = preserve_strings(workflow)

print(workflow)
print(type(workflow))
print("-------------------")


# Update the service choices
#workflow[True]['workflow_dispatch']['inputs']['service']['options'] = services

#pprint(workflow)
#print(workflow)
#print(type(workflow))

# Save the updated workflow file
with open('.github/workflows/choices.yaml', 'w') as file:
    yaml.safe_dump(workflow, file)
    
with open('.github/workflows/choices.yaml', 'r') as file:
    workflow2 = yaml.safe_load(file)
    
print(workflow2)
print(type(workflow2))


print("Workflow file updated with service choices.")
