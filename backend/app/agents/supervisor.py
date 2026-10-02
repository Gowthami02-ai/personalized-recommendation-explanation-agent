from backend.app.agents.supervisor import SupervisorAgent


class Supervisor:
    def __init__(self):
        self.agent = SupervisorAgent()

    def run(self, state):
        return self.agent.handle(state)
