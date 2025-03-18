# E-Waste Reward Calculator

## Overview
The E-Waste Reward Calculator is a Streamlit-based web application that helps users estimate rewards and recycling points for electronic waste, such as smartphones and laptops. Users can input the condition of their devices and provide component scores to determine whether components are recyclable or scrap. The app also generates downloadable reports for recyclable and scrap components.

## Features
Select electronic device type (Smartphone or Laptop).
Input quantity and condition (Working/Non-Working).
Provide component scores (1-10) to assess recyclability.
Calculate total rewards and recycling points.
Display recyclable and scrap components separately.
Generate and download Recyclable and Scrap documentation.

## Installation
To run the application, follow these steps:

Clone this repository:

``` git clone https://github.com/your-repo/e-waste-reward-calculator.git ```

``` cd e-waste-reward-calculator ```

Install dependencies:

``` pip install streamlit ```

Run the application:

``` streamlit run app.py ```

## Usage
Select Device Type: Choose between Smartphone or Laptop.
Enter Quantity: Specify the number of devices.
Select Condition: Choose whether the device is Working or Non-Working.
Set Component Scores: Use sliders (1-10) to provide component quality scores.
Calculate Rewards: Click the Calculate button to compute rewards and recycling points.
View Results:
Recyclable Components: Displays recyclability percentage and earned credits.
Scrap Components: Displays the scrap value of non-recyclable components.
Download Reports: Click the Download Recyclable Documentation or Download Scrap Documentation buttons to save the reports.
