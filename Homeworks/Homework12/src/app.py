from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = 'students.csv'

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'first_name', 'last_name', 'age'])
        writer.writeheader()

def read_students():
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_students(students):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'first_name', 'last_name', 'age'])
        writer.writeheader()
        writer.writerows(students)

def generate_id():
    students = read_students()
    if not students:
        return 1
    return int(students[-1]['id']) + 1

@app.route('/students', methods=['GET'])
def get_all_students():
    students = read_students()
    return jsonify(students), 200

@app.route('/students/id/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    students = read_students()
    for student in students:
        if int(student['id']) == student_id:
            return jsonify(student), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/lastname/<string:last_name>', methods=['GET'])
def get_students_by_last_name(last_name):
    students = read_students()
    matched = [s for s in students if s['last_name'].lower() == last_name.lower()]
    if matched:
        return jsonify(matched), 200
    return jsonify({'error': 'No student found with that last name'}), 404

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    required = {'first_name', 'last_name', 'age'}
    if not data or not required.issubset(data.keys()) or any(k not in required for k in data.keys()):
        return jsonify({'error': 'Invalid fields or missing data'}), 400

    student = {
        'id': str(generate_id()),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'age': str(data['age'])
    }

    students = read_students()
    students.append(student)
    write_students(students)

    return jsonify(student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    required = {'first_name', 'last_name', 'age'}
    if not data or not required.issubset(data.keys()) or any(k not in required for k in data.keys()):
        return jsonify({'error': 'Invalid fields or missing data'}), 400

    students = read_students()
    for student in students:
        if int(student['id']) == student_id:
            student.update({
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'age': str(data['age'])
            })
            write_students(students)
            return jsonify(student), 200

    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['PATCH'])
def patch_student(student_id):
    data = request.get_json()
    if not data or 'age' not in data or len(data) > 1:
        return jsonify({'error': 'Invalid or missing age field'}), 400

    students = read_students()
    for student in students:
        if int(student['id']) == student_id:
            student['age'] = str(data['age'])
            write_students(students)
            return jsonify(student), 200

    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students = read_students()
    updated = [s for s in students if int(s['id']) != student_id]
    if len(updated) == len(students):
        return jsonify({'error': 'Student not found'}), 404
    write_students(updated)
    return jsonify({'message': f'Student with id {student_id} deleted successfully'}), 200

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

