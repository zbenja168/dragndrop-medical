#!/usr/bin/env python3
"""Add prev/next navigation buttons to new game files 109-114 and update file 108."""
import re

PREV_TPL = '<a href="{href}" style="position:fixed;top:12px;z-index:9999;background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:\'Segoe UI\',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;right:115px;" onmouseover="this.style.color=\'#fff\';this.style.borderColor=\'rgba(255,255,255,0.5)\';this.style.background=\'rgba(0,0,0,0.88)\'" onmouseout="this.style.color=\'#e2e8f0\';this.style.borderColor=\'rgba(255,255,255,0.22)\';this.style.background=\'rgba(0,0,0,0.72)\'">&#8592; Previous</a>'

NEXT_TPL = '<a href="{href}" style="position:fixed;top:12px;z-index:9999;background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;font-family:\'Segoe UI\',sans-serif;backdrop-filter:blur(10px);transition:.15s;display:inline-flex;align-items:center;gap:6px;right:12px;" onmouseover="this.style.color=\'#fff\';this.style.borderColor=\'rgba(255,255,255,0.5)\';this.style.background=\'rgba(0,0,0,0.88)\'" onmouseout="this.style.color=\'#e2e8f0\';this.style.borderColor=\'rgba(255,255,255,0.22)\';this.style.background=\'rgba(0,0,0,0.72)\'">Next &#8594;</a>'

# File sequence
files = [
    ("108_sinus_bradycardia_treatment.html", None, "109_antiarrhythmic_classes_II_III_IV.html"),  # add Next only (already has Prev)
    ("109_antiarrhythmic_classes_II_III_IV.html", "108_sinus_bradycardia_treatment.html", "110_miscellaneous_antiarrhythmics.html"),
    ("110_miscellaneous_antiarrhythmics.html", "109_antiarrhythmic_classes_II_III_IV.html", "111_afib_pathophysiology_risk_factors.html"),
    ("111_afib_pathophysiology_risk_factors.html", "110_miscellaneous_antiarrhythmics.html", "112_afib_treatment.html"),
    ("112_afib_treatment.html", "111_afib_pathophysiology_risk_factors.html", "113_supraventricular_arrhythmia_types.html"),
    ("113_supraventricular_arrhythmia_types.html", "112_afib_treatment.html", "114_svt_ecg_and_treatment.html"),
    ("114_svt_ecg_and_treatment.html", "113_supraventricular_arrhythmia_types.html", None),  # last file, no Next
]

import os
os.chdir("C:/dragndrop_claude")

for filename, prev_file, next_file in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Build nav buttons to insert
    nav_buttons = ""
    if prev_file:
        nav_buttons += "\n" + PREV_TPL.format(href=prev_file)
    if next_file:
        nav_buttons += "\n" + NEXT_TPL.format(href=next_file)

    if not nav_buttons:
        continue

    if filename == "108_sinus_bradycardia_treatment.html":
        # File 108 already has prev button, just need to add Next before the blank line after nav
        content = content.replace(
            "&#8592; Previous</a>\n",
            "&#8592; Previous</a>\n" + NEXT_TPL.format(href=next_file) + "\n"
        )
    else:
        # New files: insert nav buttons after the back/index button line
        idx = content.find("Index</a>")
        if idx != -1:
            end_of_line = content.find("\n", idx)
            if end_of_line != -1:
                content = content[:end_of_line] + nav_buttons + content[end_of_line:]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {filename} (prev={'yes' if prev_file else 'no'}, next={'yes' if next_file else 'no'})")

print("\nNav buttons added to all files.")
