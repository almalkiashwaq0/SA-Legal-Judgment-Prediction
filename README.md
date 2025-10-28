# Legal Judgment Prediction in the Saudi Arabian Commercial Court

This repository provides the implementation and supporting resources for the research paper “Legal Judgment Prediction in the Saudi Arabian Commercial Court”.
The study introduces a deep learning framework for predicting judicial outcomes (Accepted vs. Rejected) based on Arabic commercial court case texts.
The approach leverages AraBERT-based sentence-level classification combined with document-level aggregation strategies to improve interpretability and performance.


| Folder                 | Description                                                                                                 |
| --------------------   | ----------------------------------------------------------------------------------------------------------- |
| `Data_Scraping/`       | Selenium-based scripts for collecting Saudi commercial case judgments from the Ministry of Justice website. |
| `Data_EDA_&_Labeling/` | Data cleaning, preprocessing, exploratory data analysis, and rule-based labeling of case outcomes.          |
| `Main_Methodology/`    | Core training notebooks for AraBERT models, sentence-level classification, and document-level aggregation.  |
| `Baselines/`           | Baseline experiments including TF-IDF + SVM, AraBERT-first512, XLM-RoBERTa, and Longformer models.          |



## Methodology Summary
The methodology follows a two-stage hierarchical approach:

1. Sentence-Level Classification
- Each case judgment is segmented into factual sentences.
- Sentences are encoded using AraBERT v2 with domain-specific preprocessing.
- A classifier predicts whether each sentence supports an Accepted or Rejected outcome.

2. Document-Level Aggregation
- Sentence predictions are aggregated using multiple strategies (e.g., mean, top-3 mean, confidence-weighted, and position-aware).
- The final judgment label is derived from these aggregated sentence-level probabilities.

Table 1. Document-Level Accuracy by Aggregation Method

| **Aggregation Method** | **Accuracy (%)** |
| ---------------------- | ---------------- |
| Max                    | 85.25            |
| Mean                   | 85.37            |
| Median                 | 84.99            |
| Top-3 Mean             | 85.42            |
| Length-Weighted        | 85.41            |
| Confidence-Weighted    | 85.62            |
| Positional-Early       | 81.39            |
| Positional-Late        | 84.92            |



## Baselines for Comparison
- Traditional models: TF-IDF + SVM
- Transformer baselines: AraBERT-first512, XLM-RoBERTa, Longformer

Table 2. Baseline Model Accuracy

| **Baseline**             | **Accuracy (%)** |
| ------------------------ | ---------------- |
| TF-IDF + SVM             | 82.98            |
| AraBERT v2               | 78.71            |
| XLM-RoBERTa-base (XLM-R) | 77.38            |
| Longformer (base-4096)   | 76.09            |



## Dataset Access
The dataset was constructed from publicly available Saudi Commercial Court judgments provided by the  
[Ministry of Justice](https://www.moj.gov.sa/).

Due to legal and privacy considerations, the raw data cannot be publicly distributed.  
For academic or research collaboration, please [contact the author directly](mailto:almalkiashwag1@gmail.com).

## Paper Reference:  
Title: Legal Judgment Prediction in the Saudi Arabian Commercial Court
Authors: Ashwaq Almalki, Safa Alsafari, and Noura M. Alotaibi
Journal: Future Internet (MDPI), 2025
DOI:[Link to Paper](https://www.mdpi.com/1999-5903/17/10/439)
