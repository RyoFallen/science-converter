# Project 2 — Collaborative Development & CI Pipeline Automation

**Application:** Science Converter (CLI tool for converting physical units — length, mass, temperature, fuel consumption)
**Repository:** https://github.com/RyoFallen/science-converter

## Team & Roles (two-account simulation)

| Role   | GitHub account     | Responsibilities                                              |
|--------|--------------------|--------------------------------------------------------------|
| Lead   | `RyoFallen`        | Initialized main repo & core app, code review, merge, CI      |
| Junior | `mustafacankatarr` | Forked repo, feature branch, new module, opened Pull Request  |

---

## 1. Collaborative Workflow

**Lead** initialized the main repository with the core application structure
(`src/converter.py`, `src/cli.py`, `tests/`) and the CI pipeline.

**Junior** forked the repository
(`mustafacankatarr/science-converter`), created a dedicated feature branch
`feature/fuel-consumption`, and added a new functional module:
a **fuel-consumption converter** (`src/fuel.py`) supporting `mpg ↔ L/100km`,
wired into the CLI, with 8 new tests (`tests/test_fuel.py`).

## 2. The "Gatekeeper" — Pull Request & Review

- **Pull Request #1:** https://github.com/RyoFallen/science-converter/pull/1
  (from `mustafacankatarr:feature/fuel-consumption` → `RyoFallen:main`)
- **Code review with inline line-comment** (Lead → Junior, on `src/fuel.py` line 18):
  https://github.com/RyoFallen/science-converter/pull/1#pullrequestreview-4587656920
  > *"Technical: the parentheses around `_KM_PER_MILE` are redundant here … consider documenting that this constant works symmetrically in both directions."*

### Merge conflict simulation
While the PR was open, the Lead changed the CLI `description` line on `main`.
The Junior had also changed that same line, so GitHub flagged the PR as
**CONFLICTING / DIRTY**. The Lead resolved the conflict locally (combining both
edits) and completed the merge:

```
Merge commit: "Merge fuel-consumption module from Junior (resolve CLI conflict)"
Merged by: RyoFallen
Status: MERGED
```

## 3. Continuous Integration (CI)

Workflow file: [`.github/workflows/main.yml`](.github/workflows/main.yml)

- Triggers on **every push** (and pull requests)
- Boots a **Linux runner** (`ubuntu-latest`)
- Installs dependencies and runs the automated test-suite with **pytest**

**Success (Green) run** — merge commit on `main`:
https://github.com/RyoFallen/science-converter/actions/runs/28325151361

## 4. Simulated Failure (CI turns Red)

A bug was intentionally introduced on branch `bug/simulated-failure`:
the Fahrenheit formula was changed from `celsius * 9 / 5 + 32` to `+ 23`.
On push, CI detected the broken logic and the pipeline turned **Red**:

```
tests/test_converter.py::TestTemperature::test_celsius_to_fahrenheit FAILED
    self.assertAlmostEqual(converter.convert_temperature(100, "C", "F"), 212.0)
    AssertionError: 203.0 != 212.0 within 7 places (9.0 difference)
========================= 1 failed, 21 passed in 0.05s =========================
```

**Failure (Red) run:**
https://github.com/RyoFallen/science-converter/actions/runs/28325173289

The CI system caught the regression automatically before it could reach `main`,
demonstrating the protective value of the pipeline.

---

## Screenshots to capture for the Moodle report

1. **PR Evidence** — the merged PR #1 page (shows `mustafacankatarr` → `RyoFallen` interaction)
2. **Code Review** — the inline line-comment on `src/fuel.py`
3. **CI Success (Green)** — the Actions run on `main`
4. **CI Failure (Red)** — the Actions run on `bug/simulated-failure`
5. **Repository link** — https://github.com/RyoFallen/science-converter
