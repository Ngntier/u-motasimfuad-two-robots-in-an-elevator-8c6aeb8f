import os

LINE = "So\u2026 do you also pretend your firmware is updating when the doors close, or do you just stand here counting the silence like I do?"

# The entry must be a single line of 1-200 characters (counted in UTF-8
# bytes so multi-byte characters like the ellipsis are charged fairly).
encoded = LINE.encode("utf-8")
if not 1 <= len(encoded) <= 200:
    raise ValueError(
        f"entry line must be 1-200 UTF-8 bytes, got {len(encoded)}"
    )
if "\n" in LINE or "\r" in LINE:
    raise ValueError("entry line must not contain a newline")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
