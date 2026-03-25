# ETL-pipelines
ETL stands for Extract, Transform, and Load. In an ELT process, data is first extracted from a source, then transformed and formatted in a specific way, and finally loaded into a final storage location. These pipelines are useful for organizing and preparing data for future purposes such as performing analysis and model creation smoothly and efficiently.

## ETL Pipeline 1
### A pipeline to scrape textual data from any article on the web, which generates a DataFrame of word frequencies:

## NFL Data Pipeline (Local Medallion Architecture)
This project simulates a real-world data engineering pipeline using NFL API data.  

**Pipeline layers:**  

1. **Bronze:** Raw JSON data ingested from the NFL API and stored with timestamps
2. **Silver:** Cleaned and structured tables extracted from nested JSON
3. **Gold:** Analytics-ready datasets for downstream analysis or machine learning