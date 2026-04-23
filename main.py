from js import document  # type: ignore
from pyscript import display  # type: ignore
import matplotlib.pyplot as plt

plt.clf()

class Attendance:
    def __init__(self):
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.absences = [0, 0, 0, 0, 0]
        self.day_chart = {
            "Monday": "Mon",
            "Tuesday": "Tue",
            "Wednesday": "Wed",
            "Thursday": "Thu",
            "Friday": "Fri",
        }

    def update_day(self, full_day: str, absences: int):
        short_day = self.day_chart.get(full_day.strip(), full_day.strip())

        if short_day not in self.days:
            self.days.append(short_day)
            self.absences.append(absences)
        else:
            index = self.days.index(short_day)
            self.absences[index] = absences

class Attendance_Check:
    def __init__(self):
        self.data = Attendance()
        
    def add_record(self, day: str, Absence: int):
        self.data.update_day(day, Absence)

    @property
    def days(self):
        return self.data.days

    @property
    def absences(self):
        return self.data.absences

tracker = Attendance_Check()

def _render_plot():
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.plot(tracker.days, tracker.absences, marker="o", color="#1f77b4", linewidth=2)
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.set_ylim(bottom=0)
    ax.grid(True, linestyle="-", alpha=0.35)
    fig.tight_layout()

    plot_el = document.getElementById("plot-area")
    plot_el.innerHTML = ""  # Clear current plots
    display(fig, target="plot-area")

def Chart_show(*args, **kwargs):
    # Accept *args because py-click calls without arguments
    day = document.getElementById("Day").value  # full day name (Monday...)
    raw = document.getElementById("Absence").value or "0"

    try:
        absence = int(raw)
        if absence < 0:
            absence = 0
    except Exception:
        absence = 0

    tracker.add_record(day, absence)

    # Update status
    document.getElementById("output").innerText = f"Saved: {day} → {absence} absences"
    _render_plot()

#With help from Aria AI: I could not figure this out miss 💔