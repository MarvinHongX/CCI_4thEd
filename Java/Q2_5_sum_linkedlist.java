/* #########################################################################################
* Author  : Hong
* Created : 7/28/2022
* Modified: 7/28/2022
* Notes   : [2.5] You have two numbers represented by a linked list, where each node contains a
*                single digit. The digits are stored in reverse order, such that the 1's digit is at the head
*                of the list. Write a function that adds the two numbers and returns the sum as a linked list.
*                FOLLOW UP
*                Suppose the digits are stored in forward order. Repeat the above problem.
 ######################################################################################### */
public class Q2_5_sum_linkedlist {
    private void addListsByNode(Node node1, Node node2, int carry, LinkedList result){
        int value = 0;
        value += carry;
        if (node1 != null) value += Integer.parseInt(node1.getVal());
        if (node2 != null) value += Integer.parseInt(node2.getVal());
        result.add(Integer.toString(value % 10));

        if (node1 != null || node2 != null) {
            addListsByNode(node1 == null ? null : node1.getNext(),
                            node2 == null ? null : node2.getNext(),
                            value >= 10 ? 1 : 0,
                            result);
        }
    }
    LinkedList addLists(LinkedList list1, LinkedList list2){
        if (list1 == null && list2 == null) return null;

        Node head1 = list1.getHead();
        Node head2 = list2.getHead();
        LinkedList result = new LinkedList();
        addListsByNode(head1, head2, 0, result);
        return result;
    }
}
/*
Q2_5_sum_linkedlist q2_5_sum_linkedlist = new Q2_5_sum_linkedlist();

LinkedList list1 = new LinkedList("7");
list1.add("1");
list1.add("6");
LinkedList list2 = new LinkedList("5");
list2.add("9");
list2.add("3");

LinkedList list3 = q2_5_sum_linkedlist.addLists(list1, list2);
list1.printListReverse();
list2.printListReverse();
list3.printListReverse();
 */
