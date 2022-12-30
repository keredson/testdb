



import os
import json
import subprocess



for fn in os.listdir('.'):
  if not fn.endswith('.json'): continue
  with open(fn,'r') as f:
    doc = json.load(f)
  resourceType = doc.get('resourceType', 'unknown')
  id = doc.get('id')
  if not os.path.isdir(resourceType):
    os.mkdir(resourceType)
  if resourceType and id:
    nfn = os.path.join(resourceType, f'{resourceType}-{id}.json')
  else:
    nfn = os.path.join(resourceType, fn)
  cmd = ['git','mv',fn,nfn]
  print(' '.join(cmd))
  subprocess.call(cmd) 
      

