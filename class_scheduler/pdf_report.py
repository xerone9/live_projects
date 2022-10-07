from fpdf import FPDF
from datetime import datetime
import calendar


def date_in_range(date):
    get_year = str(date).split("-")[0]
    get_date = str(date).split("-")
    spring_start, spring_end = datetime(int(get_year), 1, 1), datetime(int(get_year), 6, 30)
    fixed_date = datetime(int(get_date[0]), int(get_date[1]), int(get_date[2]))
    if spring_start <= fixed_date <= spring_end:
        return str("Spring " + get_year)
    else:
        return str("Fall " + get_year)


def time_in_range(x):
    def result(start, current, end):
        return start <= current <= end

    if str(x) != "TimeSlot Removed":
        current_time = x.split(":")
        current = (int(current_time[0]), int(current_time[1]), 0)
        first_start_hour = (9, 0, 0)
        first_end_hour = (11, 45, 0)
        second_start_hour = (12, 0, 0)
        second_end_hour = (14, 45, 0)
        third_start_hour = (15, 0, 0)
        third_end_hour = (17, 45, 0)
        forth_start_hour = (18, 0, 0)
        forth_end_hour = (20, 45, 0)
        if result(first_start_hour, current, first_end_hour) is True:
            return str("First Slot")

        elif result(second_start_hour, current, second_end_hour) is True:
            return str("Second Slot")

        elif result(third_start_hour, current, third_end_hour) is True:
            return str("Third Slot")

        elif result(forth_start_hour, current, forth_end_hour) is True:
            return str("Forth Slot")


def generate_pdf_report(list):
    class PDF(FPDF):
        def header(self):
            date_complete = str(datetime.now()).split(".")
            date_and_time = date_complete[0].split(" ")
            date = date_and_time[0]

            schedule_date = ""
            schedule_day = ""
            for row in list:
                schedule_date = str(row).split(" ----- ")[4]
                datem = datetime.strptime(schedule_date, "%Y-%m-%d")
                schedule_day = str(calendar.day_name[datem.weekday()])
                break


            # Logo
            # self.image('iu_logo.png', 10, 8, 55)
            self.set_font('helvetica', 'IU', 12)
            self.cell(150)
            self.cell(10, 25, "Print Date: " + str(date), ln=0, align='L')
            self.ln(5)
            # font
            self.set_font('helvetica', 'B', 20)
            # Padding
            self.cell(70)
            # Title
            self.cell(60, 30, 'Schedule Dated: ' + str(schedule_date), ln=1, align='C')
            self.cell(70)
            # Title
            self.cell(60, 1, schedule_day + ' Classes Time Table ' + str(date_in_range(schedule_date)), ln=1,
                      align='C')
            self.set_font('helvetica', '', 12)
            self.cell(80, 10, '', border=False, ln=1, align='R')
            # Line break


            self.set_font('helvetica', 'B', 16)
            self.cell(1)

            self.set_fill_color(r=0, g=0, b=0)
            self.set_text_color(255, 255, 255)
            self.cell(30, 10, "Timings", border=True, ln=0, fill=True)
            self.cell(60, 10, "Course Title ", border=True, ln=0, fill=True)
            self.cell(60, 10, "Teacher", border=True, ln=0, fill=True)
            self.cell(42, 10, "Location", border=True, ln=1, fill=True)


    # Create a PDF object
    pdf = PDF('P', 'mm', 'A4')

    # get total page numbers
    pdf.alias_nb_pages()

    # Set auto page break
    pdf.set_auto_page_break(auto = True, margin = 50)

    #Add Page
    pdf.add_page()

    # specify font

    pdf.set_font('helvetica', 'B', 14)

    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(208, 206, 206)
    # pdf.cell(192, 10, "SLOT 1", border=True, align='C', ln=1, fill=True)
    # pdf.set_font('helvetica', '', 10)

    list = sorted(list, reverse=False)
    index = 0
    for row in list:
        split_values = str(row).split(" ----- ")[0]
        split_time = str(split_values).split(" TO ")[0]
        index += 1
        if time_in_range(split_time) == "First Slot":
            list.insert(index - 1, "First Slot")
            break

    index = 0
    for row in list:
        index += 1
        if row != "First Slot":
            split_values = str(row).split(" ----- ")[0]
            split_time = str(split_values).split(" TO ")[0]
            if time_in_range(split_time) == "Second Slot":
                list.insert(index - 1, "Second Slot")
                break

    index = 0
    for row in list:
        index += 1
        if row != "First Slot" and row != "Second Slot":
            split_values = str(row).split(" ----- ")[0]
            split_time = str(split_values).split(" TO ")[0]
            if time_in_range(split_time) == "Third Slot":
                list.insert(index - 1, "Third Slot")
                break

    index = 0
    for row in list:
        index += 1
        if row != "First Slot" and row != "Second Slot" and row != "Third Slot":
            split_values = str(row).split(" ----- ")[0]
            split_time = str(split_values).split(" TO ")[0]
            if time_in_range(split_time) == "Forth Slot":
                list.insert(index - 1, "Forth Slot")
                break

    index = 0
    for row in list:
        index += 1
        if row != "First Slot" and row != "Second Slot" and row != "Third Slot" and row != "Forth Slot":
            split_time = str(row).split(" ----- ")[0]
            if str(split_time) == "TimeSlot Removed":
                list.insert(index - 1, "TimeSlots Removed")
                break

    for item in list:
        pdf.set_text_color(0, 0, 0)
        if item == "First Slot":
            pdf.cell(1)
            pdf.set_fill_color(208, 206, 206)
            pdf.set_font('helvetica', 'B', 14)
            pdf.cell(192, 10, "SLOT 1", border=True, align='C', ln=1, fill=True)
        elif item == "Second Slot":
            pdf.cell(1)
            pdf.set_fill_color(208, 206, 206)
            pdf.set_font('helvetica', 'B', 14)
            pdf.cell(192, 10, "SLOT 2", border=True, align='C', ln=1, fill=True)
        elif item == "Third Slot":
            pdf.cell(1)
            pdf.set_fill_color(208, 206, 206)
            pdf.set_font('helvetica', 'B', 14)
            pdf.cell(192, 10, "SLOT 3", border=True, align='C', ln=1, fill=True)
        elif item == "Forth Slot":
            pdf.cell(1)
            pdf.set_fill_color(208, 206, 206)
            pdf.set_font('helvetica', 'B', 14)
            pdf.cell(192, 10, "SLOT 4", border=True, align='C', ln=1, fill=True)
        elif item == "TimeSlots Removed":
            pdf.cell(1)
            pdf.set_fill_color(208, 206, 206)
            pdf.set_font('helvetica', 'B', 14)
            pdf.cell(192, 10, "Unknown Slots", border=True, align='C', ln=1, fill=True)
        else:
            pdf.set_font('helvetica', '', 10)
            split_data = str(item).split(" ----- ")
            pdf.cell(1)
            if str(split_data[0]) == "TimeSlot Removed":
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)
            pdf.cell(32, 10, str(split_data[0]), border=True, ln=0)
            pdf.set_text_color(0, 0, 0)
            if str(split_data[1]) == " Subject Removed":
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)
            if len(str(split_data[1])) > 30:
                pdf.cell(60, 10, str(split_data[1][0:30]) + " ...", border=True, ln=0)
            else:
                pdf.cell(60, 10, str(split_data[1]), border=True, ln=0)
            pdf.set_text_color(0, 0, 0)
            if str(split_data[2]) == "Teacher Removed":
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)
            pdf.cell(60, 10, str(split_data[2]), border=True, ln=0)
            pdf.set_text_color(0, 0, 0)
            if str(split_data[3]) == "Room Removed":
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)
            pdf.cell(40, 10, str(split_data[3]), border=True, ln=1)

    pdf.set_font('times', '', 12)
    saveLocation = "pdf_report.pdf"
    pdf.output(saveLocation)


# list = ['09:00 - 10:00 ----- Interior Design Studio-I sssssssssssssssssssssssssssssss(Thy) ----- Sadia Perveen (Visiting) ----- Fashion theis room', '09:00 - 11:00 ----- Design Collection-I (Lab) ----- Faryal Ahsun (Fulltime) ----- Fashion thesis room', '09:00 - 11:00 ----- History of Art &amp; Culture-I ----- Zainab Abid (Visiting) ----- LEcture Room,LEcture Room', '09:00 - 11:00 ----- History of Art &amp; Culture-II ----- Afsheen Khalid (Visiting) ----- Lecture Room', '09:00 - 11:00 ----- Intro to Textile ----- Fareesa Javaid (Fulltime) ----- Lecture Room,Computer Lab', '09:00 - 12:00 ----- Business English,Business English ----- Yamna Khan (Visiting) ----- Lecture Room,LEcture Room', '09:00 - 12:00 ----- Digital Communication-II (Lab) ----- Amna Hashmi (Visiting) ----- Lecture Room,Lecture Room', '10:00 - 12:00 ----- Interior Design Studio-I (Lab) ----- Sadia Perveen (Visiting) ----- Seminar Hall', '10:00 - 13:00 ----- Collection-II (Thesis) (Lab) ----- Noor Ul Ain Shaikh (Visiting) ----- Textile Thesis Room', '11:00 - 12:00 ----- Design Collection-II (Lab) ----- Faryal Ahsun (Fulltime) ----- Textile thesis Lab', '12:30 - 14:30 ----- History of Art and Architecture-I ----- Kainat Riaz (Fulltime) ----- Thesis room,Lecture Room', '12:30 - 14:30 ----- History of Arts ----- Syeda Mona Batool Taqvi (Visiting) ----- lec room', '12:30 - 15:30 ----- Design Collection-III (Lab) ----- Faryal Ahsun (Fulltime) ----- Fashion theis room', '12:30 - 15:30 ----- English-I (Compulsory) ----- Zuraiz Akhter (Fulltime) ----- Fashion thesis room', '12:30 - 15:30 ----- History of Media Art ----- Syeda Mona Batool Taqvi (Visiting) ----- LEcture Room,LEcture Room', '12:30 - 15:30 ----- Media Laws and Ethics ----- Ayesha Naveed (Fulltime) ----- Lec room', '15:30 - 18:30 ----- Media Laws and Ethics ----- Ayesha Naveed (Fulltime) ----- Lec room', '15:30 - 18:30 ----- Media Laws and Ethics ----- Ayesha Naveed (Fulltime) ----- Lec room', '15:30 - 18:30 ----- Media Laws and Ethics ----- Ayesha Naveed (Fulltime) ----- Lec room', '15:30 - 18:30 ----- Media Laws and Ethics ----- Ayesha Naveed (Fulltime) ----- Lec room']
# generate_pdf_report(list, "Monday", "Fall 2022")