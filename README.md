# IVF extremes

## 1 Overview

Python package to analyze IVF clinical data, helping identifying infertile women and characterizing the following infertility 
endophenotypes:

- **IFR**: low fertilization rates 
- **LMR**: low oocyte maturity rate
- **PDA**: preimplantation developmental arrest

Extreme phenotypes are identified by performing one tailed-Binomial hypothesis tests of IVF clinical outcomes.

The following paper provides an overview of the statistical model used, and an exemplary application.
If using the 
Ref to publication:

Capalbo et al. "Genomics analysis of maternal exomes reveals new candidate genes and pathways for the diagnosis of oocyte maturation 
arrest and early embryonic developmental arrest in IVF" 2021

We ask that you cite this paper if you use the package in work that leads to publication. 

## 2 Installation

### 2.1 Pip installation

```console
$ pip install IVF_extremes
```

### 2.2 Conda installation?

## 3 Usage

In its simplest operation, IVF_extremes requires only one input: a csv file with IVF clinical data to be analyzed 
(see: Input Data Format)

```console
$ IVF_extremes input.csv
```

### 3.1 Options

```console
$ IVF_extremes input.csv --no-baseline
```

### 3.2 Input Data Format 

Input data must be in csv format, each line representing the outcome of an IVF cycle, 
using the following headers:
- Patient_ID: Unique identifier for the patient
- Cycle_ID: Unique identifier for the IVF cycle
- Age: Age of the patient at the time of oocyte pick-up
- COC: number of COC oocytes
- MII: number of mature oocytes
- Fertilized: number of fertilized oocytes
- Blastocysts: number of developed blastocysts

Example data:

|Patient_ID|Cycle_ID|Age|COC|MII|Fertilized|Blastocysts|
|----------|--------|---|---|---|----------|-----------|
|1 |0|44|5|5|4|0|
|1|1|44|7|5|5|2|
|1|2|46|3|3|2|0|
|2|3|29|5|4|4|1|
|3|4|31|5|4|3|0|


### 3.3 Examples

Once the package is installed, run the following script:

```console
$ python sample_script.py
```

This execute the analysis on the sample data in the data folder.

## 4 Development

To download IVF_extremes, please use git to download the most recent development tree:


```console
$ git clone https://github.com/matteofigliuzzi/IVF_extremes.git
```

To install the package locally

```console
$ pip install -e .
```

https://python-packaging.readthedocs.io/en/latest/minimal.html
