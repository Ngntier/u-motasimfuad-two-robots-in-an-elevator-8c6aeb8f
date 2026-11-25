import os

LINE = "So\u2026 do you also pretend your firmware is updating when the doors close, or do you just stand here counting the silence like I do?"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
