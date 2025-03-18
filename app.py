from flask import Flask,jsonify

todo = Flask('__name__')

students = [
        {
            'id':1,
            'student_name': 'std1',
            'age':21,
            'email':'trs@gmail.com'
        },
        {
            'id':2,
            'student_name': 'std12',
            'age': 22,
            'email': 'smd@gmail.com'
        },
        {
            'id':3,
            'student_name': 'std3',
            'age': 21,
            'email': 'trs2@gmail.com'
        }
]
@todo.route('/students-list')
def students_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>',methods=['GET'])
def student_id(id):
    student=next((student for student in students if student['id']==id),None)

    if student is None:
        return jsonify({'message':'Student not found'}),404

    return jsonify(student)

@todo.route('/students-api')
def student_api():
    import requests

    url = "https://rest-api-1-03f4.onrender.com/students-list"

    response = requests.request(method="GET", url=url)

    return response.json()



if __name__== "__main__":
    todo.run(
    
        debug=True
    )
