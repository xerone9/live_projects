import PyPDF2
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import fitz


def add_linebreaks_text_box_accordingly(value):
    length_limit = 115
    max_limit = 500
    data = value

    count = 0
    full_count = 0
    text_with_line_break = ""
    for index, value in enumerate(data):
        if count == 0 and value == " ":
            count += 1
            full_count += 1
        else:
            text_with_line_break += value
            count += 1
            full_count += 1
            try:
                if count == length_limit:
                    if data[index + 1] == " ":
                        text_with_line_break += "\n"
                        count = 0
                    else:
                        if value == " ":
                            text_with_line_break += "\n"
                            count = 0
                        elif data[index + 2] == " ":
                            count -= 1
                        else:
                            text_with_line_break += "-\n"
                            count = 0
                if full_count == max_limit:
                    break
            except IndexError:
                break

    return text_with_line_break.split("\n")


def generate_pdf_report(jubilee_data_dict):
    # for key, value in jubilee_data_dict.items():
    #     print(f"Field: {key}, Value: {value}")

    female = False

    if jubilee_data_dict["gender"] == "female":
        female = True

    congental = False
    infertility = False
    psychatric = False
    cosmetic = False
    sucide = False
    contraceptive = False
    others = False

    if jubilee_data_dict["which_disease"] == "congenital":
        congental = True
    elif jubilee_data_dict["which_disease"] == "infertility":
        infertility = True
    elif jubilee_data_dict["which_disease"] == "psychiatric":
        psychatric = True
    elif jubilee_data_dict["which_disease"] == "cosmetic":
        cosmetic = True
    elif jubilee_data_dict["which_disease"] == "suicide":
        sucide = True
    elif jubilee_data_dict["which_disease"] == "contraceptive":
        contraceptive = True
    elif jubilee_data_dict["which_disease"] == "others":
        others = True

    check_mark = "✓"
    company_name = jubilee_data_dict["company_name"]
    claimant_name = jubilee_data_dict["claimant_name"]
    claimant_father_name = jubilee_data_dict["claimant_father_name"]
    claimant_address = jubilee_data_dict["claimant_address"]
    raw = str(jubilee_data_dict["date_of_birth"]).replace("-", "")
    claimant_date_of_birth = raw[0] + "        " + raw[1] + "                 " + raw[2] + "        " + raw[3] + "                 " + raw[4] + "      " + raw[5] + "      " + raw[6] + "      " + raw[7]
    raw = str(jubilee_data_dict["cnic"]).replace("-", "")
    claimant_NIC = raw[0] + "        " + raw[1] + "        " + raw[2] + "        " + raw[3] + "        " + raw[4] + "                " + raw[5] + "       " + raw[6] + "       " + raw[7] + "       " + raw[8] + "       " + raw[9] + "       " + raw[10] + "       " + raw[11] + "                " + raw[12]
    policy_number = jubilee_data_dict["policy_number"]
    claimant_insured_ID = jubilee_data_dict["insurance_number"]
    claimant_phone_number = jubilee_data_dict["phone_number"]
    try:
        claimant_claim_amount = "{:,}".format(int(jubilee_data_dict["claim_amount"]))
    except ValueError:
        claimant_claim_amount = jubilee_data_dict["claim_amount"]
    claimant_sickness = jubilee_data_dict["illness"]
    symptoms_first_occur = jubilee_data_dict["symptoms_occur"]
    last_Working_day = jubilee_data_dict["last_working_day"]
    hospital_name = jubilee_data_dict["hospital_name"]
    hospital_address = jubilee_data_dict["hospital_address"]
    doctor_name = jubilee_data_dict["doctor_name"]
    required_exmaination_patient_address = jubilee_data_dict["patient_current_address"]
    any_other_insurance = jubilee_data_dict["another_insurance"]
    this_disease_continuation_of_old_disease = jubilee_data_dict["previous_treatment"]

    how_long_the_doctor_is_treating = jubilee_data_dict["how_long_patient_treatment"]
    surgical_or_obsterical_peformed = jubilee_data_dict["surgical"]
    detailed_treatement = jubilee_data_dict["treatment_detail"]
    same_disease_old_treatment = jubilee_data_dict["suffered_before"]

    expected_date_of_delivery = jubilee_data_dict["delivery_date"]
    reason_for_CSection = jubilee_data_dict["c_section"]
    first_consulted_for_maternity_date = jubilee_data_dict["first_maternity_visit"]

    # Page 1

    script_directory = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(script_directory, 'inpatient_form_2.pdf')
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[0]
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page.mediabox[2], page.mediabox[3]))
    can.setFont("Helvetica", 10)
    can.drawString(205, 725, company_name)
    can.drawString(205, 707, claimant_name)
    can.drawString(205, 668, claimant_father_name)
    can.drawString(205, 650, claimant_address)
    can.drawString(205, 632, claimant_name)
    can.drawString(205, 613, claimant_date_of_birth)
    can.setFont("Helvetica", 20)
    if female:
        can.drawString(545, 614, check_mark)
    else:
        can.drawString(488, 614, check_mark)
    can.setFont("Helvetica", 10)
    can.drawString(205, 594, claimant_NIC)
    can.drawString(205, 576, policy_number)
    can.drawString(360, 576, claimant_insured_ID)
    can.drawString(500, 576, claimant_phone_number)
    can.setFont("Helvetica", 20)
    can.drawString(202, 557, check_mark)
    can.setFont("Helvetica", 10)
    can.drawString(500, 557, claimant_claim_amount + "/-")
    can.drawString(205, 537, claimant_sickness)
    can.drawString(205, 500, symptoms_first_occur)
    can.drawString(205, 481, last_Working_day)
    can.drawString(205, 462, hospital_name)
    can.drawString(205, 424, hospital_address)
    can.drawString(205, 406, doctor_name)
    can.drawString(55, 367, required_exmaination_patient_address)
    can.drawString(55, 329, any_other_insurance)
    can.drawString(55, 294, this_disease_continuation_of_old_disease)
    can.save()

    packet.seek(0)
    output_pdf = PyPDF2.PdfWriter()
    new_pdf = PyPDF2.PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    output_pdf.add_page(page)
    output_file = open( os.path.join(script_directory, 'isu_page_1.pdf'), 'wb')
    output_pdf.write(output_file)
    pdf_file.close()
    output_file.close()


    # Page 2
    pdf_file_path = os.path.join(script_directory, 'inpatient_form_2.pdf')
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[1]
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page.mediabox[2], page.mediabox[3]))
    can.setFont("Helvetica", 10)
    can.drawString(205, 725, company_name)
    can.drawString(205, 707, claimant_name)
    can.drawString(205, 668, claimant_father_name)
    can.drawString(205, 650, claimant_address)
    can.drawString(205, 632, claimant_name)
    can.drawString(205, 613, claimant_date_of_birth)
    can.setFont("Helvetica", 20)
    if female:
        can.drawString(545, 614, check_mark)
    else:
        can.drawString(488, 614, check_mark)
    can.setFont("Helvetica", 10)
    can.drawString(205, 594, claimant_NIC)
    can.drawString(205, 576, policy_number)
    can.drawString(360, 576, claimant_insured_ID)
    can.drawString(500, 576, claimant_phone_number)
    can.setFont("Helvetica", 20)
    can.drawString(202, 557, check_mark)
    can.setFont("Helvetica", 10)
    can.drawString(500, 557, claimant_claim_amount + "/-")
    can.drawString(205, 537, claimant_sickness)
    can.drawString(205, 500, symptoms_first_occur)
    can.drawString(205, 481, last_Working_day)
    can.drawString(205, 462, hospital_name)
    can.drawString(205, 424, hospital_address)
    can.drawString(205, 406, doctor_name)
    can.drawString(55, 367, required_exmaination_patient_address)
    can.drawString(55, 329, any_other_insurance)
    can.drawString(55, 294, this_disease_continuation_of_old_disease)
    can.save()

    packet.seek(0)
    output_pdf = PyPDF2.PdfWriter()
    new_pdf = PyPDF2.PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    output_pdf.add_page(page)
    output_file = open(os.path.join(script_directory, 'isu_page_2.pdf'), 'wb')
    output_pdf.write(output_file)
    pdf_file.close()
    output_file.close()



    # Page 3
    pdf_file_path = os.path.join(script_directory, 'inpatient_form_2.pdf')
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[2]
    packet = io.BytesIO()


    can = canvas.Canvas(packet, pagesize=(page.mediabox[2], page.mediabox[3]))
    can.setFont("Helvetica", 10)
    can.drawString(210, 785, claimant_name)
    can.drawString(210, 765, how_long_the_doctor_is_treating)
    can.drawString(435, 748, symptoms_first_occur)
    can.drawString(60, 708, claimant_sickness)
    y = 667
    for line in add_linebreaks_text_box_accordingly(surgical_or_obsterical_peformed):
        can.drawString(58, y, line)
        y -= 10
    can.setFont("Helvetica", 20)
    if congental:
        can.drawString(55, 620, check_mark)
    if infertility:
        can.drawString(130, 620, check_mark)
    if psychatric:
        can.drawString(192, 620, check_mark)
    if cosmetic:
        can.drawString(286, 620, check_mark)
    if sucide:
        can.drawString(350, 620, check_mark)
    if contraceptive:
        can.drawString(403, 620, check_mark)
    if others:
        can.drawString(483, 620, check_mark)
    can.setFont("Helvetica", 10)
    # print(detailed_treatement)
    y = 590
    for line in add_linebreaks_text_box_accordingly(detailed_treatement):
        can.drawString(58, y, line)
        y -= 10
    can.drawString(60, 537, same_disease_old_treatment)
    can.drawString(295, 509, expected_date_of_delivery)
    can.drawString(295, 490, reason_for_CSection)
    can.drawString(295, 472, first_consulted_for_maternity_date)
    can.drawString(147, 434, doctor_name)
    can.save()


    packet.seek(0)
    output_pdf = PyPDF2.PdfWriter()
    new_pdf = PyPDF2.PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    output_pdf.add_page(page)
    output_file = open(os.path.join(script_directory, 'isu_page_3.pdf'), 'wb')
    output_pdf.write(output_file)
    pdf_file.close()
    output_file.close()

    input_file = os.path.join(script_directory, 'isu_page_1.pdf')
    output_file = os.path.join(script_directory, 'info_recieving.pdf')
    signature_file = os.path.join(script_directory, 'signature.png')
    water_mark_file = os.path.join(script_directory, 'watermark.png')

    file_handle = fitz.open(input_file)
    first_page = file_handle[0]

    page_width = first_page.rect.width
    page_height = first_page.rect.height
    image_width = 175  # Adjust the width of the image as needed
    image_height = 175  # Adjust the height of the image as needed

    x_left = 275
    x_right = x_left + image_width
    y_top = 470
    y_bottom = page_height

    # Define the position (bottom-center)
    image_rectangle = fitz.Rect(x_left, y_top, x_right, y_bottom)
    water_mark_rectangle = fitz.Rect(100, 0, x_right + 100, y_bottom)

    # Retrieve the first page of the PDF
    file_handle = fitz.open(input_file)
    first_page = file_handle[0]

    # Open the image file and read its binary data
    with open(signature_file, "rb") as image_file:
        image_data = image_file.read()
    first_page.insert_image(image_rectangle, stream=image_data)

    with open(water_mark_file, "rb") as image_file:
        info_data = image_file.read()
    first_page.insert_image(water_mark_rectangle, stream=info_data)

    file_handle.save(output_file)

    file_handle.close()

    pdf_file1 = open(os.path.join(script_directory, 'info_recieving.pdf'), "rb")
    pdf_file2 = open(os.path.join(script_directory, 'isu_page_2.pdf'), "rb")
    pdf_file3 = open(os.path.join(script_directory, 'isu_page_3.pdf'), "rb")

    # Create PDF readers for each file
    pdf_reader1 = PyPDF2.PdfReader(pdf_file1)
    pdf_reader2 = PyPDF2.PdfReader(pdf_file2)
    pdf_reader3 = PyPDF2.PdfReader(pdf_file3)

    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader1.pages)):
        page = pdf_reader1.pages[page_num]
        pdf_writer.add_page(page)

    for page_num in range(len(pdf_reader2.pages)):
        page = pdf_reader2.pages[page_num]
        pdf_writer.add_page(page)

    for page_num in range(len(pdf_reader3.pages)):
        page = pdf_reader3.pages[page_num]
        pdf_writer.add_page(page)

    merged_pdf = open(os.path.join(script_directory, 'inpatient_form_filled.pdf'), "wb")
    pdf_writer.write(merged_pdf)

    # Close the input and output files
    pdf_file1.close()
    pdf_file2.close()
    pdf_file3.close()
    merged_pdf.close()
    return "inpatient_form_filled.pdf"

