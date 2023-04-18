# code_switch

## This code is for construction of code switch dataset in the paper()

## Usage

```

Follow the guideline(http://codepothunter.github.io/2016/07/11/How-to-use-GIZA-for-alignment/) for construction of phrase_table(the vocabulary mapping between two languages)

Load the parallel data for X(source language) and Y(target language)

Run the code: python code_switch.py to get the mixture data. You don't need to change the parameters in this code.

```

### Output

```
For each call of the function, the output would be the list [Source_language_mixed, Target_language_mixed]
```
