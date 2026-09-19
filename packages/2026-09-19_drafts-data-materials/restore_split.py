"""Restore split ZIP archives next to their .part01 files, then verify SHA-256."""
from pathlib import Path
import hashlib,json
root=Path(__file__).parent
for record in json.loads((root/'manifest.json').read_text(encoding='utf-8')):
 if 'parts' not in record:continue
 target=root/record['archive']
 with target.open('wb') as out:
  for name in record['parts']:out.write((target.parent/name).read_bytes())
 assert hashlib.sha256(target.read_bytes()).hexdigest()==record['archive_sha256']
 print('Restored:',target.name)
