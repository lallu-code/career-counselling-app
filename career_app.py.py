import streamlit as st
import json
import os

# JSON file path
DATA_FILE = "careers.json"

# Load career data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

# Save career data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# View all careers
def view_all_careers(data):
    st.subheader("Available Careers")
    for career in data:
        st.write(f"- {career}")

# View detailed info
def view_career_details(data):
    st.subheader("Career Details")
    career_list = list(data.keys())
    if career_list:
        selected = st.selectbox("Select a career", career_list)
        details = data[selected]
        st.markdown(f"**Description:** {details['description']}")
        st.markdown(f"**Salary:** {details['salary']}")
        st.markdown(f"**Opportunities:** {', '.join(details['opportunities'])}")
        st.markdown(f"**Future Prospects:** {details['future_prospects']}")
        st.markdown(f"**Top Universities:** {', '.join(details['universities'])}")
    else:
        st.warning("No careers found. Please add some.")

# Add a new career
def add_career(data):
    st.subheader("Add a New Career")
    name = st.text_input("Career Name")
    description = st.text_area("Description")
    salary = st.text_input("Salary Range")
    opportunities = st.text_input("Opportunities (comma-separated)")
    future_prospects = st.text_area("Future Prospects")
    universities = st.text_input("Top Universities (comma-separated)")

    if st.button("Add Career"):
        if name in data:
            st.error("Career already exists.")
        elif name and description and salary and opportunities and future_prospects and universities:
            data[name] = {
                "description": description,
                "salary": salary,
                "opportunities": [op.strip() for op in opportunities.split(",")],
                "future_prospects": future_prospects,
                "universities": [uni.strip() for uni in universities.split(",")]
            }
            save_data(data)
            st.success(f"{name} added successfully!")
        else:
            st.error("Please fill in all fields.")

# Main Streamlit app
def main():
    st.title("🎓 Career Counselling App")
    menu = ["Home", "View Career Details", "Add a Career"]
    choice = st.sidebar.selectbox("Menu", menu)

    data = load_data()

    if choice == "Home":
        view_all_careers(data)
    elif choice == "View Career Details":
        view_career_details(data)
    elif choice == "Add a Career":
        add_career(data)

if __name__ == "__main__":
    main()
