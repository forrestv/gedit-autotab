def ignore_indent(line):
    return line.strip() == ''

def length(s):
    return len(s.replace('\t', ' '*8))

def split(x):
    assert x
    res = []
    for c in x:
        if c == '\t':
            res.append('\t')
        else:
            assert c == ' '
            if res and res[-1] != '\t':
                res[-1] += c
            else:
                res.append(c)
    return res

def determine(contents):
    counts = {}
    indents = []
    
    # parse lines, removing trailing whitespace and converting tabs
    for line in contents.splitlines(True):
        indentation = ''
        for char in line:
            if char not in [' ', '\t']:
                break
            indentation += char
        
        if not ignore_indent(line):
            while not indentation.startswith(''.join(indents)):
                indents.pop()
            if indentation != ''.join(indents):
                indents.extend(split(indentation[len(''.join(indents)):]))
            assert ''.join(indents) == indentation
            
            for y in indents:
                counts[y] = counts.get(y, 0) + 1
        #print indents
    
    print counts
    
    if not counts: return None
    best = max(sorted(counts), key=counts.get)
    if best == '\t':
        return 'tabs'
    else:
        return len(best)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rb') as f:
        print determine(f.read())
