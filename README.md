![](logo.png)

# Waveform-Comparator

Calculate the similarity between two waveforms in Python.

## Demo

![](demo.gif)

## Features

* Easy to set up with an interactive prompt.
* The following three types of features can be set.

    SPECTRUM, SPECTRUM_CENTROID, MFCC

* You can compare multiple wav files at once.
* Waveforms can be overlaid and drawn.

## Requirement

* Python 3.10.5
* librosa 0.9.2
* numpy 1.22.4
* matplotlib 3.5.2

## Installation

1. Install [Python](https://www.python.org/downloads/).

2. Clone this repository.

3. Install the required modules from [requirements.txt](https://github.com/yuukuru0511/Waveform-Comparator/blob/main/requirements.txt).

```bash
git clone https://github.com/yuukuru0511/Waveform-Comparator.git
pip install -r requirements.txt
```

## Usage

Run [script/main.py](https://github.com/yuukuru0511/Waveform-Comparator/blob/main/script/main.py).

```bash
cd Waveform-Comparator
python script/main.py
```

Enter the settings at the interactive prompt.

1. Enter the path to the Wav file.
2. Select the feature type.
3. Select a Wav file as the basis for comparison.
4. Calculate the similarity.
5. Draw waveform.

## Note

* I have not tested it in a Linux or Mac environment.
* GUI will be implemented.

## Author

* Yuukuru

## License

MIT license (See
[LICENSE](https://github.com/yuukuru0511/Waveform-Comparator/blob/main/LICENSE) file)
