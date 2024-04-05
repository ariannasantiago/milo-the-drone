from .base import BaseRule
from constants import BACKOFF_DISTANCE, MINIMUM_DISTANCE

class BackoffRule(BaseRule):
    '''
    Rule to move back if the detection is too close
    NOTE: assumes that z-distance of detection can be found
    TODO: confirm that we can calculate the distance to detection, otherwise may need
          to reimplement 
    '''

    def isActive(self):
        return self.camera.closestDetection() != None and \
            self.camera.closestDetection().z < BACKOFF_DISTANCE

    def update(self):
        detection = self.camera.closestDetection()
        if detection == None:
            return

        xDistance = detection.x
        zDistance = detection.z
        #TODO ^ update this if we can't do the radius distance method

        self._targetPosition = (zDistance - MINIMUM_DISTANCE, xDistance)

    def name(self) -> str:
        return 'backoff'