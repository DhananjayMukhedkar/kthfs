import scipy.io
from pykalman import KalmanFilter
import numpy

#Load data.mat
mat = scipy.io.loadmat('data.mat')
indata=mat['in_data']
#setup all data
val=indata[0,0]

gnss=val['GNSS']
imu=val['IMU']
speedometer=val['SPEEDOMETER']

#GNSS data
pos_ned=gnss['pos_ned'] # array N,E,D
hdop=gnss['HDOP']
vdop=gnss['VDOP']
gnssTime=gnss['t']
#IMU data
acc=imu['acc']
gyro=imu['gyro']
imuTime=imu['t']
#SPEEDOMETER DATA
speed=speedometer['speed']
speedometerTime=speedometer['t']




def kalmanLib():
    """
    Try KalmanFilter library
    :return:
    """
    transition_matrices=[],observation_matrices=[]
    kf = KalmanFilter(transition_matrices , observation_matrices )
    measurements = pos_ned #measurement array
    kf = kf.em(measurements, n_iter=5)
    (filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
    (smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)


class KalmanFromScratch():

    def __init__(self):
        self.A=[],self.B=[] ,self.C=[],self.R=[],self.Q=[]
        self.init_mean=[],self.initCov=[]


    def getKalmanGain(self,cov):
        """
        Calculate Kalman gain value based on current parameters
        :param cov:
        :return:
        """
        k_gain=[]
        return k_gain

    def getControlInput(self,i):
        """
        return the control input vector at time i from IMU/SPEEDOMETER data
        :return:
        """
        controlState=acc[i]

    def getCurrentMeasure(self,i):
        """
        get current measurement vector using GNSS
        :param i:
        :return:
        """
        z=pos_ned[i]
        return


    def publishKalman(self,posterior_mean,posterior_cov):
        """
        This method can be used to return or publish current Kalman mean and covariances
        :param posterior_mean:
        :param posterior_cov:
        :return:
        """
        return  posterior_mean,posterior_mean


    def kalmanUpdate(self):

        """
        loop over measurements and calculate next mean and covariances based on algorithm
        :return:
        """

        mean_candidate=[],cov_candidate=[]
        for i,t in enumerate(gnssTime):
            #predict
            mean_candidate=self.A.dot(self.init_mean)+self.B.dot(self.getControlInput(i))
            cov_candidate=self.A.dot(self.initCov).dot(self.A).transpose + self.R
            gain=self.getKalmanGain(cov_candidate)
            z=self.getCurrentMeasure(i)
            #update
            posterior_mean=mean_candidate+gain.dot(z-(self.C.dot(mean_candidate)))
            posterior_cov=(numpy.identity()-gain.self.C).cov_candidate

            self.publishKalman(posterior_mean,posterior_cov)
            #update last to last timestep
            self.initCov=posterior_cov
            self.init_mean=posterior_mean


















