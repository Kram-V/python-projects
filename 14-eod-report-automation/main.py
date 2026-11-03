import os
import subprocess
from datetime import datetime

# ---- Settings ----
REPO_PATH = r"C:\Users\kAriZmA\Desktop\nuxt-projects\flameguard-nuxt"
NAME = "Mark"
PROJECT = "Flameguard Website (Nuxt)"

# Save the report next to this script
REPORT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def run_git(args):
    """Run a git command in the project folder and return its output as text."""
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_PATH,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


# ---- 1. Get today's commits ----
commits_text = run_git(["log", "--all", "--since=1.week.ago", "--pretty=format:%s"])
commits = [line for line in commits_text.splitlines() if line.strip()]

# ---- 2. Count changed files and lines today ----
stats_text = run_git(["log", "--all", "--since=1.week.ago", "--shortstat", "--pretty=format:"])
files_changed = insertions = deletions = 0
for line in stats_text.splitlines():
    for part in line.split(","):
        part = part.strip()
        if "file" in part:
            files_changed += int(part.split()[0])
        elif "insertion" in part:
            insertions += int(part.split()[0])
        elif "deletion" in part:
            deletions += int(part.split()[0])

# ---- 3. Build the report ----
today = datetime.now()

lines = [
    "END OF DAY REPORT",
    "=" * 40,
    f"Name:    {NAME}",
    f"Date:    {today.strftime('%B %d, %Y (%A)')}",
    f"Project: {PROJECT}",
    "",
    "TASKS COMPLETED",
    "-" * 40,
]

if commits:
    for i, commit in enumerate(reversed(commits), start=1):  # oldest first
        lines.append(f"{i}. {commit}")
else:
    lines.append("No commits today.")

notes = input("Notes / blockers: ")
plan = input("Plan for tomorrow: ")

lines += [
    "",
    "SUMMARY",
    "-" * 40,
    f"Commits:       {len(commits)}",
    f"Files changed: {files_changed}",
    f"Lines added:   {insertions}",
    f"Lines removed: {deletions}",
    "",
    "NOTES / BLOCKERS",
    "-" * 40,
    f"- {notes}" if notes else "- None",
    "",
    "PLAN FOR TOMORROW",
    "-" * 40,
    f"- {plan}" if plan else "- ",
]

report = "\n".join(lines)

# ---- 4. Save to a .txt file ----
file_name = f"EOD-{today.strftime('%Y-%m-%d')}.txt"
file_path = os.path.join(REPORT_FOLDER, file_name)

with open(file_path, mode="w", encoding="utf-8") as file:
    file.write(report)

print(report)
print(f"\nSaved to {file_path}")