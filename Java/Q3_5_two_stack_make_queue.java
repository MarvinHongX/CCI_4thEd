/* #########################################################################################
* Author  : Hong
* Created : 7/29/2022
* Modified: 7/29/2022
* Notes   : [3.5] Implement a MyQueue class which implements a queue using two stacks.
 ######################################################################################### */
public class Q3_5_two_stack_make_queue {
    private Stack stack1,stack2;
    public Q3_5_two_stack_make_queue(){
        stack1 = new Stack();
        stack2 = new Stack();
    }
    public void enqueue(String item){ stack1.push(item); }
    public void dequeue(){
        if (stack2.size() < 1){
            while (stack1.size() > 0){ stack2.push(stack1.pop()); }
        }
    }
    public void printListStack1(){ stack1.printList(); }
    public void printListStack2(){ stack2.printList(); }
}
/*
Q3_5_two_stack_make_queue q3_5_two_stack_make_queue = new Q3_5_two_stack_make_queue();

q3_5_two_stack_make_queue.enqueue("1");
q3_5_two_stack_make_queue.enqueue("2");
q3_5_two_stack_make_queue.enqueue("3");
q3_5_two_stack_make_queue.printListStack1();
q3_5_two_stack_make_queue.dequeue();
q3_5_two_stack_make_queue.printListStack1();
q3_5_two_stack_make_queue.printListStack2();
 */