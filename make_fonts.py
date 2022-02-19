#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess

sizes = [9, 12, 18, 24, 36, 48, 54, 56]
last = {7: 126, 8: 255}

def main():
    p = Path("TTF")
    for src in p.glob("*.ttf"):
        for s in sizes:
            for b in range(7,9):
                base = re.sub(r'[-_ ]', '', Path(src).stem)
                hfile = f"{base}{s}pt{b}b.h"
                guard = f"{base}{s}pt{b}b".upper()
                last_c = last[b]
                if (s >= 50):
                    last_c = min(last_c, 177)
                elif (s >= 40):
                    last_c = min(last_c, 191)
                content = subprocess.getoutput(f'./fontconvert {src} {s} 32 {last_c}')
                match = re.search(r"Approx. (\d+) bytes", content)
                if match:
                    mem_size = (int(match.group(1)))
                    if mem_size > 2**16 - 32:
                        print (f"Font {src} {s} 32 {last_c} too big ({mem_size})")
                        continue
                with open(f"Fonts/{hfile}", "wt") as dest:
                    dest.write(f'#ifndef {guard}_H_\n')
                    dest.write(f'#define {guard}_H_\n\n')
                    dest.write(f'{content}\n\n')
                    dest.write(f'#endif /* {guard}_H_ */\n')

if __name__ == "__main__":
    main()