# LAB-08_database_design

## Overview
The database architecture for processing and evaluating financial gainer data gathered from Yahoo Finance, Wall Street Journal (WSJ), and StockAnalysis. The goal of this design is to organize raw stock market data into structured tables that support recurring stock detection, price behavior insights, and downstream analysis in Snowflake. The ERD below reflects how raw data is transformed into intermediate and final tables in preparation for analytical tasks and stakeholder reporting.

## Use Cases

- **Picking Recurring Stocks**: By identifying stock symbols that appear repeatedly across different sources and days, we can highlight trending or consistently performing stocks that may merit further investment attention.
- **Understanding Price Ranges**: Compiling average, maximum, and minimum prices from various sources aids stakeholders in comprehending the market environment for these gainers.
- **Source Comparison**: Having raw data tracked by source enables direct comparisons of reporting patterns between Yahoo, WSJ, and StockAnalysis.
- **Supporting Future Analysis**: The data is prepared to be expanded with candlestick information in subsequent labs, enabling a more thorough examination of performance patterns over time

## Methods

Custom Python normalization scripts were used to handle each CSV file from the data sources (Yahoo, WSJ, and StockAnalysis). These scripts introduced a `source` field, cleaned the data, and extracted consistent columns (`symbol`, `price`, `price_change`, `price_percent_change`). A single `RAW-DATA` table included all of the normalized data. From this base, intermediary tables were developed to calculate price behavior summaries (`PRICE-DISTRIBUTION`) and track the frequency of symbol instances across sources (`SYMBOL-FREQUENCY`). These intermediate results feed into the final `CONSOLIDATED-ANALYSIS` table for broader insights.

## Summary

The ERD successfully outlines how raw data is transformed into a structured format that supports both high-level insights and deeper analysis. The tables provide a solid foundation for answering key stakeholder questions around recurring stock symbols, pricing patterns, and source reliability.  Additional data like candlestick patterns, sector classification, or sentiment scores could further enhance the value of the analysis in future phases. The ERD captures the essential components needed to explore what is in the gainers lists and how to use them effectively.
## Entity Relationship Diagram

```mermaid
erDiagram
	YAHOO ||--o{ RAW-DATA : "contributes"
	WSJ ||--o{ RAW-DATA : "contributes"
	SANALYSIS ||--o{ RAW-DATA : "contributes"
	RAW-DATA {
		string symbol
		float price
		float price_change
		float price_percent_change
		string source
	}
	RAW-DATA ||--o{ SYMBOL-FREQUENCY : "extracts"
	SYMBOL-FREQUENCY {
		string symbol
		int total_occurrences
		int yahoo_occurrences
		int wsj_occurrences
		int sanalysis_occurrences
	}
	RAW-DATA ||--o{ PRICE-DISTRIBUTION : "compiles"
	PRICE-DISTRIBUTION {
		string symbol
		float average_price
		float max_price
		float min_price
	}
	SYMBOL-FREQUENCY ||--|| CONSOLIDATED-ANALYSIS : "aggregates"
	CONSOLIDATED-ANALYSIS {
		string symbol
		float average_price_change
		float total_volume
		string most_frequent_source
	}
