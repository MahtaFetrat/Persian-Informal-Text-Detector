# Persian-Informal-Text-Detector
Persian Informal Text Detector is a rule-based informal text detector based on regular expressions. It can be used to identify informal Persian text by detecting certain indicators such as informal words and verb formats.

## Source of Informal Text Indicators
Some of the informal text indicators, such as informal words and verb formats, are derived from [this Wikipedia page](https://fa.wikipedia.org/wiki/%D9%88%DB%8C%DA%A9%DB%8C%E2%80%8C%D9%BE%D8%AF%DB%8C%D8%A7:%D8%A7%D8%B4%D8%AA%D8%A8%D8%A7%D9%87%E2%80%8C%DB%8C%D8%A7%D8%A8/%D9%81%D9%87%D8%B1%D8%B3%D8%AA/%D8%BA%DB%8C%D8%B1%D8%B1%D8%B3%D9%85%DB%8C).

## Installation
You can install Persian Informal Text Detector using pip:
```bash
pip install informal_detector
```

## Example Usage
```python
from informal_detector import is_informal

# Returns True since the text contains at least one informal indicator
result1 = is_informal("دلم میخواد برم خونه", threshold=1)
print(result1)  # Output: True

# Returns False since the text does not contain enough informal indicators
result2 = is_informal("نباید به خانه بروم", threshold=1)
print(result2)  # Output: False
```

## The threshold Argument
The `threshold` keyword argument is crucial as it indicates how strict the detector should be. It determines the number of informal Persian indicators, such as informal words and verbs, required to classify a text as informal.

A lower threshold is suitable for smaller text files, while a higher threshold is more appropriate for larger files where some formal sentences might exist but the text should still be marked as informal if it contain a significant number of informal indicators. A threshold of 1 means that a text is considered informal if it contains at least one informal word or verb.

## Contribution
If you come across any issues or have ideas for improvements, please don't hesitate to let us know by opening an issue or sending a pull request. Thank you for using Persian Informal Text Detector!
