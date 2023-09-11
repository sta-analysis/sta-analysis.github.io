import datetime
import json
from pathlib import Path


def nth_tuesday(year, month, n=3):
    date = datetime.datetime(year, month, 1)
    offset = (1 - date.weekday()) % 7 + 7 * (n - 1)  # 'weekday = 1' means tuesday
    return date + datetime.timedelta(offset)


def increment_semester_name(semester_name):
    season, year = semester_name.split(" ")
    if season == "Spring":
        return f"Fall {year}"
    else:
        return f"Spring {int(year)+1}"


def get_updated_archive():
    prev_semester = json.loads(Path("data/seminars.json").read_text())
    archive = json.loads(Path("data/archive.json").read_text())
    next_semester_name = increment_semester_name(next(iter(archive.keys())))

    return next_semester_name, {
        next_semester_name: prev_semester,
        **archive,
    }


def make_seminar_insert(date):
    return (
        date.strftime("%Y-%m-%d"),
        {k: "TBA" for k in ("name", "title", "abstract")},
    )


def generate_new_semester(next_semester_name):
    season, year_str = next_semester_name.split(" ")
    if season == "Spring":
        month = 9
        year = int(year_str)
    else:
        month = 1
        year = int(year_str) + 1

    first_seminar_date = nth_tuesday(year, month)
    return dict(
        make_seminar_insert(first_seminar_date + datetime.timedelta(7 * n))
        for n in range(12)
    )


if __name__ == "__main__":
    next_semester_name, archive = get_updated_archive()

    # take the previous semester and add to the archive
    Path("data/archive.json").write_text(json.dumps(archive, indent=2))
    print("Copied previous semester to `data/archive.json`.")

    # generate some placeholders for the current semester
    Path("data/seminars.json").write_text(
        json.dumps(generate_new_semester(next_semester_name), indent=2)
    )
    print("Generate new semester placeholders in `data/seminars.json`.")

    # update the semester date on the seminar page
    seminar_summary_path = Path("content/seminars/_index.md")
    seminar_summary_path.write_text(
        "\n".join(seminar_summary_path.read_text().strip().split("\n")[:-1])
        + f"\n### {increment_semester_name(next_semester_name)}"
    )
    print("Update seminar title in `content/seminars/_index.md`.")
