"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""

from Logic.LaserJobs_Book import LaserJobs_Book
from Data.Excel_Utilities.ExcelUtils import loadJobsFromExcel
from Data.Excel_Utilities.ExcelUtils import updateExcel
from Logic.DesignPatterns.ObserverPattern import Publisher


class LogicController(Publisher):

    def __init__(self, laserJobsPath, laserJobsFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.laserJobsPath = laserJobsPath
        self.laserJobsFileName = laserJobsFileName

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)

    def getGuiController(self):
        return self.guiController

    def loadJobsFromExcel(self):
        loadJobsFromExcel(self.laserJobsBook, self.laserJobsPath, self.laserJobsFileName)
        self.notify(self.laserJobsBook)

    def updateExcel(self, updatedJobData):
        updateExcel(updatedJobData, self.laserJobsPath, self.laserJobsFileName)

    def newJob(self,newJobData):
        try:
            self.laserJobsBook.newJob(newJobData)
            self.updateExcel(newJobData)
            self.notify(self.laserJobsBook)
        except Exception as inst:
            raise(inst)

    def getJob(self, jobId):
        # TODO implement getJob
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        # TODO implement updateJob
        self.laserJobsBook.updateJob(updatedJobData)

    def deleteJob(self,jobId):
        #TODO implement deleteJob
        self.laserJobsBook.deleteJob(jobId)

    def start(self):
        self.guiController.start()