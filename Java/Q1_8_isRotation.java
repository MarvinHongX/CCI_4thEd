/* #########################################################################################
* Author  : Hong
* Created : 7/22/2022
* Modified: 7/22/2022
* Notes   : [1.8] Assume you have a method isSubstring which checks if one word is a substring
*                of another. Given two strings, s1 and s2, write code to check If s2 is a rotation of s1
*                using only onecalltoisSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
 ######################################################################################### */
public class Q1_8_isRotation {
    boolean isRotation(String str1, String str2){
        if (str1 == null || str1.isEmpty() || str2 == null || str2.isEmpty()) return false;
        if (str1.length() != str2.length()) return false;

        StringBuilder buffer = new StringBuilder();
        buffer.append(str1);
        buffer.append(str1);

        return isSubstring(buffer.toString(), str2);
    }
    private boolean isSubstring(String str1, String str2){
        return str1.contains(str2);
    }

}
/*
Q1_8_isRotation q1_8_isRotation = new Q1_8_isRotation();
System.out.println(q1_8_isRotation.isRotation("isRotation", "Rotationsi"));
System.out.println(q1_8_isRotation.isRotation("waterbottLe", "erbottLewat"));
 */
