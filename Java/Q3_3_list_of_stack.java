/* #########################################################################################
* Author  : Hong
* Created : 7/29/2022
* Modified: 7/29/2022
* Notes   : [3.3] Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
*                in real life, we would likely start a new stack when the previous stack exceeds some
*                threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
                Stacks should be composed of several stacks and should create a new stack once
*                the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.
*                pop() should behave identically to a single stack (that is, pop() should return the
*                same values as it would if there were just a single stack).
*                FOLLOW UP
*                Implement a function popAt(int index) which performs a pop operation on a
*                specific sub-stack.
 ######################################################################################### */
import java.util.ArrayList;
class SetOfStacks{
    protected int capacity;
    private ArrayList<Stack> stacks;

    public SetOfStacks(){
        this.capacity = 10;
        stacks = new ArrayList<Stack>();
    }

    public SetOfStacks(int capacity){
        this.capacity = capacity;
        stacks = new ArrayList<Stack>();
    }
    private Stack getLastStack(){
        if (stacks.size() == 0) return null;
        return stacks.get(stacks.size() - 1);
    }
    public void push(String item){
       Stack last = getLastStack();
       if (last != null && (last.size() < capacity)){
           last.push(item);
       }else{
            Stack newStack = new Stack();
            newStack.push(item);
            stacks.add(newStack);
       }
    }
    public String pop(){
        Stack last = getLastStack();
        if (last == null) return null;

        String result = last.pop();
        if (last.size() == 0) stacks.remove(stacks.size() - 1);
        return result;
    }
    public void printList(){
        for (int i = 0; i < stacks.size(); ++i){ stacks.get(i).printList(); }
    }
}

public class Q3_3_list_of_stack extends SetOfStacks{
    public Q3_3_list_of_stack(int capacity){super.capacity = capacity;}
}
/*
Q3_3_list_of_stack q3_3_list_of_stack = new Q3_3_list_of_stack(3);
q3_3_list_of_stack.push("1");
q3_3_list_of_stack.push("2");
q3_3_list_of_stack.push("3");
q3_3_list_of_stack.push("4");
q3_3_list_of_stack.push("5");
q3_3_list_of_stack.printList();
System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();
System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();

System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();
System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();
System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();
System.out.println(q3_3_list_of_stack.pop());
q3_3_list_of_stack.printList();
 */