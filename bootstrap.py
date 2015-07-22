in_code = False
code = []
with open('orb.lpy', 'r') as f:
    for line in f:
        if line.strip()[:3] == '```':
            # toggle between in and out of code
            in_code = not in_code
            if line.lstrip()[3:].isspace():
                code.append('# ###\n')
            else:
                code.append('# ### ' + line.lstrip()[3:])
            continue
        
        if in_code:
            code.append(line.rstrip() + '\n')
        else:
            if line.isspace():
                code.append('#\n')
            else:
                code.append('# ' + line)

with open('orb.py', 'w') as f:
      f.write(''.join(code))
