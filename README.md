# Port-Scanner

Minimal Python port scanner (educational). Scans a small set of common ports on a target (localhost / VM).

## Features
- Single-threaded starter scanner
- Easy to extend (argparse, threading, logging)
- Designed for local/VM/lab use only

## Safety & Ethics (READ THIS)
**Do NOT** scan any systems or networks you do not own or have explicit permission to test. Unauthorized scanning may be illegal and can get you in trouble. Use this tool only on localhost, your VMs, or lab targets.

## Requirements
- Python 3.8+
- No external libraries required

## Usage
```bash
python simple_scanner.py
# or
python simple_scanner.py --target 127.0.0.1 --ports 22,80,443 --timeout 0.8
