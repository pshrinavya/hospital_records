# ============================================
# SMART HOSPITAL ANALYTICS SYSTEM
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# LOAD CSV FILE
# ============================================

df = pd.read_csv("hospital_records.csv")

# ============================================
# SEARCH PATIENT BY NAME
# ============================================

def search_patient():

    print("\n========== SEARCH PATIENT ==========\n")

    name = input("Enter Patient Name: ")

    result = df[df["Name"].str.lower() == name.lower()]

    if result.empty:
        print("\n❌ No Patient Found\n")

    else:
        print("\n========== PATIENT DETAILS ==========\n")
        print(result.to_string(index=False))

# ============================================
# SEARCH BY DISEASE
# ============================================

def search_disease():

    print("\n========== DISEASE SEARCH ==========\n")

    disease = input("Enter Disease Name: ")

    result = df[df["Disease"].str.lower() == disease.lower()]

    if result.empty:
        print("\n❌ No Disease Record Found\n")

    else:
        print("\n========== DISEASE DETAILS ==========\n")
        print(result.to_string(index=False))

# ============================================
# SEARCH BY DOCTOR
# ============================================

def search_doctor():

    print("\n========== DOCTOR SEARCH ==========\n")

    doctor = input("Enter Doctor Name: ")

    result = df[df["Doctor"].str.lower() == doctor.lower()]

    if result.empty:
        print("\n❌ No Doctor Record Found\n")

    else:
        print("\n========== DOCTOR DETAILS ==========\n")
        print(result.to_string(index=False))

# ============================================
# DISPLAY ALL RECORDS
# ============================================

def display_all():

    print("\n========== ALL HOSPITAL RECORDS ==========\n")

    print(df.to_string(index=False))

# ============================================
# DISEASE ANALYSIS
# ============================================

def disease_analysis():

    print("\n========== DISEASE ANALYSIS ==========\n")

    disease_count = df["Disease"].value_counts()

    print(disease_count)

    plt.figure(figsize=(10,6))

    disease_count.plot(
        kind='bar',
        color=['red','blue','green','orange','purple']
    )

    plt.title("Disease Distribution")
    plt.xlabel("Diseases")
    plt.ylabel("Number of Patients")

    plt.xticks(rotation=45)

    plt.show()

# ============================================
# DOCTOR WORKLOAD ANALYSIS
# ============================================

def doctor_analysis():

    print("\n========== DOCTOR WORKLOAD ==========\n")

    doctor_count = df["Doctor"].value_counts()

    print(doctor_count)

    plt.figure(figsize=(10,6))

    doctor_count.plot(
        kind='bar',
        color=['cyan','magenta','yellow','green']
    )

    plt.title("Doctor Workload")
    plt.xlabel("Doctors")
    plt.ylabel("Patients Handled")

    plt.xticks(rotation=45)

    plt.show()

# ============================================
# REVENUE ANALYSIS
# ============================================

def revenue_analysis():

    print("\n========== REVENUE ANALYSIS ==========\n")

    total = np.sum(df["Bill_Amount"])

    average = np.mean(df["Bill_Amount"])

    maximum = np.max(df["Bill_Amount"])

    minimum = np.min(df["Bill_Amount"])

    print(f"Total Revenue  : ₹{total}")
    print(f"Average Bill   : ₹{average}")
    print(f"Highest Bill   : ₹{maximum}")
    print(f"Lowest Bill    : ₹{minimum}")

# ============================================
# PATIENT STAY ANALYSIS
# ============================================

def stay_analysis():

    print("\n========== PATIENT STAY ANALYSIS ==========\n")

    longest = df["Days_Admitted"].max()

    shortest = df["Days_Admitted"].min()

    average = df["Days_Admitted"].mean()

    print(f"Longest Stay  : {longest} days")
    print(f"Shortest Stay : {shortest} days")
    print(f"Average Stay  : {average:.2f} days")

# ============================================
# BED OCCUPANCY FORECAST
# ============================================

def bed_forecast():

    print("\n========== BED OCCUPANCY FORECAST ==========\n")

    avg_days = df["Days_Admitted"].mean()

    patients = len(df)

    beds = int((avg_days * patients)/10)

    print(f"Estimated Beds Required : {beds}")

# ============================================
# READMISSION ANALYSIS
# ============================================

def readmission_analysis():

    print("\n========== READMISSION ANALYSIS ==========\n")

    readmit = df["Readmission"].value_counts()

    print(readmit)

    plt.figure(figsize=(6,6))

    plt.pie(
        readmit,
        labels=readmit.index,
        autopct='%1.1f%%'
    )

    plt.title("Readmission Analysis")

    plt.show()

# ============================================
# DEPARTMENT ANALYSIS
# ============================================

def department_analysis():

    print("\n========== DEPARTMENT ANALYSIS ==========\n")

    dept = df["Department"].value_counts()

    print(dept)

    plt.figure(figsize=(8,6))

    dept.plot(
        kind='bar',
        color=['pink','lightblue','lightgreen','gold']
    )

    plt.title("Department Wise Patients")
    plt.xlabel("Departments")
    plt.ylabel("Patients")

    plt.xticks(rotation=45)

    plt.show()

# ============================================
# STATISTICAL INSIGHTS
# ============================================

def statistical_insights():

    print("\n========== STATISTICAL INSIGHTS ==========\n")

    print(df.describe())

# ============================================
# MAIN MENU
# ============================================

while True:

    print("\n===================================")
    print(" SMART HOSPITAL ANALYTICS SYSTEM ")
    print("===================================")

    print("""
1. Search Patient by Name
2. Search by Disease
3. Search by Doctor
4. Display All Records
5. Disease Analysis
6. Doctor Workload Analysis
7. Revenue Analysis
8. Patient Stay Analysis
9. Bed Occupancy Forecast
10. Readmission Analysis
11. Department Analysis
12. Statistical Insights
13. Exit
""")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        search_patient()

    elif choice == '2':
        search_disease()

    elif choice == '3':
        search_doctor()

    elif choice == '4':
        display_all()

    elif choice == '5':
        disease_analysis()

    elif choice == '6':
        doctor_analysis()

    elif choice == '7':
        revenue_analysis()

    elif choice == '8':
        stay_analysis()

    elif choice == '9':
        bed_forecast()

    elif choice == '10':
        readmission_analysis()

    elif choice == '11':
        department_analysis()

    elif choice == '12':
        statistical_insights()

    elif choice == '13':
        print("\nThank You\n")
        break

    else:
        print("\n❌ Invalid Choice\n")