import os

all = os.listdir()
files = [f for f in all if os.path.isfile(f)]
jars = [f for f in files if f.endswith('.jar')]

with open('jars.txt', 'w') as f:
    for jar in jars:
        f.write(jar + '\n')

print(f"Found {len(jars)} .jar files. List written to jars.txt")