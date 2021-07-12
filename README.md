# IVF extremes

## 1 Overview

Python package to analyze IVF clinical data, helping in the idenfication of infertile women and in the characterization
of the following infertility endophenotypes:

- **LMR**: low oocyte maturity rate
- **IFR**: low fertilization rates 
- **PDA**: preimplantation developmental arrest

Extreme phenotypes are identified comparing individual outcomes in terms of oocyte maturation rate,
oocyte fertilization rate, and blastocyst production rate with typical rates observed in a reference population. 
and performing one tailed-Binomial hypothesis tests of IVF cycles outcomes.

The following paper provides an overview of the statistical model used, and an exemplary application.

Capalbo et al. "Genomics analysis of maternal exomes reveals new candidate genes and pathways for the diagnosis of oocyte maturation 
arrest and early embryonic developmental arrest in IVF" 2021

Please cite this paper if you use the package in work that leads to publication. 

## 2 Installation

### 2.1 Pip installation

IVF_extremes package can be installed directly from pip:

```console
$ pip install IVF_extremes
```

### 2.2 Conda installation

Not available yet

## 3 Usage

### 3.1 Single Case Processing


In its simplest operation, IVF_extremes processes IVF data from a single patient,
it compares the data with IVF typical outcomes, and provides a classification of the patient (and pvalues related to 
hypothesis tests). The analysis requires 5 inputs:

```console
$ IVF_extremes --coc num_coc --mii num_mii --fert num_fert --blast num_blast --age age
```

where num_coc, num_mii, num_fert and num_blast are not negative integer representing the total number 
of cocs, mature oocytes, fertilized oocytes and blastocysts, and age is the age of the patient, eg:

```console
$ IVF_extremes --coc 11 --mii 4 --fert 2 --blast 0 --age 38
```


To check all available options, type:

```console
$ IVF_extremes --help
```

### 3.2 Batch processing

Is it possible to analyze data from multiple patients using the following command:

```console
$ IVF_extremes_batch -i input.csv
```

where input.csv is a csv file with IVF clinical data to be analyzed (see: Input Data Format).

To estimate baseline rates from the input dataset, type:

```console
$ IVF_extremes_batch -i input.csv -e
```

To provide custom IVF outcomes rates, type:

```console
$ IVF_extremes_batch -i data/Sample_IVF_data.csv --om_rate 0.9```
```

To check all available options, type:

```console
$ IVF_extremes_batch --help
```

#### 3.2.1 Input Data Format 

For the case of batch processing input data must be in csv format, each line representing the outcome of an IVF cycle, 
using the following headers:
- Patient_ID: Unique identifier for the patient
- Cycle_ID: Unique identifier for the IVF cycle
- Age: Age of the patient at the time of oocyte pick-up
- COC: number of oocyte cumulus complexes
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

An example data file is in the github repository:

https://github.com/matteofigliuzzi/IVF_extremes/blob/master/data/Sample_IVF_data.csv


#### 3.2.2 Batch analysis example

Once the package is installed, download the example data file and run the following scripts:

```console
$ python sample_script.py
```

or

```console
$ IVF_extremes_batch -i data/Sample_IVF_data.csv
```

Either of these scripts executes the analysis on the sample data in the data folder.

## 4 Development

To download IVF_extremes, please use git to download the most recent development tree:


```console
$ git clone https://github.com/matteofigliuzzi/IVF_extremes.git
```

To install the package locally

```console
$ pip install -e .
```

To run the unit tests:

```console
$ cd IVF_extremes
$ python -m test discover
```