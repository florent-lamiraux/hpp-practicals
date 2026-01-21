from hpp.corbaserver.manipulation import Client, ProblemSolver
from hpp.gepetto import PathPlayer  # noqa: F401
from hpp.gepetto.manipulation import ViewerFactory

from hpp.corbaserver import loadServerPlugin
from hpp.corbaserver.manipulation.robot import Robot as Parent

loadServerPlugin("corbaserver", "manipulation-corba.so")
Client().problem.resetProblem()

class Robot(Parent):
    packageName = "hpp_practicals"
    urdfName = "ur5_gripper"
    urdfSuffix = ""
    srdfSuffix = ""

    def __init__(self, compositeName, robotName, load=True, rootJointType="anchor"):
        Parent.__init__(self, compositeName, robotName, rootJointType, load)
        self.rightWrist = "wrist_3_joint"
        self.leftWrist = "wrist_3_joint"
        self.endEffector = "ee_fixed_joint"

    def getInitialConfig(self):
        q = 6 * [0]
        return q

class Pokeball:
    rootJointType = "freeflyer"
    packageName = "hpp_practicals"
    meshPackageName = "hpp_practicals"
    urdfName = "ur_benchmark/pokeball"
    urdfSuffix = ""
    srdfSuffix = ""


class Ground:
    rootJointType = "anchor"
    packageName = "hpp_practicals"
    urdfName = "ur_benchmark/ground"
    meshPackageName = "hpp_practicals"
    urdfSuffix = ""
    srdfSuffix = ""


class Box:
    rootJointType = "anchor"
    packageName = "hpp_practicals"
    urdfName = "ur_benchmark/box"
    meshPackageName = "hpp_practicals"
    urdfSuffix = ""
    srdfSuffix = ""


robot = Robot("ur5-pokeball", "ur5")
ps = ProblemSolver(robot)
ps.setErrorThreshold(1e-4)
ps.setMaxIterProjection(40)

vf = ViewerFactory(ps)
gripperName = "ur5/wrist_3_joint"
ballName = "pokeball/root_joint"
