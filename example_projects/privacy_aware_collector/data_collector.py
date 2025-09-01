class DataCollector:
    def __init__(self):
        self.data = []

    def collect(self, user_input, consent):
        if consent:
            self.data.append(user_input)
            return f"Data collected: {user_input}"
        else:
            return "Consent not given. Data not collected."


if __name__ == "__main__":
    collector = DataCollector()
    print(collector.collect("User Location", consent=False))
    print(collector.collect("User Location", consent=True))
