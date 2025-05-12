#include <iostream>
#include <vector>
using namespace std;


class Course {
protected:
    string courseName;
    int maxSlots;
    int slotsFilled;

public:
    Course(string name = "Unknown", int slots = 30) {
        courseName = name;
        maxSlots = slots;
        slotsFilled = 0;
    }

    void displayCourse() {
        cout << "Course: " << courseName << endl;
        cout << "Slots Remaining: " << (maxSlots - slotsFilled) << endl;
    }

    bool registerSlot() {
        if (slotsFilled < maxSlots) {
            slotsFilled++;
            return true;
        } else {
            return false;
        }
    }

    string getCourseName() {
        return courseName;
    }

    int slotsLeft() {
        return maxSlots - slotsFilled;
    }
};

// Single Inheritance
class LabCourse : public Course {
public:
    LabCourse(string name = "LabCourse", int slots = 20) : Course(name, slots) {}
};

// Multilevel Inheritance
class AdvancedLabCourse : public LabCourse {
public:
    AdvancedLabCourse(string name = "Advanced Lab", int slots = 2) : LabCourse(name, slots) {}
};

// Hierarchical Inheritance
class TheoryCourse : public Course {
public:
    TheoryCourse(string name = "TheoryCourse", int slots = 40) : Course(name, slots) {}
};

// Hybrid Inheritance
class RegistrationPortal : public AdvancedLabCourse, public TheoryCourse {
private:
    vector<string> registeredStudents;

public:
    RegistrationPortal(string labName, string theoryName)
        : AdvancedLabCourse(labName), TheoryCourse(theoryName) {}

    void registerStudent(string studentName, string courseType) {
        cout << "\nRegistering student: " << studentName << " for " << courseType << "...\n";
        bool success = false;

        if (courseType == "Lab") {
            success = AdvancedLabCourse::registerSlot();
            if (success)
                registeredStudents.push_back(studentName + " | Registered: " + AdvancedLabCourse::getCourseName());
        } else if (courseType == "Theory") {
            success = TheoryCourse::registerSlot();
            if (success)
                registeredStudents.push_back(studentName + " | Registered: " + TheoryCourse::getCourseName());
        } else {
            cout << "Invalid course type.\n";
            return;
        }

        if (success)
            cout << "Registration Successful!\n";
        else
            cout << "Registration Failed: No slots remaining.\n";
    }

    void showRegisteredStudents() {
        cout << "\n--- Registered Students ---\n";
        for (string entry : registeredStudents) {
            cout << "Student: " << entry << endl;
        }
        cout << "Conflict Detected: None\n";
    }

    void showRemainingSlots() {
        cout << "\nLab Slots Left: " << AdvancedLabCourse::slotsLeft() << endl;
        cout << "Theory Slots Left: " << TheoryCourse::slotsLeft() << endl;
    }
};


void menu() {
    cout << "\n======= University Course Registration =======\n";
    cout << "1. Register a student\n";
    cout << "2. Show registered students\n";
    cout << "3. Show remaining slots\n";
    cout << "4. Exit\n";
    cout << "Enter your choice: ";
}


int main() {
    RegistrationPortal portal("Data Structures Lab", "Data Structures Theory");
    int choice;
    string name, type;

    while (true) {
        menu();
        cin >> choice;
        cin.ignore();

        switch (choice) {
            case 1:
                cout << "Enter student name: ";
                getline(cin, name);
                cout << "Enter course type (Lab or Theory): ";
                getline(cin, type);
                portal.registerStudent(name, type);
                break;
            case 2:
                portal.showRegisteredStudents();
                break;
            case 3:
                portal.showRemainingSlots();
                break;
            case 4:
                cout << "Exiting program. Goodbye!\n";
                return 0;
            default:
                cout << "Invalid choice. Try again.\n";
        }
    }

    return 0;
}
