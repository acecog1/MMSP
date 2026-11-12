#!/usr/bin/env python3
"""Dependency/status validator for MMSP WBS. Does not auto-approve work."""
import csv
from pathlib import Path

path=Path(__file__).resolve().parents[1]/"models/mmsp-wbs-v0.1.csv"
rows=list(csv.DictReader(path.open(encoding="utf-8",newline="")))
ids={r["wbs_id"] for r in rows}
allowed={"blocked","ready","in_progress","in_review","done"}
errors=[]
for r in rows:
    k=r["wbs_id"]
    if r["status"] not in allowed: errors.append(f"{k}: invalid state")
    for dep in filter(None, r["dependencies"].split(";")):
        if dep not in ids: errors.append(f"{k}: missing predecessor {dep}")
        if dep==k: errors.append(f"{k}: self dependency")
byid={r["wbs_id"]:r for r in rows}
for r in rows:
    if r["status"]=="ready":
        for dep in filter(None,r["dependencies"].split(";")):
            if dep in byid and byid[dep]["status"]!="done":
                errors.append(f'{r["wbs_id"]}: premature ready; dependency {dep} not done')
seen=set()
def visit(k,stack):
    if k in stack: errors.append(f"cycle: {'->'.join(stack+[k])}");return
    if k in seen:return
    for d in filter(None,byid[k]["dependencies"].split(";")):
        if d in byid:visit(d,stack+[k])
    seen.add(k)
for k in ids:visit(k,[])
if errors:
    print("\n".join(errors));raise SystemExit(1)
print(f"WBS PASS: {len(rows)} tasks, dependencies and states valid")
print("States:",{s:sum(r["status"]==s for r in rows) for s in sorted(allowed)})
