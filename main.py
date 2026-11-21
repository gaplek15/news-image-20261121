"""THE WORLD — Saturday, 21 November 2026.

One broadsheet page that sums up the day's world news, built as a
single HTML front page and rendered once to news.png. The lead is the
war crossing a border: Russian missiles landing in Poland during the
biggest strike on Ukraine in months, with NATO's chief due in Warsaw
the same day. Around it, the EU's fresh billion euros for Ukraine's
arsenal, a tanker burning in the Strait of Hormuz, and Ebola's toll
on children in Congo. In brief: Denmark expelling a Russian attache
after a foiled murder plot, a 19-and-a-half-year sentence in the
Pannun murder-for-hire case, a Houthi strike on Riyadh's PIF Tower,
a fired US cyber chief, a subpoena for Nvidia over China chip sales,
and Virginia's first measles death of 2026.

This program only delivers that finished page to the harness. It
reads nothing but the bundled image, writes nothing but the entry,
and never touches the network, the clock, or a random number — run
it twice and both outputs are the same bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = "news.png"
ENTRY = "entry.png"


def bundled_page() -> Path:
    """The finished front page, sitting next to this file."""
    return Path(__file__).resolve().parent / SOURCE


def deliver() -> None:
    """Copy the front page into the harness output folder, unchanged."""
    out = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out.mkdir(parents=True, exist_ok=True)
    source = bundled_page()
    target = out / ENTRY
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("entry.png does not match news.png")


if __name__ == "__main__":
    deliver()
