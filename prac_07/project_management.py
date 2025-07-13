"""
CP1404/CP5632 Practical
project_management.py
Read and manage a list of software projects.
"""

from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Complete projects:")
    for project in sorted(complete):
        print(f"  {project}")


def main():
    """Main entry point of the project management program."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print("Projects loaded.\n")
    display_projects(projects)


if __name__ == '__main__':
    main()
