# IAM Integration

## Getting Started

SecZetta has integrations with all of the top Identity and Access Management (IAM) tools in the market. There are *primarily* 2 ways our customers integrate with their IAM solutions depending on the capabilities of the IAM tool.

### 1. IAM initated data aggregation

This integration is initiated from the IAM system itself. These solutions sometimes call this data aggregations, data collection, or something similar. All of your IAM tools will have some sort of connector framework that will allow data to flow from an external place into the IAM system itself. 

Within this integration type there is also 2 ways to go about it. There is a flat file based integration and there is API based integration. 

#### Flat File Integration

For this integration the IAM tool simply looks for a file with a specific format in a specific location and pulls all data into the solutions internal database. This integration 'sub-type' is the easiest way to integrate your IAM system with SecZetta.

Common type of file formats are CSV, JSON, and maybe something like XML. CSV being the overwellmingly most popular of the three. Every IAM solution will be able to handle this type of integration

#### API Integration 
