import os
import logging

import gridstorm.trace as trace

logger = logging.getLogger(__name__)


class VideoRecorder:
    def __init__(self, renderer, only_keep_finishers):
        self._only_keep_finishers = only_keep_finishers
        self._paths = []
        self._path = None
        self._renderer = renderer

    def start_path(self):
        assert self._path is None
        self._path = trace.Trace()

    def end_path(self, finished):
        self._path.append_action(None)
        if not self._only_keep_finishers or finished:
            self._paths.append(self._path)
        self._path = None

    def record_state(self, state):
        self._path.append_state(state)

    def record_selected_action(self, action):
        self._path.append_action(action)

    def record_available_actions(self, actions):
        self._path.append_available_actions(actions)

    def record_allowed_actions(self, actions):
        self._path.append_considered_actions(actions)

    def trim_from_end(self, length):
        for path in self._paths:
            path.trim_from_end(length)

    def save(self, path, prefix, gif=False):
        for i, trace in enumerate(self._paths):
            suffix = "gif" if gif else "mp4"
            mp4file = os.path.join(path,f"{prefix}-{i}.{suffix}")
            logger.info(f"Rendering {mp4file}")
            self._renderer.record(mp4file, trace)