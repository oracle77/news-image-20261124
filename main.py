# news-image-20261124 entry (Python 3.13, standard library only).
# The image is the entry.png beside this file; the program copies it to
# /output/entry.png (or $MAKEFUN_OUTPUT_DIR outside the grader).
# It reads no network and writes the same bytes on every run, so the
# grader's two runs agree byte for byte.
import os
import shutil


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
