# Waveform-Comparator v1.0.0 | MIT License | https://github.com/yuukuru0511/Waveform-Comparator/blob/main/LICENSE

import time
from enum import Enum
import numpy as np
import librosa
import matplotlib.pyplot as plt

DEFAULT_SR = 44100

class Feature_Types(Enum):
    SPECTRUM = 1
    SPECTRUM_CENTROID = 2
    MFCC = 3

print("#0 [Settings]")

path_list = list()

is_continue_input = True
while is_continue_input:
    entered_path = input("Enter the path to the Wav file. \n(Entering a space will terminate your input.): ")
    if entered_path == "":
        if len(path_list) < 2:
            print("Please enter at least two.")
        else:
            print("OK.\n")
            is_continue_input = False
    else:
        path_list.append(entered_path)

is_correct_input = False
while not is_correct_input:
    entered_type_num = input("Select the feature type:\n[SPECTRUM: 1, SPECTRUM_CENTROID: 2, MFCC: 3]: ")
    if entered_type_num == "":
        print("Please be sure to enter the information.")
    if entered_type_num == "1" or entered_type_num == "2" or entered_type_num == "3":
        is_correct_input = True
    else:
        print("Please enter the information in the specified format.")

if entered_type_num == "1":
    feature_type = Feature_Types.SPECTRUM
elif entered_type_num == "2":
    feature_type = Feature_Types.SPECTRUM_CENTROID
elif entered_type_num == "3":
    feature_type = Feature_Types.MFCC

print("OK.\n")

is_correct_index = False
while not is_correct_index:
    print("Select a Wav file as the basis for comparison.")
    print("> | {} : {}".format("Index", "Path"))
    for index in range(len(path_list)):
        print("> | {} : {}".format(index + 1, path_list[index]))
    try:
        entered_index_num = int(input("Select an index from the list above: "))
    except:
        print("Please enter a number.")
    if not (entered_index_num >= 1 and len(path_list)):
        print("Enter within the index range of the listing.")
    else:
        reference_index = entered_index_num - 1
        print("OK.")
        is_correct_index = True

start = time.time()

print("#1 [Wav files read]")

y_and_sr_list = []
for path in path_list:
    y, sr = librosa.load(path, sr=DEFAULT_SR)
    y_and_sr_list.append((y, sr))

print("> | {} : {}".format("Index", "Path"))
for index in range(len(path_list)):
    print("> | {} : {}".format(index + 1, path_list[index]))

print("")

print("#2 [Feature extraction]")

print("> Selected feature type : {}".format(feature_type.name))

feature_list = []
for y_and_sr in y_and_sr_list:
    y = y_and_sr[0]
    sr = y_and_sr[1]
    if feature_type == Feature_Types.SPECTRUM:
        feature = np.abs(librosa.stft(y=y))
    elif feature_type == Feature_Types.SPECTRUM_CENTROID:
        feature = librosa.feature.spectral_centroid(y=y, sr=sr)
    elif feature_type == Feature_Types.MFCC:
        feature = librosa.feature.mfcc(y=y, sr=sr)
    feature_list.append(feature)

print("")

print("#3 [Evaluation]")

reference_feature = feature_list[reference_index]
print("> Reference : {} ({})".format(reference_index + 1, path_list[reference_index]))

eval_list = []
for target_feature in feature_list:
    ac, wp = librosa.sequence.dtw(reference_feature, target_feature)
    eval = 1 - (ac[-1][-1] / np.array(ac).max())
    eval_list.append(eval)

print("> | {} , {} : {}".format("Reference", "Target", "Score"))
for target_index in range(len(eval_list)):
    eval = eval_list[target_index]
    print("> | {} , {} : {}".format(reference_index + 1, target_index + 1, round(eval, 4)))

print("")

end = time.time()
print("Total elapsed time : {}[sec]".format(round(end - start, 4)))

print("#4 [Waveform drawing]")

index = 0
for y_and_sr in y_and_sr_list:
    y = y_and_sr[0]
    sr = y_and_sr[1]
    time = np.arange(0,len(y)) / sr
    plt.plot(time, y, label=path_list[index])
    index += 1

plt.xlabel("Time [s]")
plt.ylabel("Sound Amplitude")
plt.legend()
plt.show()
