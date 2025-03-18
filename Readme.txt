# E-Waste Reward Calculator

## Overview

The E-Waste Reward Calculator is a Streamlit-based web application designed to help users estimate the potential rewards and recycling points for their electronic waste, specifically smartphones and laptops. By inputting details about the device's condition and providing scores for individual components, users can understand the breakdown of recyclable and scrap parts and the associated benefits. The application also generates downloadable reports summarizing this information.

## Features

* **Device Type Selection:** Allows users to choose the type of electronic device they are recycling (currently supports Smartphone and Laptop).
* **Quantity Input:** Enables users to specify the number of devices they are submitting for recycling.
* **Condition Selection:** Provides a clear choice between "Working" and "Non-Working" to describe the overall state of the device.
* **Component Scoring:** Features interactive sliders for each component of the selected device, allowing users to rate the condition of each part on a scale of 1 to 10. This scoring is crucial in determining component recyclability.
* **Reward and Point Calculation:** Automatically calculates the estimated total monetary reward and the number of recycling points based on the device type, quantity, condition, and the component scores provided.
* **Recyclable Component Breakdown:** Clearly displays a section detailing the components deemed recyclable based on the user scores. This includes the calculated recyclability percentage and the associated credits for those components.
* **Scrap Component Breakdown:** Provides a separate section outlining the components classified as scrap, along with their estimated scrap value.
* **Documentation Generation and Download:** Offers convenient buttons to generate and download Markdown-formatted reports for both recyclable and scrap components, allowing users to keep a record of the assessment.

## Installation

To get the E-Waste Reward Calculator up and running on your local machine, follow these steps:

1.  **Clone the Repository:** If you have the code hosted on a platform like GitHub, use the following command in your terminal to clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

    *(Replace `<repository_url>` with the actual URL of the repository)*

2.  **Navigate to the Project Directory:** Once the repository is cloned, move into the project directory using the `cd` command:

    ```bash
    cd <repository_name>
    ```

    *(Replace `<repository_name>` with the name of the directory created after cloning)*

3.  **Install Dependencies:** The application relies on the Streamlit library. If you haven't already, you can install it using pip:

    ```bash
    pip install streamlit
    ```

## Usage

1.  **Run the Application:** With the dependencies installed, you can launch the E-Waste Reward Calculator by running the following command in your terminal from within the project directory:

    ```bash
    streamlit run your_script_name.py
    ```

    *(Replace `your_script_name.py` with the actual name of the Python script containing the Streamlit application code, e.g., `ewaste_calculator.py` or `app.py`)*

2.  **Interact with the Application:** Once the application is running, your web browser should automatically open to the calculator interface. If it doesn't, you can usually find the local URL in your terminal output (typically something like `http://localhost:8501`).

3.  **Using the Calculator:**
    * **Select Device Type:** Use the dropdown menu to choose between "Smartphone" and "Laptop".
    * **Enter Quantity:** Type the number of devices you wish to recycle into the provided number input field.
    * **Select Condition:** Choose the overall condition of the device by selecting either the "Working" or "Non-Working" radio button.
    * **Set Component Scores:** For each listed component, use the corresponding slider to input a quality score between 1 and 10. A higher score indicates better condition.
    * **Calculate Rewards:** After providing all the necessary information, click the "Calculate" button.
    * **View Results:** The application will then display the calculated results:
        * **Recyclable Components:** A section will show the components that meet the criteria for recyclability based on their scores, along with their recyclability percentage and the associated credit value.
        * **Scrap Components:** Another section will detail the components classified as scrap and their estimated monetary value.
    * **Download Reports:** To save a record of the assessment, you can click either the "Download Recyclable Documentation" button to get a report of the recyclable components or the "Download Scrap Documentation" button for a report of the scrap components. The reports will be downloaded as Markdown files.
