import sys
import json

s = sys.stdin.read()
d = { 'text': s,
      'mode': 'gfm',
      'context': 'github/gollum'
    }
sys.stdout.write(json.dumps(d))
