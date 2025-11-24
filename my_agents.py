# app.py

import sys
from pathlib import Path

from agents.analyst import run as run_analyst
from agents.tester import run as run_tester
from agents.coder import run as run_coder
from agents.reviewer import run as run_reviewer


# Active spec file (chosen by user)
ACTIVE_SPEC = None


def choose_spec():
    """Let the user pick a specification file."""
    global ACTIVE_SPEC

    specs = sorted(Path("specs").glob("*.md"))

    if not specs:
        print("\nNo specifications found in specs/ directory.\n")
        return

    print("\nAvailable specifications:\n")
    for i, spec in enumerate(specs, start=1):
        print(f"{i}) {spec.name}")

    choice = input("\nSelect a spec number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(specs)):
        print("Invalid choice.")
        return

    ACTIVE_SPEC = specs[int(choice) - 1].name
    print(f"\nActive specification set to: {ACTIVE_SPEC}\n")

def menu():
    print("==============================================")
    print("  AI Multi-Agent Development Application")
    print("==============================================")
    print(f"Active Spec: {ACTIVE_SPEC if ACTIVE_SPEC else 'None selected'}")
    print("----------------------------------------------")
    print("1) Choose active specification")
    print("2) Generate or update a specification (Analyst)")
    print("3) Generate or replace tests (Developer Tests)")
    print("4) Implement or update code (Developer Code)")
    print("5) Review implementation and tests (Reviewer)")
    print("6) Exit")
    print("----------------------------------------------")

    return input("Choose an option (1-6): ").strip()

def main():
    global ACTIVE_SPEC

    while True:
        choice = menu()

        if choice == "1":
            choose_spec()

        elif choice == "2":
            task = input("\nEnter specification task:\n> ")
            run_analyst(task)
            print("\nSpecification generated. Now choose it in step (2).\n")

            ACTIVE_SPEC = None

        elif choice == "3":
            if not ACTIVE_SPEC:
                print("\nYou must select a spec first!\n")
                continue

            feature = (
                ACTIVE_SPEC.replace("ft-", "")
                .replace(".md", "")
                .replace("-", "_")
            )

            task = f"""
        Generate pytest tests for the specification in specs/{ACTIVE_SPEC}.
        Treat this as feature '{feature}'.

        Place ALL tests under:
            tests/{feature}/

        Create ONE test file per acceptance criterion:
            ac_<NN>_<short_slug>_test.py

        Overwrite existing test files if necessary.
        """

            run_tester(task)
        elif choice == "4":
            if not ACTIVE_SPEC:
                print("\nYou must select a spec first!\n")
                continue

            feature = (
                ACTIVE_SPEC.replace("ft-", "")
                .replace(".md", "")
                .replace("-", "_")
            )

            test_folder = f"tests/{feature}"

            task = f"""
        Implement or update Python code for specs/{ACTIVE_SPEC}.

        Read ALL tests in:
            {test_folder}

        Ensure ALL tests pass.
        Modify only code under src/.
        """

            run_coder(task)

        elif choice == "5":
            if not ACTIVE_SPEC:
                print("\nYou must select a spec first!\n")
                continue

            feature = (
                ACTIVE_SPEC.replace("ft-", "")
                .replace(".md", "")
                .replace("-", "_")
            )

            task = f"""
            Review code and tests for spec: specs/{ACTIVE_SPEC}

            Read:
                - specs/{ACTIVE_SPEC}
                - ALL tests in tests/{feature}/
                - ALL relevant code in src/

            Produce a Markdown review report under reviews/.
            Do NOT modify code or tests.
            """

            run_reviewer(task)

        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()