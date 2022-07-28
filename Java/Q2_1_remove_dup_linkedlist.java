/* #########################################################################################
* Author  : Hong
* Created : 7/27/2022
* Modified: 7/27/2022
* Notes   : [2.1] Write code to remove duplicates from an unsorted linked list.
*                FOLLOW UP
*                How would you solve this problem if a temporary buffer is not allowed?
 ######################################################################################### */

 class Node{
     private String val;
     private Node next = null;
     public Node(String item){ val = item; }
     public String getVal(){ return this.val;}
     public Node getNext(){ return this.next;}
     public void setNext(Node newNext){ this.next = newNext;}
     public boolean isEmpty(){
         return (val.isEmpty() || val == null) ? true : false;
     }
}
class LinkedList{
    private Node head;
    public LinkedList(){
        head = null;
    }
    public LinkedList(String item){
        head = new Node(item);
    }
    public void add(String item){
        Node newNode = new Node(item);
        if (head == null){
            this.head = newNode;
        }else{
            Node n = this.head;
            while(n.getNext() != null){
                n = n.getNext();
            }
            n.setNext(newNode);
        }
    }
    public void printList(){
        Node buffer = this.head;
        StringBuilder sb = new StringBuilder();
        while (buffer != null){
            if (sb.length() > 0) sb.append(", ");

            sb.append(buffer.getVal());
            buffer = buffer.getNext();
        }
        System.out.println(sb.toString());
    }
    public void printListReverse(){
        Node buffer = this.head;
        StringBuilder sb = new StringBuilder();
        while (buffer != null){
            if (sb.length() > 0) sb.append(", ");

            sb.append(buffer.getVal());
            buffer = buffer.getNext();
        }
        System.out.println(sb.reverse().toString());
    }
    public Node getHead(){ return this.head;}
}
public class Q2_1_remove_dup_linkedlist {
    void removeDuplicate(LinkedList list){
        if (list == null) return;
        if (list.getHead() == null) return;

        Node walker = list.getHead();
        while (walker.getNext() != null){
            Node runner = list.getHead();
            while (runner != null) {
                if (runner == walker.getNext()) {
                    walker = walker.getNext();
                    break;
                }
                if (runner.getVal() == walker.getNext().getVal()){
                    walker.setNext(walker.getNext().getNext());
                    break;
                }

                runner = runner.getNext();
            }
        }
    }
}
/*
Q2_1_remove_dup_linkedlist q2_1_remove_dup_linkedlist = new Q2_1_remove_dup_linkedlist();

LinkedList list = new LinkedList("1");
list.add("1");
list.add("3");
list.add("5");
list.add("7");
list.add("3");
list.add("4");
list.add("5");
list.add("1");
list.printList();
q2_1_remove_dup_linkedlist.removeDuplicate(list);
list.printList();
 */