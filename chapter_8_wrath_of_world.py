class EthicalAutopsy:
    def __init__(self, event, stakeholders, technical_cause, ethical_lapse):
        self.event = event
        self.stakeholders = stakeholders
        self.technical_cause = technical_cause
        self.ethical_lapse = ethical_lapse
        self.lessons = []

    def derive_lessons(self):
        # Fixed the line
        if "opacity" in self.technical_cause.lower():
            self.lessons.append("Ensure transparency in future system designs.")
        if "profit" in self.ethical_lapse.lower():
            self.lessons.append("Avoid prioritizing profit over safety.")
        if not self.lessons:
            self.lessons.append("Conduct broader ethical review before deployment.")
        return self.lessons

    def report(self):
        return {
            "Event": self.event,
            "Stakeholders": self.stakeholders,
            "Technical Cause": self.technical_cause,
            "Ethical Lapse": self.ethical_lapse,
            "Lessons": self.lessons
        }

# Example usage:
boeing_autopsy = EthicalAutopsy(
    event="737 MAX crashes",
    stakeholders=["Passengers", "Pilots", "Boeing", "Regulators"],
    technical_cause="MCAS reliance on single sensor; lack of pilot awareness",
    ethical_lapse="Profit-driven concealment of system complexity"
)

# Derive lessons first
boeing_autopsy.derive_lessons()

# Print the report
print(boeing_autopsy.report())
