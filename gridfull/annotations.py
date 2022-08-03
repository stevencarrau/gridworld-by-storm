from collections.abc import Iterable
from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    WEST = 3
    SOUTH = 4

    @property
    def rotation(self):
        if self == Direction.NORTH:
            return 0
        elif self == Direction.WEST:
            return 90
        elif self == Direction.SOUTH:
            return 180
        elif self == Direction.EAST:
            return 270

    def __str__(self):
        if self == Direction.NORTH:
            return "N"
        elif self == Direction.WEST:
            return "W"
        elif self == Direction.SOUTH:
            return "S"
        elif self == Direction.EAST:
            return "E"


class ProgramAnnotation:
    def __init__(self, constants):
        self._constants = constants
        self._ensure_list('adv-yvar-module')
        self._ensure_list('adv-xvar-module')
        self._ensure_list('adv-yvar-name')
        self._ensure_list('adv-xvar-name')

    def _ensure_list(self, entry):
        if entry in self._constants:
            if isinstance(self._constants[entry], str):
                self._constants[entry] = [self._constants[entry]]
            elif isinstance(self._constants[entry], Iterable):
                self._constants[entry] = list(self._constants[entry])
            else:
                self._constants[entry] = [self._constants[entry]]

    def _require(self, entry):
        if not entry in self._constants:
            raise RuntimeError(f"{entry} needs to be set, but has not been set")

    @property
    def nr_adversaries(self):
        if 'adv-xvar-module' in self._constants:
            return len(self._constants['adv-xvar-module'])
        else:
            return 0

    @property
    def has_landmarks(self):
        return 'landmarks' in self._constants

    @property
    def ego_xvar_identifier(self):
        self._require("ego-xvar-module")
        self._require("ego-xvar-name")
        return self._constants['ego-xvar-module'], self._constants['ego-xvar-name']

    @property
    def ego_yvar_identifier(self):
        self._require("ego-yvar-module")
        self._require("ego-yvar-name")
        return self._constants['ego-yvar-module'], self._constants['ego-yvar-name']

    def adv_xvar_identifier(self,index=0):
        if self.nr_adversaries == 0:
            raise RuntimeError("No adversary in this program.")
        self._require("adv-xvar-module")
        self._require("adv-xvar-name")
        return self._constants['adv-xvar-module'][index], self._constants['adv-xvar-name'][index]

    def adv_yvar_identifier(self,index=0):
        if self.nr_adversaries == 0:
            raise RuntimeError("No adversary in this program.")
        self._require("adv-yvar-module")
        self._require("adv-yvar-name")
        return self._constants['adv-yvar-module'][index], self._constants['adv-yvar-name'][index]

    def interactive_landmark_status_identifier(self, index=0):
        if self.nr_interactive_landmarks == 0:
            raise RuntimeError("No interactive landmarks in this program.")
        self._require("il-statusvar-module")
        self._require("il-statusvar-name")
        return self._constants['il-statusvar-module'][index], self._constants['il-statusvar-name'][index]

    def interactive_landmark_clearance_identifier(self, index=0):
        if self.nr_interactive_landmarks == 0:
            raise RuntimeError("No interactive landmarks in this program.")
        self._require("il-clearancevar-module")
        self._require("il-clearancevar-name")
        return self._constants['il-clearancevar-module'][index], self._constants['il-clearancevar-name'][index]

    @property
    def has_goal_action(self):
        if 'goal-action' in self._constants and self._constants['goal-action']:
            return True
        return False

    @property
    def adv_has_direction(self):
        return 'adv-dirvar-name' in self._constants

    def adv_dir_identifier(self,index=0):
        if self.nr_adversaries == 0:
            raise RuntimeError("No adversary in this program")
        if not self.adv_has_direction:
            raise RuntimeError("Adversaries have no direction")
        self._require("adv-dirvar-module")
        self._require("adv-dirvar-name")
        return self._constants['adv-dirvar-module'][index], self._constants['adv-dirvar-name'][index]

    @property
    def adv_radius_constant(self):
        if 'adv-radius-constant' in self._constants:
            return self._constants['adv-radius-constant']
        return None

    @property
    def ego_radius_constant(self):
        if 'ego-radius-constant' in self._constants:
            return self._constants['ego-radius-constant']
        return None

    @property
    def xmax_constant(self):
        self._require("xmax-constant")
        return self._constants["xmax-constant"]

    @property
    def ymax_constant(self):
        self._require("ymax-constant")
        return self._constants["ymax-constant"]

    @property
    def has_static_targets(self):
        return 'target-label' in self._constants

    @property
    def target_label(self):
        self._require("target-label")
        return self._constants["target-label"]

    @property
    def traps_label(self):
        self._require("traps-label")
        return self._constants["traps-label"]

    @property
    def scan_action(self):
        if 'scan-action' in self._constants:
            return self._constants["scan-action"]
        return None

    @property
    def adv_draw_area_boundaries(self):
        return 'adv-area' in self._constants

    def adv_area(self, adv_index=0):
        self._require('adv-area')
        camera_prefix = self._constants['adv-area'][adv_index]
        return [camera_prefix + suffix for suffix in ["XMIN", "YMIN", "XMAX", "YMAX"]]


    @property
    def landmark_label(self):
        self._require("landmarks")
        return self._constants['landmarks']

    @property
    def adv_goal_label(self):
        if "adv-goals-label" in self._constants:
            return self._constants['adv-goals-label']
        return None

    @property
    def has_resources(self):
        return "resource-name" in self._constants

    @property
    def resource_names(self):
        self._require("resource-name")
        return [self._constants['resource-name']]

    @property
    def max_resource_level_constants(self):
        self._require("resource-maximum-constant")
        return [self._constants["resource-maximum-constant"]]

    @property
    def resource_identifiers(self):
        self._require("resource-module")
        self._require("resource-variable")
        return [(self._constants['resource-module'], self._constants['resource-variable'])]

    def adversary_direction_value_to_direction(self, val):
        return self._constants['adv-dirvalue-mapping'][val]

    @property
    def nr_cameras(self):
        if 'camera' in self._constants:
            return len(self._constants['camera'])
        return 0

    def camera_constants(self, camera_index=0):
        camera_prefix = self._constants['camera'][camera_index]
        return [camera_prefix + suffix for suffix in ["XMIN", "YMIN", "XMAX", "YMAX"]]

    @property
    def nr_interactive_landmarks(self):
        if 'interactive-landmarks-x' in self._constants:
            return len(self._constants['interactive-landmarks-x'])
        return 0

    def interactive_landmark_constants(self, index=0):
        return self._constants['interactive-landmarks-x'][index], self._constants['interactive-landmarks-y'][index]

