import java.util.Scanner;
import java.io.*;
import java.util.concurrent.*;
import java.text.DecimalFormat;
import java.text.NumberFormat;

class testLookAndSay40 {

    public static void main (String args[]) {
        int n;
        long a;
        long b;
        long startTime;
        long estimatedTime;

        NumberFormat formatter = new DecimalFormat("#00000.00000000");

        if (args.length > 0) {
            try {
                n = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.err.println("Argument" + args[0] + " must be an integer.");
                System.exit(1);
            }
        }

        n = 40;
        //n = Integer.parseInt(args[0]);

        // System.out.println("Look and say sequence: "+n);
        startTime = System.nanoTime();
 
        String num = "1223334444";
    for (int i=2;i<=n;i++) {
        num = lookandsayseq(num);             
    }
    //System.out.println(num);

        estimatedTime = System.nanoTime() - startTime;
        System.out.println("LookAndSay40 " + formatter.format(estimatedTime  / 1000000000d));

        try {
            File resultsLog = new File("java-results-log.txt");

            if(!resultsLog.exists()) resultsLog.createNewFile();

            FileWriter fw = new FileWriter(resultsLog.getName(), true);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write("LookAndSay40 " + formatter.format(estimatedTime  / 1000000000d));
            bw.newLine();

            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static String lookandsayseq(String number)
    {
        StringBuilder result= new StringBuilder();
     
        char repeat= number.charAt(0);
        number= number.substring(1) + " ";
        int times= 1;
     
        for (char actual: number.toCharArray())
        {
           if (actual != repeat)
           {
              result.append(times + "" + repeat);
              times= 1;
              repeat= actual;
           }
           else
           {
              times+= 1;
           }
        }
        return result.toString();
    }

}
