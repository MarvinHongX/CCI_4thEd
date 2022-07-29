/* #########################################################################################
* Author  : Hong
* Created : 7/29/2022
* Modified: 7/29/2022
* Notes   : [3.2] How would you design a stack which, in addition to push and pop, also has a
*                function min which returns the minimum element? Push, pop and min should all
*                operate in 0(1) time.
 ######################################################################################### */
class Stack{
    private Node last;
    private int size;
    public Stack(){
        last = null;
        size = 0;
    }
    public void push(String item){
        Node newNode = new Node(item);
        newNode.setNext(last);
        last = newNode;
        ++size;
    }

    public String pop(){
        String result = last.getVal();
        last = last.getNext();
        --size;
        return result;
    }

    public int size(){return size;}
    public Node getLast(){ return last; }
    public void printList(){
        Node buffer = this.last;
        StringBuilder sb = new StringBuilder();
        while (buffer != null){
            if (sb.length() > 0) sb.append(", ");

            sb.append(buffer.getVal());
            buffer = buffer.getNext();
        }
        System.out.println(sb.reverse().toString());
    }
}
public class Q3_2_stack_min extends Stack{}
/*
Q3_2_stack_min q3_2_stack_min = new Q3_2_stack_min();
q3_2_stack_min.push("1");
q3_2_stack_min.push("2");
q3_2_stack_min.push("3");
q3_2_stack_min.push("4");
q3_2_stack_min.printList();
System.out.println(q3_2_stack_min.pop());
q3_2_stack_min.printList();
System.out.println(q3_2_stack_min.pop());
q3_2_stack_min.printList();
 */
