# quiet-dread entry — final version
# A tired engineer approves the PR, knowing exactly whose pager will go off.
import os

ENTRY = "Approved. The tests pass and the rollback is documented, so when this wakes someone at 3 AM it will at least be me, not you."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
