class MotionPlanner:
    def __init__(self, robot, ps):
        self.robot = robot
        self.ps = ps

    def solveBiRRT(self, maxIter=float("inf")):
        print("Method solveBiRRT is not implemented yet")
        self.ps.prepareSolveStepByStep()
        finished = False

        # In the framework of the course,
        # we restrict ourselves to 2 connected components.
        nbCC = self.ps.numberConnectedComponents()
        if nbCC != 2:
            raise Exception("There should be 2 connected components.")

        iter = 0
        while True:
            # RRT begin
            newConfigs = list()

            # Try connecting the new nodes together
            for i in range(len(newConfigs)):
                pass
            # RRT end
            # Check if the problem is solved.
            nbCC = self.ps.numberConnectedComponents()
            if nbCC == 1:
                # Problem solved
                finished = True
                break
            iter = iter + 1
            if iter > maxIter:
                break
        if finished:
            self.ps.finishSolveStepByStep()
            return self.ps.numberPaths() - 1

    def solvePRM(self,maxIter):
        finished = False
        self.ps.prepareSolveStepByStep()
        # PRM begin
        while not finished :
            q_rand = self.robot.shootRandomConfig()
            res,msg = self.robot.isConfigValid(q_rand)
            if res :
                self.ps.addConfigToRoadmap(q_rand)
            else :
                continue
            configs_to_connect = list()
            n_cc = self.ps.numberConnectedComponents()
            for i in range (n_cc-1) :
                q,d = self.ps.getNearestConfig(q_rand,i)
                configs_to_connect.append(q)
            for q in configs_to_connect :
                res,p,msg = self.ps.directPath(q_rand,q,True)
                if res :
                    self.ps.addEdgeToRoadmap(q_rand,q,p,True)
            # Test whether initial and goal configs are in the same
            # connected component
            q_init = self.ps.getInitialConfig()
            q_goal = self.ps.getGoalConfigs()[0]
            for i in range(self.ps.numberConnectedComponents()):
                nodes = self.ps.nodesConnectedComponent(i)
                if q_init in nodes and q_goal in nodes:
                    finished = True
                    break

        # PRM end
        if finished:
            self.ps.finishSolveStepByStep()
        print("bonjour")
