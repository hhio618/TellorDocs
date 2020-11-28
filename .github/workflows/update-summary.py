import os, sys, re
fname = 'SUMMARY.md'
os.rename(fname, fname + '.orig')
with open(fname + '.orig', 'r') as fin, open(fname, 'w') as fout, open("../telliot/docs/INDEX.md", "r") as fcontent:
    newContent = fcontent.read()
    data = fin.read()

    data = re.sub(r'(## Miner Documentation).*?(##)', 
      r'\1\n\n' +
      newContent + 
      r'\2\n\n##', data, flags=re.DOTALL)
    fout.write(data)
