class Snapshot:
    def __init__(self, trace, index=0):
        self._index = index
        self._trace = trace

    def __next__(self):
        self._index += 1
        if self._index == len(self._trace):
            raise StopIteration()
        return self

    @property
    def state(self):
        return self._trace._states[self._index]

    @property
    def action(self):
        return self._trace._actions[self._index]

    @property
    def available_actions(self):
        return self._trace._available_actions[self._index]

    @property
    def considered_actions(self):
        return self._trace._considered_actions[self._index]


class Trace:
    def __init__(self):
        self._states = []
        self._actions = []
        self._available_actions = []
        self._considered_actions = []

    def append_state(self,state):
        self._states.append(state)

    def append_action(self, action):
        self._actions.append(action)

    def append_available_actions(self, available_actions):
        self._available_actions.append(available_actions)

    def append_considered_actions(self, considered_actions):
        self._considered_actions.append(considered_actions)

    def __len__(self):
        return len(self._states)

    def check_validity(self):
        if len(self._states) != len(self._actions):
            raise RuntimeError("Invalid path (nr actions and states do not match)")
        if len(self._actions) != len(self._available_actions):
            raise RuntimeError("Invalid path (nr actions and nr available action sets do not match)")

    def __iter__(self):
        return Snapshot(self)


class BeliefSnapshot(Snapshot):
    def __init__(self, trace, index=0):
        super().__init__(trace, index)

    @property
    def potential_states(self):
        return self._trace._potential_states[self._index]


class BeliefTrace(Trace):
    def __init__(self):
        super().__init__()
        self._potential_states = []

    def append_potential_states(self, states):
        self._potential_states.append(states)

    def __iter__(self):
        return BeliefSnapshot(self)






