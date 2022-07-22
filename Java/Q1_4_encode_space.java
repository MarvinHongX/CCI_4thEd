/* #########################################################################################
* Author  : Hong
* Created : 7/19/2022
* Modified: 7/19/2022
* Notes   : [1.4] Write a method to replace all spaces in a string with'%20'. You may assume that
*                the string has sufficient space at the end of the string to hold the additional
*                characters, and that you are given the "true" length of the string.
*                (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
*                EXAMPLE
*                Input: "Mr John Smith"
*                Output: "Mr%20John%20Smith"
 ######################################################################################### */
public class Q1_4_encode_space {
    void encode_space(char[] str, int length){
        int spaceCount = 0;

        for (char ch : str) {
            if (ch == ' ') spaceCount++;
        }

        int newLength = length + (2 * spaceCount);
        --newLength;
        for (int i = length - 1; i >= 0; --i) {
            if (str[i] == ' ') {
                str[newLength--] = '0';
                str[newLength--] = '2';
                str[newLength--] = '%';
            } else {
                str[newLength--] = str[i];
            }
        }
    }
}
/*
Q1_4_encode_space q1_4_encode_space = new Q1_4_encode_space();
char[] str1 = "How you do? \0\0\0\0\0\0".toCharArray();
char[] str2 = "Mr John Smith0\0\0\0".toCharArray();
q1_4_encode_space.encode_space(str1,12);
q1_4_encode_space.encode_space(str2,13);
System.out.println(str1);
System.out.println(str2);
 */
