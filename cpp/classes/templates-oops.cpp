// Generic function template
template <typename T>
T add(T a, T b) {
    return a + b;
}

// Generic class template
template <typename T>
class Container {
private:
    T element;
public:
    void setElement(T arg) { element = arg; }
    T getElement() { return element; }
};

int main() {
    // Using the template function with different types
    int intSum = add(5, 3);           // Works with integers
    double doubleSum = add(3.14, 2.0); // Works with doubles

    // Using the template class
    Container<int> intContainer;
    intContainer.setElement(42);
    
    Container<std::string> stringContainer;
    stringContainer.setElement("Hello");

    return 0;
}