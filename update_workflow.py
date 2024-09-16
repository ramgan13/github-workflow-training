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

# Load the existing workflow file
with open('.github/workflows/choices.yaml', 'r') as file:
    workflow = yaml.safe_load(file)

pprint(workflow)
print(workflow)

# Update the service choices
workflow['on']['workflow_dispatch']['inputs']['service']['options'] = services

pprint(workflow)
print(workflow)

# Save the updated workflow file
with open('.github/workflows/choices.yaml', 'w') as file:
    yaml.safe_dump(workflow, file)

print("Workflow file updated with service choices.")
