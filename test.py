# from fpdf import FPDF
# #import smtplib
# from tkinter import Tk, Label, Entry, Button

# # List to store questions
# questions = []

# def add_question(question_text, options, supplementary_materials):
#     questions.append({
#         'question_text': question_text,
#         'options': options,
#         'supplementary_materials': supplementary_materials
#     })

# def generate_question_paper(num_questions):
#     pdf = FPDF()
#     pdf.add_page()
#     # Logic to fetch questions from list and add them to PDF
#     # You need to implement this logic
#     pdf.output("question_paper.pdf")

# # Function to handle GUI for adding questions
# def add_question_gui():
#     def submit_question(question_entry, options_entry, supplementary_entry):
#         question_text = question_entry.get()
#         options = options_entry.get()
#         supplementary_materials = supplementary_entry.get()
#         add_question(question_text, options, supplementary_materials)
#         # Optionally clear the entry fields after submission
#         question_entry.delete(0, 'end')
#         options_entry.delete(0, 'end')
#         supplementary_entry.delete(0, 'end')

#     root = Tk()
#     root.title("Add Question")

#     question_label = Label(root, text="Question Text:")
#     question_label.pack()
#     question_entry = Entry(root)
#     question_entry.pack()

#     options_label = Label(root, text="Options (if any):")
#     options_label.pack()
#     options_entry = Entry(root)
#     options_entry.pack()

#     supplementary_label = Label(root, text="Supplementary Materials (e.g., graph, table, diagram):")
#     supplementary_label.pack()
#     supplementary_entry = Entry(root)
#     supplementary_entry.pack()

#     submit_button = Button(root, text="Submit", command=submit_question)
#     submit_button.pack()
#     root.mainloop()


from fpdf import FPDF
from tkinter import Tk, Label, Entry, Button, filedialog

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automatic Question Paper', 0, 1, 'C')
        self.ln(10)

    def section_title(self, section, marks):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Section {section} ({marks} marks)', 0, 1)
        self.ln(5)

    def question(self, question_text, options, supplementary_materials):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, f'Q: {question_text}')
        if options:
            self.set_font('Arial', 'I', 12)
            self.multi_cell(0, 10, f'Options: {options}')
        if supplementary_materials:
            self.image(supplementary_materials, x=10, w=100)
        self.ln(10)

questions = []

def add_question(question_text, options, supplementary_materials, section, marks):
    questions.append({
        'question_text': question_text,
        'options': options,
        'supplementary_materials': supplementary_materials,
        'section': section,
        'marks': marks
    })

def generate_question_paper():
    pdf = PDF()
    pdf.add_page()
    
    current_section = ""
    
    for question in questions:
        if question['section'] != current_section:
            current_section = question['section']
            pdf.section_title(current_section, question['marks'])
        
        pdf.question(question['question_text'], question['options'], question['supplementary_materials'])
    
    pdf.output('question_paper.pdf')
    print("Question paper generated successfully!")

def add_question_gui():
    def submit_question():
        question_text = question_entry.get()
        options = options_entry.get()
        supplementary_materials = supplementary_entry.get()
        section = section_entry.get()
        marks = marks_entry.get()
        add_question(question_text, options, supplementary_materials, section, marks)
        question_entry.delete(0, 'end')
        options_entry.delete(0, 'end')
        supplementary_entry.delete(0, 'end')
        section_entry.delete(0, 'end')
        marks_entry.delete(0, 'end')

    def upload_image():
        filename = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        supplementary_entry.delete(0, 'end')
        supplementary_entry.insert(0, filename)

    root = Tk()
    root.title("Add Question")

    Label(root, text="Question Text:").pack()
    question_entry = Entry(root)
    question_entry.pack()

    Label(root, text="Options (if any):").pack()
    options_entry = Entry(root)
    options_entry.pack()

    Label(root, text="Supplementary Materials (e.g., graph, table, diagram):").pack()
    supplementary_entry = Entry(root)
    supplementary_entry.pack()
    Button(root, text="Upload Image", command=upload_image).pack()

    Label(root, text="Section:").pack()
    section_entry = Entry(root)
    section_entry.pack()

    Label(root, text="Marks:").pack()
    marks_entry = Entry(root)
    marks_entry.pack()

    submit_button = Button(root, text="Submit", command=submit_question)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    add_question_gui()
    generate_question_paper()
    print("Question paper generated successfully!")
