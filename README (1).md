"WATERPRO — Automated Water Station Management

WaterPro is a simple Python-based water dispensing management system that tracks user water balance, allows withdrawals, and manages recharges using an Excel sheet as the database.

📌 Features

User Authentication by Number: Fetches user details from an Excel sheet.

Water Withdrawal: Decreases available water count.

Balance Check: Shows remaining water credits.

Recharge System: Supports plans of 300, 900, and 3600.

Auto‑update Excel Database: Saves all changes back to the Excel file.

📂 Project Structure
waterpro.py              # Main program logic
waterpro.xlsx            # Database storing user Number and C (water credits)
README.md                # Project documentation
🛠️ Requirements

Python 3.10+

Required libraries:

pip install numpy pandas matplotlib openpyxl

waterpro.xlsx must contain at least two columns:

Number – User ID

C – Water credit count

▶️ How to Run the Program

Place waterpro.py and waterpro.xlsx in the same project directory.

Update the Excel file path inside the script if necessary.

Run the script using:

python waterpro.py

Follow on‑screen instructions for:

Getting water

Checking balance

Recharging

💳 Recharge Plans
Amount	Credits Given
300	30 credits
900	90 credits
3600	360 credits

Credits are calculated as: credits = amount // 10

🔄 How the Logic Works
1. User Input

The user enters their number, and the program finds their record in the Excel sheet.

2. Main Menu Options

GetWater → Deducts 1 credit.

Balance → Shows remaining credits.

Recharge → Adds credits based on plan.

3. Data Update

After each operation, updated data is saved back into waterpro.xlsx.

🧪 Example Interaction
Hello welcome to the water station
enter your number: 101
1.GetWater
2.Balance
3.Recharge
enter your choose: 1
your remaining balance is: 14
🚀 Future Improvements

Add GUI using Tkinter / Streamlit.
Add authentication (PIN).
Add total usage history.
Convert Excel backend into SQL database.

👨‍💻 Author
Developed by Eswar Vivek.

📄 License
This project is free to use for educational and personal purposes.
