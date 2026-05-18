import random

topics = {

    "Python": [

        {
            "question": "What is Python?",
            "correct": "Programming Language",
            "wrong": ["Snake", "Browser", "Game"]
        },

        {
            "question": "Which keyword creates function?",
            "correct": "def",
            "wrong": ["fun", "create", "function"]
        },

        {
            "question": "Which symbol is comment?",
            "correct": "#",
            "wrong": ["//", "--", "/*"]
        },

        {
            "question": "Which datatype stores text?",
            "correct": "str",
            "wrong": ["int", "float", "bool"]
        },

        {
            "question": "Which loop repeats code?",
            "correct": "for",
            "wrong": ["repeat", "loop", "again"]
        },

        {
            "question": "Which function prints output?",
            "correct": "print()",
            "wrong": ["echo()", "show()", "display()"]
        },

        {
            "question": "Which operator checks equality?",
            "correct": "==",
            "wrong": ["=", "!=", ">="]
        },

        {
            "question": "Which keyword is conditional?",
            "correct": "if",
            "wrong": ["when", "check", "case"]
        },

        {
            "question": "Which collection uses [] ?",
            "correct": "List",
            "wrong": ["Tuple", "Set", "Dictionary"]
        },

        {
            "question": "Python creator?",
            "correct": "Guido van Rossum",
            "wrong": ["Elon Musk", "James Gosling", "Dennis Ritchie"]
        }

    ],


    "Java": [

        {
            "question": "Java was developed by?",
            "correct": "James Gosling",
            "wrong": ["Dennis Ritchie", "Guido van Rossum", "Elon Musk"]
        },

        {
            "question": "Java is which type language?",
            "correct": "Object Oriented",
            "wrong": ["Markup", "Database", "Assembly"]
        },

        {
            "question": "Which keyword creates object?",
            "correct": "new",
            "wrong": ["create", "make", "class"]
        },

        {
            "question": "Which method starts Java program?",
            "correct": "main()",
            "wrong": ["start()", "run()", "execute()"]
        },

        {
            "question": "Java source file extension?",
            "correct": ".java",
            "wrong": [".py", ".cpp", ".exe"]
        },

        {
            "question": "Which package is imported automatically?",
            "correct": "java.lang",
            "wrong": ["java.io", "java.util", "java.sql"]
        },

        {
            "question": "Java is platform?",
            "correct": "Independent",
            "wrong": ["Dependent", "Hardware", "OS"]
        },

        {
            "question": "Which loop is entry controlled?",
            "correct": "for",
            "wrong": ["do while", "goto", "switch"]
        },

        {
            "question": "Java uses which memory cleanup?",
            "correct": "Garbage Collection",
            "wrong": ["Delete", "Destructor", "Cleaner"]
        },

        {
            "question": "Which keyword inherits class?",
            "correct": "extends",
            "wrong": ["inherits", "implements", "super"]
        }

    ],


    "DBMS": [

        {
            "question": "DBMS stands for?",
            "correct": "Database Management System",
            "wrong": ["Data Backup Management System", "Digital Base Management", "Data Building System"]
        },

        {
            "question": "Which language is used in DBMS?",
            "correct": "SQL",
            "wrong": ["HTML", "Python", "C"]
        },

        {
            "question": "Which key uniquely identifies record?",
            "correct": "Primary Key",
            "wrong": ["Foreign Key", "Candidate Key", "Super Key"]
        },

        {
            "question": "Which normal form removes partial dependency?",
            "correct": "2NF",
            "wrong": ["1NF", "3NF", "BCNF"]
        },

        {
            "question": "Which command removes table?",
            "correct": "DROP",
            "wrong": ["DELETE", "REMOVE", "CLEAR"]
        },

        {
            "question": "Which clause filters rows?",
            "correct": "WHERE",
            "wrong": ["GROUP", "ORDER", "SELECT"]
        },

        {
            "question": "Which join returns all records?",
            "correct": "FULL JOIN",
            "wrong": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN"]
        },

        {
            "question": "DBMS reduces?",
            "correct": "Data Redundancy",
            "wrong": ["Speed", "Security", "Memory"]
        },

        {
            "question": "Which SQL command adds data?",
            "correct": "INSERT",
            "wrong": ["ADD", "PUT", "CREATE"]
        },

        {
            "question": "Which database is relational?",
            "correct": "MySQL",
            "wrong": ["MongoDB", "Redis", "Firebase"]
        }

    ],


    "DSA": [

        {
            "question": "DSA stands for?",
            "correct": "Data Structures and Algorithms",
            "wrong": ["Digital System Algorithm", "Data Science Algorithm", "Data Search Analysis"]
        },

        {
            "question": "Which structure uses FIFO?",
            "correct": "Queue",
            "wrong": ["Stack", "Tree", "Graph"]
        },

        {
            "question": "Which structure uses LIFO?",
            "correct": "Stack",
            "wrong": ["Queue", "Array", "Linked List"]
        },

        {
            "question": "Binary Search works on?",
            "correct": "Sorted Array",
            "wrong": ["Linked List", "Tree", "Graph"]
        },

        {
            "question": "Time complexity of Binary Search?",
            "correct": "O(log n)",
            "wrong": ["O(n)", "O(n2)", "O(1)"]
        },

        {
            "question": "Which traversal uses root-left-right?",
            "correct": "Preorder",
            "wrong": ["Postorder", "Inorder", "Levelorder"]
        },

        {
            "question": "Which data structure stores nodes?",
            "correct": "Linked List",
            "wrong": ["Array", "Stack", "Queue"]
        },

        {
            "question": "Which algorithm finds shortest path?",
            "correct": "Dijkstra",
            "wrong": ["DFS", "Bubble Sort", "Selection Sort"]
        },

        {
            "question": "Merge Sort complexity?",
            "correct": "O(n log n)",
            "wrong": ["O(n2)", "O(log n)", "O(1)"]
        },

        {
            "question": "Tree with one root?",
            "correct": "Binary Tree",
            "wrong": ["Graph", "Queue", "Stack"]
        }

    ]

}


def generate_questions(topic):

    return topics.get(topic, [])