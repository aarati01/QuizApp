import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')  # Change if your project folder has a different name
django.setup()

from quizapp.models import Question

questions = [
    {
        "question_text": "What does HTML stand for?",
        "option1": "Hyper Trainer Marking Language",
        "option2": "Hyper Text Marketing Language",
        "option3": "Hyper Text Markup Language",
        "option4": "Hyperlink Text Mark Language",
        "correct_option": 3
    },
    {
        "question_text": "Which tag is used to create a hyperlink in HTML?",
        "option1": "<a>",
        "option2": "<link>",
        "option3": "<href>",
        "option4": "<hyper>",
        "correct_option": 1
    },
    {
        "question_text": "Which property is used to change text color in CSS?",
        "option1": "font-color",
        "option2": "text-color",
        "option3": "color",
        "option4": "background-color",
        "correct_option": 3
    },
    {
        "question_text": "What does CSS stand for?",
        "option1": "Colorful Style Sheets",
        "option2": "Computer Style Sheets",
        "option3": "Cascading Style Sheets",
        "option4": "Creative Style Syntax",
        "correct_option": 3
    },
    {
        "question_text": "Which HTML element is used for the largest heading?",
        "option1": "<heading>",
        "option2": "<h6>",
        "option3": "<head>",
        "option4": "<h1>",
        "correct_option": 4
    },
    {
        "question_text": "Inside which HTML element do we put JavaScript?",
        "option1": "<js>",
        "option2": "<script>",
        "option3": "<javascript>",
        "option4": "<code>",
        "correct_option": 2
    },
    {
        "question_text": "How do you write a comment in CSS?",
        "option1": "// comment",
        "option2": "/* comment */",
        "option3": "<!-- comment -->",
        "option4": "# comment",
        "correct_option": 2
    },
    {
        "question_text": "Which attribute is used to provide an image path in HTML?",
        "option1": "src",
        "option2": "href",
        "option3": "link",
        "option4": "path",
        "correct_option": 1
    },
    {
        "question_text": "Which of the following is a JavaScript data type?",
        "option1": "number",
        "option2": "string",
        "option3": "boolean",
        "option4": "All of the above",
        "correct_option": 4
    },
    {
        "question_text": "Which method adds an element to the end of a JavaScript array?",
        "option1": "push()",
        "option2": "pop()",
        "option3": "shift()",
        "option4": "unshift()",
        "correct_option": 1
    },
    {
        "question_text": "Which tag is used to insert a line break in HTML?",
        "option1": "<br>",
        "option2": "<break>",
        "option3": "<lb>",
        "option4": "<newline>",
        "correct_option": 1
    },
    {
        "question_text": "How do you apply a class in HTML?",
        "option1": "class:",
        "option2": "css:",
        "option3": "class=",
        "option4": "style=",
        "correct_option": 3
    },
    {
        "question_text": "What does DOM stand for?",
        "option1": "Document Object Model",
        "option2": "Data Object Model",
        "option3": "Display Object Management",
        "option4": "Digital Ordinance Model",
        "correct_option": 1
    },
    {
        "question_text": "Which operator is used to assign a value in JavaScript?",
        "option1": "==",
        "option2": "=",
        "option3": "===",
        "option4": "!=",
        "correct_option": 2
    },
    {
        "question_text": "Which event occurs when the user clicks on an HTML element?",
        "option1": "onmouseclick",
        "option2": "onchange",
        "option3": "onclick",
        "option4": "onmouseover",
        "correct_option": 3
    },
    {
        "question_text": "Which CSS property controls the size of text?",
        "option1": "font-style",
        "option2": "text-size",
        "option3": "font-size",
        "option4": "text-style",
        "correct_option": 3
    },
    {
        "question_text": "How do you select an element with ID 'header' in CSS?",
        "option1": "#header",
        "option2": ".header",
        "option3": "header",
        "option4": "*header",
        "correct_option": 1
    },
    {
        "question_text": "Which tag is used to define a table row?",
        "option1": "<td>",
        "option2": "<th>",
        "option3": "<tr>",
        "option4": "<table>",
        "correct_option": 3
    },
    {
        "question_text": "Which HTML attribute specifies an alternate text for an image?",
        "option1": "title",
        "option2": "alt",
        "option3": "src",
        "option4": "name",
        "correct_option": 2
    },
    {
        "question_text": "How do you write 'Hello World' in an alert box in JavaScript?",
        "option1": "msg('Hello World');",
        "option2": "alertBox('Hello World');",
        "option3": "msgBox('Hello World');",
        "option4": "alert('Hello World');",
        "correct_option": 4
    }
]

for q in questions:
    Question.objects.create(
        text=q["question_text"],
        option1=q["option1"],
        option2=q["option2"],
        option3=q["option3"],
        option4=q["option4"],
        correct_option=q["correct_option"]
    )

print("✅ Successfully seeded 20 quiz questions!")
