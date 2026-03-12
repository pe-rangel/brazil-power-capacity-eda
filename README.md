# Brazilian Power Generation Capacity Analysis

This project is an Exploratory Data Analysis (EDA) of the Brazilian power grid's installed capacity. Using public data from the National Electric System Operator (ONS), this script processes, cleans, and visualizes the distribution of power plants across different states, regions, and energy sources.

## Project Goals
I built this project to apply data manipulation and visualization techniques to real engineering data. The main objectives were:
- **Personal Development:** Focus on improving data analysis skills by putting into practice the use of Python libraries such as Pandas for data manipulation and Plotly for interactive data visualization.
- Analyze and clean CSV data from the ONS open data portal.
- Generate interactive visualizations to uncover insights.

## Key Insights
One of the most interesting findings in this analysis is the "Wind Power vs. Hydro Power" contradiction in Brazil:
* If we look purely at the **number of generators**, Wind Power dominates the chart (thousands of individual wind turbines).
* However, when we calculate the **actual installed capacity (in Megawatts)**, Hydroelectric power takes the lead with ease, proving that a few giant hydro turbines generate massively more power than thousands of wind turbines.

## Technologies Used
* **Python**
* **Pandas** (Data cleaning, filtering, and aggregation)
* **Plotly Express** (Interactive histograms and pie charts)

## Visualizations
*(Note: Plotly charts are interactive, run the script locally to explore the data.)*

<img width="1256" height="572" alt="newplot" src="https://github.com/user-attachments/assets/994b328c-805b-4199-abe4-7ee622e8dd5a" />
<img width="1256" height="572" alt="newplot (1)" src="https://github.com/user-attachments/assets/c9e3e726-387e-4348-b024-77fd6c8c7624" />
<img width="1256" height="572" alt="newplot (2)" src="https://github.com/user-attachments/assets/56422f45-1e16-4b32-8a0a-1f6f9c2661eb" />
<img width="1256" height="572" alt="newplot (3)" src="https://github.com/user-attachments/assets/e88db759-ed8b-4d80-bb12-77d6a39818ae" />

## How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/pe-rangel/brazil-power-capacity-eda.git
   ```
2. Navigate to the project directory:
   ```bash
   cd brazil-power-capacity-eda
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python brazil_power_generation_capacity.py
   ```
