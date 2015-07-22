in_code = False
code = []
with open('orb.lpy', 'r') as f:
    for line in f:
        if line.strip()[:3] == '```':
            # toggle between in and out of code
            in_code = not in_code
            # We don't want to insert the ``` into the file
            code.append('###' + line.lstrip()[3:])
            continue
        
        if in_code:
            code.append(line)
        else:
            code.append('## ' + line)

with open('orb.py', 'w') as f:
      f.write(''.join(code))
