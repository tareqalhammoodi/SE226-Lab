//SE226 – LAB#3
#include <iostream>
using namespace std;
//Node class
class Node {
public:
    int data;
    Node *next;
    Node(int Data) {
        data = Data;
        next = nullptr;
    }
};

//Queue class
class Queue {
private:
    Node *front; //create front Node
    Node *back; //create back Node
    int size;   //hold the size of the queue
public:
    Queue() {
        front = nullptr;
        back = nullptr;
        size = 0;
    }

    //Add element to the queue
    void enqueue(int Data) {
        Node *newNode = new Node(Data);

        if (back == nullptr) {
            front = newNode;
            back = newNode;
        }
        else {
            back -> next = newNode;
            back = newNode;
        }

        size++;
    }

    //Remove element from the queue
    void dequeue() {
        if (isEmpty()) {
            cout << "Not: Queue is empty." << endl;
            return;
        }
        Node *tempElement = front;
        front = front -> next;
        if (front == nullptr) {
            back = nullptr;
        }
        delete tempElement;
        size--;
    }

    //Get value of top element in queue
    int top() {
        if (isEmpty()) {
            cout << "Not: Queue is empty." << endl;
            return -1;
        }
        return front -> data;
    }

    //Print contents of queue
    void print() {
        if (isEmpty()) {
            cout << "Not: Queue is empty." << endl;
            return;
        }
        Node *tempElement = front;
        while (tempElement != nullptr) {
            cout << tempElement -> data << " | ";
            tempElement = tempElement -> next;
        }
        cout << endl;
    }

    //Check if queue is empty
    bool isEmpty() {
        return front == nullptr;
    }

    //Check size of queue
    int Size() {
        return size;
    }
};

int main() {
    Queue queue;

    //Add elements to the queue
    queue.enqueue(3);
    queue.enqueue(7);
    queue.enqueue(4);
    queue.enqueue(12);
    queue.enqueue(20);
    queue.enqueue(1);

    //Print the queue
    cout << "Elements of the queue : ";
    queue.print();
    //Print size of queue
    cout << "Queue size: " << queue.Size() << endl;
    //Print top element of the queue
    cout << "Top element: " << queue.top() << endl;

    cout<<"--------------------------------------------------------" << endl;

    //Remove an element from the queue
    queue.dequeue();

    //Print the queue
    cout << "Elements of the queue : ";
    queue.print();
    //Print size of queue
    cout << "Queue size: " << queue.Size() << endl;
    //Print top element of the queue
    cout << "Top element: " << queue.top() << endl;

    cout<<"--------------------------------------------------------" << endl;

    //Remove two elements from the queue
    queue.dequeue();
    queue.dequeue();

    //Print the queue
    cout << "Elements of the queue : ";
    queue.print();
    //Print size of queue
    cout << "Queue size: " << queue.Size() << endl;
    //Print top element of the queue
    cout << "Top element: " << queue.top() << endl;

    cout<<"--------------------------------------------------------" << endl;

    return 0;
}
