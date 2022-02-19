#!/usr/bin/env python3

from pathlib import Path
import re

def main():
    p = Path("GFX_Fonts")
    for src in p.glob("*.h"):
        stem = Path(src).stem
        guard = stem.upper()
        with open(src) as f:
            content = f.read()
            content = re.sub(r'PROGMEM = ', r' = ', content)

            with open (f"Fonts/{src.name}", "wt") as dest:
                dest.write(f'#ifndef {guard}_H_\n')
                dest.write(f'#define {guard}_H_\n\n')
                dest.write('#include "stdint.h"\n')
                dest.write('#include "gfxfont.h"\n\n')
                dest.write(f'{content}\n')
                dest.write(f'#endif /* {guard}_H_ */\n')

if __name__ == "__main__":
    main()

"""
#ifndef FREESANS18PT7B_H_
#define FREESANS18PT7B_H_

#include "stdint.h"
#include "gfxfont.h"

...

#endif /* FREESANS18PT7B_H_ */



"""