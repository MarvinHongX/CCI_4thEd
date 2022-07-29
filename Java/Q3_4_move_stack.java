/* #########################################################################################
* Author  : Hong
* Created : 7/29/2022
* Modified: 7/29/2022
* Notes   : [3.4] In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
*                different sizes which can slide onto any tower. The puzzle starts with disks sorted
*                in ascending order of size from top to bottom (i.e., each disk sits on top of an even
*                larger one). You have the following constraints:
*                (1) Only one disk can be moved at a time.
*                (2) A disk is slid off the top of one tower onto the next rod.
*                (3) A disk can only be placed on top of a larger disk.
*                Write a program to move the disks from the first tower to the last using Stacks.
*                (Tower of Hanoi)
 ######################################################################################### */
class Tower{
    protected Stack disks;
    public Tower(){
        disks = new Stack();
    }
    public Tower(int i){
        disks = new Stack();
    }
    public void add(int item){
        if (disks == null) return;
        if (disks.size() > 0 && Integer.parseInt(disks.getLast().getVal()) <= item){
            System.out.println("Error placing disk " + item);
        } else {
            disks.push(Integer.toString(item));
        }
    }
    private void moveTopTo(Tower target){
        String last = disks.pop();
        target.add(Integer.parseInt(last));
    }
    public void moveDisk(int n, Tower target, Tower buffer){
        if (n > 0){
            moveDisk(n - 1, buffer, target); //n-1 disks to buffer
            moveTopTo(target); //nth disk to target
            buffer.moveDisk(n - 1, target, this); // buffer to target
        }
    }
    public int size(){ return disks.size(); }
    public void printList(){ disks.printList(); }
}
public class Q3_4_move_stack extends Tower{

}
/*
Q3_4_move_stack towerA = new Q3_4_move_stack();
Q3_4_move_stack towerB = new Q3_4_move_stack();
Q3_4_move_stack towerC = new Q3_4_move_stack();
towerA.add(5);
towerA.add(4);
towerA.add(3);
towerA.add(2);
towerA.add(1);
towerA.printList();
towerA.moveDisk(towerA.size(), towerB, towerC);
towerA.printList();
towerB.printList();
towerC.printList();
 */