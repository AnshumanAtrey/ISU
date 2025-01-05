class Person {
    // Private members (default access specifier is private)
    // These cannot be accessed directly from outside the class
private:
    std::string socialSecurityNumber; // Sensitive data kept private
    double salary;                    // Internal financial information

    // Private method - can only be called from within the class
    void validatePersonalInfo() {
        // Internal validation logic
        // Cannot be accessed from outside the class
    }

    // Public members - accessible from anywhere the object is visible
public:
    // Constructor
    Person(std::string name, int age) : 
        name(name),    // Initializing public member
        age(age)       // Initializing public member
    {}

    // Public methods - can be called from outside the class
    void displayInfo() {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
        
        // Can access private members within the class
        validatePersonalInfo();
    }

    // Getter method - controlled access to private data
    std::string getName() const {
        return name;
    }

    // Setter method with validation
    void setAge(int newAge) {
        if (newAge > 0 && newAge < 150) {
            age = newAge;
        }
    }

    // Public members
    std::string name;  // Can be directly accessed
    int age;           // Can be directly accessed
};

int main() {
    Person person("John Doe", 30);

    // Public members can be accessed directly
    person.name = "Jane Doe";  // Allowed
    person.displayInfo();      // Allowed

    // Private members cannot be accessed
    // person.socialSecurityNumber = "123-45-6789";  // Compilation ERROR
    // person.validatePersonalInfo();                // Compilation ERROR

    return 0;
}