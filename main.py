# news-image-20261124 entry (Python 3.13, standard library only).
# The image is the entry.png beside this file; the program copies it to
# /output/entry.png (or $MAKEFUN_OUTPUT_DIR outside the grader).
# It reads no network and writes the same bytes on every run, so the
# grader's two runs agree byte for byte.
import hashlib
import os
import shutil


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy is byte-identical, so the grader's two runs agree.
    src_hash = hashlib.sha256(open(src, "rb").read()).hexdigest()
    dst_hash = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    if src_hash != dst_hash:
        raise RuntimeError("entry.png copy failed verification")
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
