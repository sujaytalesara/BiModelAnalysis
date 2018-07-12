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
Emergencydf = Emergency[['Joy Evidence', 'Anger Evidence', 'Surprise Evidence', 'Fear Evidence',
                             'Contempt Evidence', 'Disgust Evidence', 'Sadness Evidence']][Emergency['PostMarker'] == 'NaN']
EmergencyAU = Emergency[
        ['AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence', 'AU6 Evidence', 'AU7 Evidence',
         'AU9 Evidence', 'AU10 Evidence', 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
         'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence', 'AU25 Evidence', 'AU26 Evidence',
         'AU28 Evidence', 'AU43 Evidence']][Emergency['PostMarker'] == 'NaN']

nonEmergencydf = NonEmergency[
        ['Joy Evidence', 'Anger Evidence', 'Surprise Evidence', 'Fear Evidence', 'Contempt Evidence',
         'Disgust Evidence', 'Sadness Evidence']][NonEmergency['PostMarker'] == 'NaN']
NonEmerencyAU = NonEmergency[
        ['AU1 Evidence', 'AU2 Evidence', 'AU4 Evidence', 'AU5 Evidence', 'AU6 Evidence', 'AU7 Evidence',
         'AU9 Evidence', 'AU10 Evidence', 'AU12 Evidence', 'AU14 Evidence', 'AU15 Evidence', 'AU17 Evidence',
         'AU18 Evidence', 'AU20 Evidence', 'AU23 Evidence', 'AU24 Evidence', 'AU25 Evidence', 'AU26 Evidence',
         'AU28 Evidence', 'AU43 Evidence']][NonEmergency['PostMarker'] == 'NaN']

    # Remove missing values
Emergencydf.dropna()
EmergencyAU.dropna()
nonEmergencydf.dropna()
NonEmerencyAU.dropna()