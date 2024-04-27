import streamlit as st

# Define a dictionary to store information about electronic devices
electronic_devices = {
    "smartphone": {
        "components": {
            "CPU": {"good_condition": 0.9, "rate": {"working": 10, "non_working": 2}},
            "memory": {"good_condition": 0.8, "rate": {"working": 8, "non_working": 1.5}},
            "battery": {"good_condition": 0.7, "rate": {"working": 15, "non_working": 3}},
            "display": {"good_condition": 0.95, "rate": {"working": 20, "non_working": 5}},
            "circuit board": {"good_condition": 0.85, "rate": {"working": 12, "non_working": 2.5}},
            "plastics": {"good_condition": 0.75, "rate": {"working": 5, "non_working": 1}},
            "metals": {"good_condition": 0.95, "rate": {"working": 10, "non_working": 2}}
        },
        "recycle_points": 20
    },
    "laptop": {
        "components": {
            "CPU": {"good_condition": 0.9, "rate": {"working": 25, "non_working": 5}},
            "memory": {"good_condition": 0.85, "rate": {"working": 20, "non_working": 4}},
            "battery": {"good_condition": 0.8, "rate": {"working": 30, "non_working": 6}},
            "display": {"good_condition": 0.9, "rate": {"working": 40, "non_working": 10}},
            "keyboard": {"good_condition": 0.85, "rate": {"working": 15, "non_working": 3}},
            "circuit board": {"good_condition": 0.85, "rate": {"working": 20, "non_working": 4}},
            "plastics": {"good_condition": 0.75, "rate": {"working": 10, "non_working": 2}},
            "metals": {"good_condition": 0.9, "rate": {"working": 15, "non_working": 3}}
        },
        "recycle_points": 50
    },
    # Add more electronic devices here
}

def calculate_reward(device_type, quantity, condition, component_scores):
    if device_type in electronic_devices:
        device_info = electronic_devices[device_type]
        total_price = 0
        total_points = 0
        component_details_recyclable = {}
        component_details_scrap = {}

        for component, info in device_info["components"].items():
            score = component_scores.get(component, 5) / 10.0  # Default score is 5 (50%)
            if score >= 0.8:
                component_price = info["rate"][condition] * quantity
                component_points_value = device_info["recycle_points"] * info["good_condition"] * quantity
                total_price += component_price
                total_points += component_points_value
                condition_label = "Recyclable"
                component_details_recyclable[component] = {
                    "Percentage": score * 100,
                    "Recyclable Percentage": info["good_condition"] * 100,
                    "Credits": component_points_value  # You may replace this with credits assigned by the agent
                }
            else:
                component_price = 0
                condition_label = "Scrap"
                component_details_scrap[component] = {
                    "Value": info["rate"][condition] * quantity
                }

        return total_price, total_points, component_details_recyclable, component_details_scrap
    else:
        st.error("Invalid device type selected.")
        return None, None, None, None

def generate_recyclable_document(device_type, component_details_recyclable):
    document = f"# Recyclable Components Documentation for {device_type.capitalize()}\n\n"
    document += "## Components and Recycling Details:\n\n"
    for component, details in component_details_recyclable.items():
        document += f"### {component.capitalize()}\n"
        document += f"- Percentage: {details['Percentage']}%\n"
        document += f"- Recyclable Percentage: {details['Recyclable Percentage']}%\n"
        document += f"- Credits: {details['Credits']} credits\n\n"
    return document

def generate_scrap_document(device_type, component_details_scrap):
    document = f"# Scrap Components Documentation for {device_type.capitalize()}\n\n"
    document += "## Components and Scrap Values:\n\n"
    for component, details in component_details_scrap.items():
        document += f"### {component.capitalize()}\n"
        document += f"- Value: ${details['Value']}\n\n"
    return document

def main():
    st.title("E-Waste Reward Calculator")

    device_type = st.selectbox("Select Device Type", ["Smartphone", "Laptop"])
    quantity = st.number_input("Enter Quantity", min_value=1, step=1)
    condition = st.radio("Device Condition", ["Working", "Non-Working"])

    st.write("Enter Component Scores (1-10):")
    component_scores = {}
    for component in electronic_devices[device_type.lower()]["components"]:
        component_scores[component] = st.slider(f"{component.capitalize()} Score", 1, 10, 5)

    if st.button("Calculate"):
        total_reward, total_points, component_details_recyclable, component_details_scrap = calculate_reward(device_type.lower(), quantity, condition.lower(), component_scores)
        if total_reward is not None:
            st.write(f"Total Reward: ${total_reward}")
            st.write(f"Total Recycle Points: {total_points}")

            st.subheader("Recyclable Components")
            for component, details in component_details_recyclable.items():
                st.write(f"**{component.capitalize()}**")
                st.write(f"- Percentage: {details['Percentage']}%")
                st.write(f"- Recyclable Percentage: {details['Recyclable Percentage']}%")
                st.write(f"- Credits: {details['Credits']} credits")

            st.subheader("Scrap Components")
            for component, details in component_details_scrap.items():
                st.write(f"**{component.capitalize()}**")
                st.write(f"- Value: ${details['Value']}")

            # Generate documentation
            recyclable_document = generate_recyclable_document(device_type, component_details_recyclable)
            scrap_document = generate_scrap_document(device_type, component_details_scrap)

            st.download_button("Download Recyclable Documentation", data=recyclable_document, file_name=f"recyclable_document_{device_type.lower()}.md", mime="text/markdown")
            st.download_button("Download Scrap Documentation", data=scrap_document, file_name=f"scrap_document_{device_type.lower()}.md", mime="text/markdown")

if __name__ == "__main__":
    main()
