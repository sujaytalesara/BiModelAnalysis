# ---- Imported Packages
import pandas as pd

# ---- Enter File name to be analysed
fileName1 = input("Enter the file path of Emergency Data : ")
fileName2 = input("Enter the file path of non Emergency Data : ")

#E:\A TCD\X Thesis\Data\Sujay Emotient Analysis\Emotient data\003_Emergency Kathleen Wynne.txt
#E:\A TCD\X Thesis\Data\Sujay Emotient Analysis\Emotient data\004_Non Emergency Kathleen Wynne.txt

    # ------ Load to data Frame
Emergency = pd.read_csv(fileName1, delimiter = '\t', header=4)
NonEmergency = pd.read_csv(fileName2, delimiter = '\t', header=4)
    # Formatting File and reading relevant content


Emergencydf = Emergency[['Joy Evidence', 'Anger Evidence', 'Surprise Evidence', 'Fear Evidence','Contempt Evidence',
                         'Disgust Evidence', 'Sadness Evidence']]
EmergencyAU = Emergency[
        ['AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence', 'AU6 Evidence', 'AU7 Evidence',
         'AU9 Evidence', 'AU10 Evidence', 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
         'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence', 'AU25 Evidence', 'AU26 Evidence',
         'AU28 Evidence', 'AU43 Evidence']]

nonEmergencydf = NonEmergency[
        ['Joy Evidence', 'Anger Evidence', 'Surprise Evidence', 'Fear Evidence', 'Contempt Evidence',
         'Disgust Evidence', 'Sadness Evidence']]
NonEmerencyAU = NonEmergency[
        ['AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence', 'AU6 Evidence', 'AU7 Evidence',
         'AU9 Evidence', 'AU10 Evidence', 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
         'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence', 'AU25 Evidence', 'AU26 Evidence',
         'AU28 Evidence', 'AU43 Evidence']]

    # Remove missing values
Emergencydf.dropna()
EmergencyAU.dropna()
nonEmergencydf.dropna()
NonEmerencyAU.dropna()

# ----------------Emergency ---------------------------------------------------
    #  ------------------Physical Parameters Evaluation ----------------------
Accept = []
SignalNoiceRatio = []
Uncertanity = []

Reject = Emergencydf[Emergencydf < -0.0000001].count()
Equiprobable = Emergencydf[(Emergencydf >= -0.0000001) & (Emergencydf <= 0.0000001)].count()
Accept1 = Emergencydf[(Emergencydf > 0.0000001) & (Emergencydf < 1)].count()
Accept10 = Emergencydf[(Emergencydf > 1) & (Emergencydf < 2)].count()
Accept100 = Emergencydf[(Emergencydf > 2) & (Emergencydf < 3)].count()
Accept1000 = (Emergencydf[(Emergencydf > 3)].count())
    # Statistics
SignalNoiceRatio.append(Reject / Emergencydf.count())
Uncertanity.append(Equiprobable / Emergencydf.count())
Accept.append((Accept1 + Accept10 + Accept100 + Accept1000) / Emergencydf.count())

# -----------Emergency Action Units Calculation --------------------------
AUSignalNoiceRatio = []
AUncertanity = []
AcceptAU = []

AUReject = EmergencyAU[EmergencyAU < -0.0000001].count()
AUEquiprobable = EmergencyAU[(EmergencyAU >= -0.0000001) & (EmergencyAU <= 0.0000001)].count()
AUAccept1 = EmergencyAU[(EmergencyAU > 0.0000001) & (EmergencyAU < 1)].count()
AUAccept10 = EmergencyAU[(EmergencyAU > 1) & (EmergencyAU < 2)].count()
AUAccept100 = EmergencyAU[(EmergencyAU > 2) & (EmergencyAU < 3)].count()
AUAccept1000 = (EmergencyAU[(EmergencyAU > 3)].count())
AngerE = AUAccept1[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
         + AUAccept10[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
         + AUAccept100[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
         + AUAccept1000[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']]
# Statistics
AUSignalNoiceRatio.append(AUReject / EmergencyAU.count())
AUncertanity.append(AUEquiprobable / EmergencyAU.count())
AcceptAU.append((AngerE / EmergencyAU[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']].count()))

# ------------------------Non Emergency ---------------------------------------
#  ------------------Non Emergency Physical Parameters Evaluation --------
nAccept = []
nSignalNoiceRatio = []
nUncertanity = []

nReject = nonEmergencydf[nonEmergencydf < -0.0000001].count()
nEquiprobable = nonEmergencydf[(nonEmergencydf >= -0.0000001) & (nonEmergencydf <= 0.0000001)].count()
nAccept1 = nonEmergencydf[(nonEmergencydf > 0.0000001) & (nonEmergencydf < 1)].count()
nAccept10 = nonEmergencydf[(nonEmergencydf > 1) & (nonEmergencydf < 2)].count()
nAccept100 = nonEmergencydf[(nonEmergencydf > 2) & (nonEmergencydf < 3)].count()
nAccept1000 = nonEmergencydf[(nonEmergencydf > 3)].count()
# Statistics
nSignalNoiceRatio.append(nReject / nonEmergencydf.count())
nUncertanity.append(nEquiprobable / nonEmergencydf.count())
nAccept.append((nAccept1 + nAccept10 + nAccept100 + nAccept1000) / nonEmergencydf.count())

# -----------Non Emergency Action Units Calculation ----------------------
AUnSignalNoiceRatio = []
AUnUncertanity = []
nAcceptAU = []

AUnReject = NonEmerencyAU[NonEmerencyAU < -0.0000001].count()
AUnEquiprobable = NonEmerencyAU[(NonEmerencyAU >= -0.0000001) & (NonEmerencyAU <= 0.0000001)].count()
AUnAccept1 = NonEmerencyAU[(NonEmerencyAU > 0.0000001) & (NonEmerencyAU < 1)].count()
AUnAccept10 = NonEmerencyAU[(NonEmerencyAU > 1) & (NonEmerencyAU < 2)].count()
AUnAccept100 = NonEmerencyAU[(NonEmerencyAU > 2) & (NonEmerencyAU < 3)].count()
AUnAccept1000 = (NonEmerencyAU[(NonEmerencyAU > 3)].count())
# Statistics
AUnSignalNoiceRatio.append(AUnReject / NonEmerencyAU.count())
AUnUncertanity.append(AUnEquiprobable / NonEmerencyAU.count())

AngerNE = AUnAccept1[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
          + AUnAccept10[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
          + AUnAccept100[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']] \
          + AUnAccept1000[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']]

nAcceptAU.append((AngerNE / NonEmerencyAU[['AU4 Evidence', 'AU5 Evidence', 'AU7 Evidence', 'AU23 Evidence']].count()))

# -- CHI Square Statistics -----------------------------------------------
import scipy.stats as stats
import numpy as np

chiStatisticsAccept = []
chiStatisticsEqui = []
chiStatisticsAU = []
RatioE_NE = []

#RatioE_NE.append((Accept/nAccept))

chiStatisticsAccept.append(stats.chisquare(np.transpose(Accept), np.transpose(nAccept)))
chiStatisticsEqui.append(stats.chisquare(np.transpose(SignalNoiceRatio), np.transpose(nSignalNoiceRatio)))
chiStatisticsAU.append(stats.chisquare(np.transpose(AcceptAU), np.transpose(nAcceptAU)))


print('-------------------------------------------------------------------------------------')
print('T test values for Acceptance ',chiStatisticsAccept)
print('-------------------------------------------------------------------------------------')
print('T test values for Equiprobable ',chiStatisticsEqui)
print('--------------------------------------------------------------------------------------')
print('T test values for Action Units ',chiStatisticsAU)
print('---------------------------------------------------------------------------------------')