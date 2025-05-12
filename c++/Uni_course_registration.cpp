#include <iostream>
#include <vector>
using namespace std;

class Student {
public:
    string name;
    int id;

    Student(string n, int i) {
        name = n;
        id = i;
    }
};

class Course {
private:
    string courseName;
    string courseCode;
    int maxCapacity;
    vector<Student> enrolledStudents;

public:
    Course(string name, string code, int capacity) {
        courseName = name;
        courseCode = code;
        maxCapacity = capacity;
    }

    void registerStudent(Student s) {
        if (enrolledStudents.size() < maxCapacity) {
            enrolledStudents.push_back(s);
            cout << s.name << " registered in " << courseName << endl;
        } else {
            cout << "Cannot register " << s.name << ". Course is full!" << endl;
        }
    }

    void displayStudents() {
        cout << "\nStudents enrolled in " << courseName << " (" << courseCode << "):\n";
        for (int i = 0; i < enrolledStudents.size(); i++) {
            cout << enrolledStudents[i].name << " (ID: " << enrolledStudents[i].id << ")\n";
        }
    }
};

int main() {
    int numCourses;
    cout << "Enter number of courses: ";
    cin >> numCourses;

    vector<Course> courses;

    for (int i = 0; i < numCourses; i++) {
        string cName, cCode;
        int capacity;

        cout << "\nEnter details for course " << i + 1 << ":\n";
        cout << "Course name: ";
        cin >> cName;
        cout << "Course code: ";
        cin >> cCode;
        cout << "Maximum capacity: ";
        cin >> capacity;

        Course c(cName, cCode, capacity);

        

        int numStudents;
        cout << "How many students do you want to register in " << cName << "? ";
        cin >> numStudents;

        for (int j = 0; j < numStudents; j++) {
            string sName;
            int sId;
            cout << "\nEnter name for student " << j + 1 << ": ";
            cin >> sName;
            cout << "Enter ID for student " << j + 1 << ": ";
            cin >> sId;

            Student s(sName, sId);
            c.registerStudent(s);
        }

        courses.push_back(c);
    }

    cout << "\n\n------ All courses and their enrolled students: ------ \n";

    for (int j = 0; j < numCourses; j++) {

        courses[j].displayStudents();
    }

    return 0;
}

