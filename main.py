"""THE WORLD — Saturday, 21 November 2026: emit the front page.

The broadsheet for the day is already rendered and ships in this
repository as news.png. All this program does is place an exact copy
of that file at $MAKEFUN_OUTPUT_DIR/entry.png. Nothing is drawn,
fetched, re-encoded, or timed here: the bytes that go in are the
bytes that come out, so running it twice always produces the same
file.
"""

import hashlib
import os
import shutil
import sys


def _abort(reason):
    sys.stderr.write("entry failed: " + reason + "\n")
    raise SystemExit(1)


def _fingerprint(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(1 << 20)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    artwork = os.path.join(folder, "news.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        _abort("MAKEFUN_OUTPUT_DIR is not set")
    destination = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(artwork):
        _abort("news.png is missing next to main.py")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(artwork, destination)

    source_bytes = os.path.getsize(artwork)
    written_bytes = os.path.getsize(destination)
    if source_bytes != written_bytes:
        _abort(
            "size mismatch after copy: news.png is %d bytes but "
            "entry.png is %d bytes" % (source_bytes, written_bytes)
        )
    if _fingerprint(artwork) != _fingerprint(destination):
        _abort("sha256 mismatch after copy: entry.png differs from news.png")
    if written_bytes > 1048576:
        _abort(
            "entry.png is %d bytes, over the 1 MiB competition limit"
            % written_bytes
        )
    print(
        "wrote %s (%d bytes, sha256 verified)"
        % (destination, written_bytes)
    )


if __name__ == "__main__":
    main()
