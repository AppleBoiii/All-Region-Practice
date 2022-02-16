import java.io.*;
import java.util.*;
import java.nio.charset.Charset;
import java.nio.file.*;

public class Main3 {

    public static int convertToDecimal(int base, String number) {
        int total = 0;

        char[] chars = number.toCharArray();
        for(int i=0;i<chars.length;i++) {
            int y = Character.getNumericValue(chars[i]);       
            double x = Math.pow(base, chars.length-i-1);
            total += y * x; 
        }  

        return total;
    }

    public static String decimalToBase(int base, int number) {
        String res = "";

        while(number > 0) {
            res += number % base;
            number /= base;
        }
        

        return res;
    }

    public static String flipString(String s) {
        char[] arr = s.toCharArray();
        char[] arr2 = new char[arr.length];
        for(int i=0;i<arr.length;i++) {
            arr2[i] = arr[arr.length-i-1];
        }

        String ns = new String(arr2);

        return ns;
    }
    public static void main(String[] args) throws Exception {

        ArrayList<String> data = new ArrayList<String>();
        for (String line : Files.readAllLines(Paths.get("input.txt"), Charset.defaultCharset())) {

            data.add(line);
        }

        for(int i=0;i<data.size();i++){
            int base = Integer.parseInt(data.get(i).split(" ")[0]);
            String num = data.get(i).split(" ")[1];

            System.out.println("Input: "+base+" "+num);

            int decimal = convertToDecimal(base, num);

            int newBase = 3;
            if(base == newBase) newBase = 5;

            String converted_answer = decimalToBase(newBase, decimal);

            converted_answer = flipString(converted_answer);

            System.out.println("Output: "+newBase+" "+converted_answer+"\n");

        }
        
        

    }
}