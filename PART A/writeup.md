# Data Cleaning and Quality Analysis – Writeup

## Overview

The goal of this task was to generate a synthetic dataset of customer support conversations and build a robust data cleaning pipeline to prepare it for machine learning training. The dataset simulates EMI collection call center conversations in three languages: English, Hindi, and Hinglish.

To mimic real-world noisy data, several quality issues were intentionally injected into approximately 30–40% of the conversations. These issues included empty conversation turns, duplicate turns, conversations with too few turns, invalid metadata fields, language mismatches, and garbled text caused by encoding problems.

A Python data cleaning pipeline was implemented to detect these issues and separate valid conversations from invalid ones.

---

## Assumptions Made During Cleaning

Several assumptions were made when designing the cleaning pipeline:

1. **Minimum number of turns**
   Conversations with fewer than two turns were rejected because meaningful dialogue requires interaction between at least two speakers.

2. **Empty or whitespace turns**
   Turns where the text field was empty or contained only whitespace were considered invalid because they provide no useful information for training a conversational model.

3. **Duplicate consecutive turns**
   If two consecutive turns had the same speaker and identical text, they were treated as duplicates and the conversation was rejected. This situation often occurs in corrupted logs or system retries.

4. **Invalid metadata**
   Conversations with negative call duration or missing/invalid outcomes were rejected because such metadata is inconsistent with real call center data.

5. **Language validation**
   Only three languages were accepted: English, Hindi, and Hinglish. Any conversation with a different label was considered invalid.

6. **Encoding issues**
   Text containing unusual characters such as "€", "¥", or "�" was flagged as a potential encoding issue and rejected.

---

## Hardest Issue to Detect

The most challenging issue to detect programmatically was **language mismatch**.

For example, a conversation could be labeled as "Hindi" but contain mostly English text. Accurately detecting this requires a language identification model.

Because the assignment focuses on building a basic pipeline, a simplified validation approach was used that checks whether the language label belongs to a predefined set. A more advanced solution could involve using a lightweight language detection library such as `langdetect` or `fastText`.

---

## Scaling to Large Datasets (100,000+ Conversations)

If the dataset size increased significantly, several improvements would be necessary:

1. **Streaming data processing**
   Instead of loading the entire dataset into memory, conversations should be processed line by line using streaming techniques.

2. **Parallel processing**
   Multiprocessing or distributed computing frameworks such as Dask or Spark could be used to speed up data validation.

3. **Better language detection**
   Integrating a trained language detection model would allow more accurate detection of language mismatches.

4. **Automated monitoring dashboards**
   Quality metrics such as rejection rates, language distribution, and metadata anomalies could be tracked through dashboards to help ML teams monitor data quality continuously.

---

## Conclusion

The implemented cleaning pipeline ensures that only high-quality conversations are passed to downstream machine learning tasks. By detecting common data quality issues and generating detailed quality reports, the pipeline helps improve the reliability of conversational AI training datasets.
