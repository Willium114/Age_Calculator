import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import calendar


class AgeCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Age Calculator")
        self.root.geometry("650x800")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)

        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configure custom styles
        self.style.configure('Title.TLabel',
                             background='#1a1a2e',
                             foreground='#eee6ff',
                             font=('Arial', 24, 'bold'))

        self.style.configure('Heading.TLabel',
                             background='#1a1a2e',
                             foreground='#bb86fc',
                             font=('Arial', 14, 'bold'))

        self.style.configure('Info.TLabel',
                             background='#1a1a2e',
                             foreground='#e0e0e0',
                             font=('Arial', 12))

        self.style.configure('Result.TLabel',
                             background='#16213e',
                             foreground='#03dac6',
                             font=('Arial', 16, 'bold'),
                             relief='solid',
                             borderwidth=1)

        self.style.configure('Custom.TCombobox',
                             fieldbackground='#16213e',
                             background='#bb86fc',
                             foreground='#ffffff',
                             borderwidth=2,
                             font=('Arial', 11))

        self.style.configure('Custom.TButton',
                             background='#bb86fc',
                             foreground='#000000',
                             font=('Arial', 12, 'bold'),
                             borderwidth=0,
                             focuscolor='none')

        self.style.map('Custom.TButton',
                       background=[('active', '#9c64e8'),
                                   ('pressed', '#8e47e8')])

        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=40, pady=30)
        main_frame.pack(fill='both', expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="🎂 Age Calculator", style='Title.TLabel')
        title_label.pack(pady=(0, 10))

        # Producer credit
        producer_label = ttk.Label(main_frame, text="Produced by M. Aqib Javed",
                                   background='#1a1a2e', foreground='#888888',
                                   font=('Arial', 10, 'italic'))
        producer_label.pack(pady=(0, 25))

        # Birth date input section
        input_frame = tk.Frame(main_frame, bg='#16213e', relief='solid', bd=2, padx=25, pady=25)
        input_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(input_frame, text="Enter Your Birth Date", style='Heading.TLabel').pack(pady=(0, 15))

        # Date input row
        date_row = tk.Frame(input_frame, bg='#16213e')
        date_row.pack(pady=(0, 20))

        # Day selection
        day_frame = tk.Frame(date_row, bg='#16213e')
        day_frame.pack(side='left', padx=(0, 15))
        ttk.Label(day_frame, text="Day", style='Info.TLabel').pack()
        self.day_var = tk.StringVar()
        self.day_combo = ttk.Combobox(day_frame, textvariable=self.day_var,
                                      values=[str(i) for i in range(1, 32)],
                                      width=5, style='Custom.TCombobox', state='readonly')
        self.day_combo.pack(pady=(5, 0))

        # Month selection
        month_frame = tk.Frame(date_row, bg='#16213e')
        month_frame.pack(side='left', padx=(0, 15))
        ttk.Label(month_frame, text="Month", style='Info.TLabel').pack()
        self.month_var = tk.StringVar()
        months = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
        month_values = [f"{num} - {name}" for num, name in months]
        self.month_combo = ttk.Combobox(month_frame, textvariable=self.month_var,
                                        values=month_values, width=12,
                                        style='Custom.TCombobox', state='readonly')
        self.month_combo.pack(pady=(5, 0))

        # Year selection
        year_frame = tk.Frame(date_row, bg='#16213e')
        year_frame.pack(side='left')
        ttk.Label(year_frame, text="Year", style='Info.TLabel').pack()
        self.year_var = tk.StringVar()
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year - 100, current_year + 1)]
        self.year_combo = ttk.Combobox(year_frame, textvariable=self.year_var,
                                       values=years, width=8,
                                       style='Custom.TCombobox', state='readonly')
        self.year_combo.pack(pady=(5, 0))

        # Calculate to date section
        calc_date_frame = tk.Frame(main_frame, bg='#16213e', relief='solid', bd=2, padx=25, pady=25)
        calc_date_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(calc_date_frame, text="Calculate Age To Specific Date", style='Heading.TLabel').pack(pady=(0, 15))

        # Option selection
        option_frame = tk.Frame(calc_date_frame, bg='#16213e')
        option_frame.pack(pady=(0, 15))

        self.date_option = tk.StringVar(value="today")
        today_radio = tk.Radiobutton(option_frame, text="Calculate to Today",
                                     variable=self.date_option, value="today",
                                     bg='#16213e', fg='#e0e0e0', selectcolor='#bb86fc',
                                     font=('Arial', 11), command=self.toggle_date_inputs)
        today_radio.pack(side='left', padx=(0, 20))

        custom_radio = tk.Radiobutton(option_frame, text="Calculate to Custom Date",
                                      variable=self.date_option, value="custom",
                                      bg='#16213e', fg='#e0e0e0', selectcolor='#bb86fc',
                                      font=('Arial', 11), command=self.toggle_date_inputs)
        custom_radio.pack(side='left')

        # Custom date input row (initially hidden)
        self.custom_date_row = tk.Frame(calc_date_frame, bg='#16213e')

        ttk.Label(self.custom_date_row, text="Calculate age on:", style='Info.TLabel').pack(pady=(0, 5))

        custom_inputs = tk.Frame(self.custom_date_row, bg='#16213e')
        custom_inputs.pack()

        # Custom Day
        custom_day_frame = tk.Frame(custom_inputs, bg='#16213e')
        custom_day_frame.pack(side='left', padx=(0, 15))
        ttk.Label(custom_day_frame, text="Day", style='Info.TLabel').pack()
        self.custom_day_var = tk.StringVar()
        self.custom_day_combo = ttk.Combobox(custom_day_frame, textvariable=self.custom_day_var,
                                             values=[str(i) for i in range(1, 32)],
                                             width=5, style='Custom.TCombobox', state='readonly')
        self.custom_day_combo.pack(pady=(5, 0))

        # Custom Month
        custom_month_frame = tk.Frame(custom_inputs, bg='#16213e')
        custom_month_frame.pack(side='left', padx=(0, 15))
        ttk.Label(custom_month_frame, text="Month", style='Info.TLabel').pack()
        self.custom_month_var = tk.StringVar()
        self.custom_month_combo = ttk.Combobox(custom_month_frame, textvariable=self.custom_month_var,
                                               values=month_values, width=12,
                                               style='Custom.TCombobox', state='readonly')
        self.custom_month_combo.pack(pady=(5, 0))

        # Custom Year
        custom_year_frame = tk.Frame(custom_inputs, bg='#16213e')
        custom_year_frame.pack(side='left')
        ttk.Label(custom_year_frame, text="Year", style='Info.TLabel').pack()
        self.custom_year_var = tk.StringVar()
        custom_years = [str(year) for year in range(current_year - 50, current_year + 51)]
        self.custom_year_combo = ttk.Combobox(custom_year_frame, textvariable=self.custom_year_var,
                                              values=custom_years, width=8,
                                              style='Custom.TCombobox', state='readonly')
        self.custom_year_combo.pack(pady=(5, 0))

        # Calculate button
        calc_button = ttk.Button(calc_date_frame, text="Calculate Age",
                                 style='Custom.TButton', command=self.calculate_age)
        calc_button.pack(pady=(15, 0))

        # Results section
        self.results_frame = tk.Frame(main_frame, bg='#16213e', relief='solid', bd=2)

        # Fun facts section (initially hidden)
        self.facts_frame = tk.Frame(main_frame, bg='#16213e', relief='solid', bd=2)

    def toggle_date_inputs(self):
        """Toggle visibility of custom date inputs based on radio button selection"""
        if self.date_option.get() == "custom":
            self.custom_date_row.pack(pady=(10, 0))
            # Set default values for custom date
            today = datetime.now()
            self.custom_day_combo.set(str(today.day))
            self.custom_month_combo.set(f"{today.month} - {calendar.month_name[today.month]}")
            self.custom_year_combo.set(str(today.year))
        else:
            self.custom_date_row.pack_forget()

    def calculate_age(self):
        try:
            # Get birth date input values
            day = int(self.day_var.get())
            month = int(self.month_var.get().split(' - ')[0])
            year = int(self.year_var.get())

            # Validate birth date
            birth_date = date(year, month, day)

            # Get the target date (today or custom date)
            if self.date_option.get() == "today":
                target_date = date.today()
                date_context = "today"
            else:
                # Get custom date input values
                custom_day = int(self.custom_day_var.get())
                custom_month = int(self.custom_month_var.get().split(' - ')[0])
                custom_year = int(self.custom_year_var.get())
                target_date = date(custom_year, custom_month, custom_day)
                date_context = f"{target_date.strftime('%B %d, %Y')}"

            if birth_date > target_date:
                self.show_error("Birth date cannot be after the target date!")
                return

            # Calculate age to target date
            age_years = target_date.year - birth_date.year
            age_months = target_date.month - birth_date.month
            age_days = target_date.day - birth_date.day

            # Adjust for negative days
            if age_days < 0:
                age_months -= 1
                # Get days in previous month
                if target_date.month == 1:
                    prev_month_days = calendar.monthrange(target_date.year - 1, 12)[1]
                else:
                    prev_month_days = calendar.monthrange(target_date.year, target_date.month - 1)[1]
                age_days += prev_month_days

            # Adjust for negative months
            if age_months < 0:
                age_years -= 1
                age_months += 12

            # Calculate total days, weeks, months
            total_days = (target_date - birth_date).days
            total_weeks = total_days // 7
            total_months = age_years * 12 + age_months
            total_hours = total_days * 24
            total_minutes = total_hours * 60

            # Calculate next birthday from target date
            next_birthday = date(target_date.year, birth_date.month, birth_date.day)
            if next_birthday < target_date:
                next_birthday = date(target_date.year + 1, birth_date.month, birth_date.day)
            days_to_birthday = (next_birthday - target_date).days

            self.display_results(age_years, age_months, age_days, total_days,
                                 total_weeks, total_months, total_hours, total_minutes,
                                 days_to_birthday, birth_date, date_context)

        except ValueError:
            self.show_error("Please select valid date values!")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def display_results(self, years, months, days, total_days, total_weeks,
                        total_months, total_hours, total_minutes, days_to_birthday, birth_date, date_context):
        # Clear previous results
        self.results_frame.destroy()
        self.facts_frame.destroy()

        # Main age result
        self.results_frame = tk.Frame(self.root, bg='#16213e', relief='solid', bd=2, padx=25, pady=20)
        self.results_frame.pack(fill='x', padx=40, pady=(0, 10))

        # Dynamic title based on date context
        if date_context == "today":
            title_text = "Your Current Age"
        else:
            title_text = f"Your Age on {date_context}"

        ttk.Label(self.results_frame, text=title_text, style='Heading.TLabel').pack(pady=(0, 15))

        # Primary age display
        age_text = f"{years} years, {months} months, {days} days"
        age_label = tk.Label(self.results_frame, text=age_text,
                             bg='#16213e', fg='#03dac6', font=('Arial', 18, 'bold'))
        age_label.pack(pady=(0, 20))

        # Additional stats in a grid
        stats_frame = tk.Frame(self.results_frame, bg='#16213e')
        stats_frame.pack()

        # Row 1
        row1 = tk.Frame(stats_frame, bg='#16213e')
        row1.pack(pady=5)

        self.create_stat_box(row1, "Total Months", f"{total_months:,}")
        self.create_stat_box(row1, "Total Weeks", f"{total_weeks:,}")

        # Row 2
        row2 = tk.Frame(stats_frame, bg='#16213e')
        row2.pack(pady=5)

        self.create_stat_box(row2, "Total Days", f"{total_days:,}")
        self.create_stat_box(row2, "Total Hours", f"{total_hours:,}")

        # Fun facts section
        self.facts_frame = tk.Frame(self.root, bg='#16213e', relief='solid', bd=2, padx=25, pady=20)
        self.facts_frame.pack(fill='x', padx=40, pady=(0, 20))

        ttk.Label(self.facts_frame, text="🎉 Fun Facts", style='Heading.TLabel').pack(pady=(0, 15))

        # Birthday countdown (adjust text based on context)
        if date_context == "today":
            birthday_text = f"Days until next birthday: {days_to_birthday}"
        else:
            if days_to_birthday == 0:
                birthday_text = f"🎂 It's your birthday on {date_context}!"
            else:
                birthday_text = f"Days to next birthday from {date_context}: {days_to_birthday}"

        ttk.Label(self.facts_frame, text=birthday_text, style='Info.TLabel').pack(pady=2)

        # Day of week born
        day_born = birth_date.strftime("%A")
        born_text = f"You were born on a {day_born}"
        ttk.Label(self.facts_frame, text=born_text, style='Info.TLabel').pack(pady=2)

        # Minutes lived (adjust text based on context)
        if date_context == "today":
            minutes_text = f"You've lived approximately {total_minutes:,} minutes!"
        else:
            minutes_text = f"You will have lived {total_minutes:,} minutes by {date_context}!"

        ttk.Label(self.facts_frame, text=minutes_text, style='Info.TLabel').pack(pady=2)

        # Age in different planets (fun calculation)
        mars_age = round(years / 1.88, 1)  # Mars year is 1.88 Earth years
        venus_age = round(years / 0.62, 1)  # Venus year is 0.62 Earth years

        planet_frame = tk.Frame(self.facts_frame, bg='#16213e')
        planet_frame.pack(pady=(10, 0))

        planet_context = "today" if date_context == "today" else f"on {date_context}"
        ttk.Label(planet_frame, text=f"🪐 Age on Mars {planet_context}: {mars_age} years", style='Info.TLabel').pack()
        ttk.Label(planet_frame, text=f"🌟 Age on Venus {planet_context}: {venus_age} years", style='Info.TLabel').pack()

    def create_stat_box(self, parent, label, value):
        box = tk.Frame(parent, bg='#0f3460', relief='solid', bd=1, padx=15, pady=10)
        box.pack(side='left', padx=5)

        tk.Label(box, text=label, bg='#0f3460', fg='#bb86fc',
                 font=('Arial', 10, 'bold')).pack()
        tk.Label(box, text=value, bg='#0f3460', fg='#03dac6',
                 font=('Arial', 12, 'bold')).pack()

    def show_error(self, message):
        # Clear previous results
        self.results_frame.destroy()
        self.facts_frame.destroy()

        self.results_frame = tk.Frame(self.root, bg='#16213e', relief='solid', bd=2, padx=25, pady=20)
        self.results_frame.pack(fill='x', padx=40, pady=(0, 10))

        error_label = tk.Label(self.results_frame, text="❌ " + message,
                               bg='#16213e', fg='#ff6b6b', font=('Arial', 12, 'bold'))
        error_label.pack()

        self.facts_frame = tk.Frame(self.root, bg='#16213e')

    def run(self):
        # Set default values for better UX
        self.day_combo.set('1')
        self.month_combo.set('1 - January')
        self.year_combo.set('2000')

        # Set default custom date values
        today = datetime.now()
        self.custom_day_combo.set(str(today.day))
        self.custom_month_combo.set(f"{today.month} - {calendar.month_name[today.month]}")
        self.custom_year_combo.set(str(today.year))

        self.root.mainloop()


if __name__ == "__main__":
    app = AgeCalculator()
    app.run()