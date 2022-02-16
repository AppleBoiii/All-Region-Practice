import java.io.*;
import java.util.*;
import java.nio.charset.Charset;
import java.nio.file.*;


public class Main3 {
    public static void main(String[] args) throws Exception {
        File f = new File("input.txt");
        ArrayList<String> data = new ArrayList<String>();

        for(String line : Files.readAllLines(Paths.get("input.txt"), Charset.defaultCharset()) ) {
            data.add(line);
        }

        String s = data.toString();
        System.out.println(s);

    }
}