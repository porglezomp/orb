import subprocess

in_code = False
code = []
with open('orb.lpy', 'r') as f:
    for line in f:
        if line.strip()[:3] == '```':
            # Toggle between in and out of code
            in_code = not in_code
            continue
        
        if in_code:
            code.append(line)

with open('orb.py', 'w') as f:
      f.write(''.join(code))

subprocess.Popen(['python', 'orb.py', 'compile', 'orb.lpy']).wait()
