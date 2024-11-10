# Census Data Standardization and Analysis Pipeline
Capstone_Project_1

## Project Overview
This project focuses on creating a comprehensive pipeline for cleaning, standardizing, and analyzing census data. The pipeline involves a series of tasks, such as data import, cleaning, renaming, and handling missing values, along with managing state formation updates. Once processed, the data is stored in MongoDB and MySQL for interactive querying and analysis. The project culminates in a Streamlit web app that enables dynamic data visualization and insights.

## Tools Used
Programming: Python

Libraries: Pandas (data handling), Matplotlib (visualization)

Databases: MongoDB (NoSQL), MySQL (SQL)

Utilities: MySQL Connector Python, PyMongo, Streamlit (for web app interface)


## Basic Workflow

1. Start Process:

2. Data Import: Load census data from a CSV file.
Standardize Columns: Rename and format columns to a consistent standard.
Edit Data: Adjust data entries to align with new rules and standards.
Missing Data Handling:

3. Identify Missing Data: Calculate the percentage of missing data for each column (before cleaning).
Fill Missing Values:
If Complete Data: Fill values based on specific calculated metrics.
If Incomplete Data: Leave values as missing if necessary metrics are unavailable.
Post-Cleaning Analysis:

4. Recalculate Missing Data: Calculate missing data percentages after cleaning.
Log Missing Data Details: Output missing data information into a file for visualization.
Database Upload:

5. Upload to MongoDB: Store cleaned data in MongoDB.
Transfer to MySQL: Retrieve data from MongoDB and upload to MySQL for further analysis.
Data Querying and Display:

6. Query MySQL: Extract relevant insights.
Visualize with Streamlit: Display results interactively using Streamlit.
End Process

## Technologies
- **Python**: Data processing and pipeline automation
- **MongoDB**: Storage of cleaned data in a NoSQL database
- **SQL (MySQL/PostgreSQL)**: Structured data querying and analysis
- **Streamlit**: Building an interactive interface for data visualization

## Note :

1. Please make sure that you're connected to the MySQL server before running the files.

2. Please run the census_data.ipynb first. The census_data.ipynb file consists the Data imports, cleaning and uploading to Database.

3. Before running the census_data.ipynb file make sure to change the variable uri with your MongoDB localhost connection string. (At the beginning of Task 5)

4. Please make sure that you have installed streamlit before running the streamlit_app.py file.

5. In case if you've not installed streamlit previously, open the Project document in VS Code, open the terminal and execute the command - pip install streamlit. Or just open command prompt and execute the command pip install streamlit.

6. In order to run the streamlit_app.py, open the terminal and execute - streamlit run streamlit_app.py

## Project Structure
```plaintext
.
├── data/                      # Contains raw and sample census data files
├── scripts/                   # Python scripts for each pipeline task
│   └── streamlit_app.py       # Streamlit interface for visualization
├── README.md                  # Project documentation
├── requirements.txt           # Project dependencies
└── census_data.ipynb          # Main notebook for end-to-end pipeline execution
