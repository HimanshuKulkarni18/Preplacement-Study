import streamlit as st

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            "Name": self.name,
            "Position": self.position,
            "Salary": f"${{self.salary:,.2f}}",
        }


def get_employees():
    if "employees" not in st.session_state:
        st.session_state.employees = []
    return st.session_state.employees


def add_employee(name: str, position: str, salary: float) -> None:
    employees = get_employees()
    employees.append(Employee(name.strip(), position.strip(), salary))
    st.success(f"Employee {name.strip()} added successfully.")


def remove_employee(name: str) -> None:
    employees = get_employees()
    filtered = [employee for employee in employees if employee.name != name]
    if len(filtered) < len(employees):
        st.session_state.employees = filtered
        st.success(f"Employee {name} removed successfully.")
    else:
        st.warning(f"Employee {name} not found.")


def main():
    st.set_page_config(page_title="Employee Management System", layout="centered")
    st.title("Employee Management System")
    st.write("Manage employees in a simple Streamlit interface.")

    with st.form("employee_form"):
        name = st.text_input("Employee name")
        position = st.text_input("Position")
        salary = st.number_input("Salary", min_value=0.0, step=100.0, format="%.2f")
        submitted = st.form_submit_button("Add employee")

        if submitted:
            if not name.strip():
                st.error("Please enter a name.")
            else:
                add_employee(name, position, salary)

    st.markdown("---")
    employees = get_employees()

    if employees:
        st.subheader("Current employees")
        st.table([employee.to_dict() for employee in employees])

        with st.expander("Remove an employee"):
            remove_option = st.selectbox("Select employee to remove", [employee.name for employee in employees])
            if st.button("Remove"):
                remove_employee(remove_option)
                st.experimental_rerun()
    else:
        st.info("No employees added yet.")


if __name__ == "__main__":
    main()
