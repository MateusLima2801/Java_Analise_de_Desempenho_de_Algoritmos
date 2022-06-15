// import java.util.Scanner;
import java.io.*;
import java.util.concurrent.*;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Random;

class testCopyMatrix7000 {

    public static void main (String[] args) {

        long startTime;
        long estimatedTime;
        int n;

        // create a scanner so we can read the command-line input
        //Scanner scanner = new Scanner(System.in);

        // create instance of Random class
        Random rand = new Random();

        if (args.length > 0) {
            try {
                n = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.err.println("Argument" + args[0] + " must be an integer.");
                System.exit(1);
            }
        }

        n = 7000;
        //n = Integer.parseInt(args[0]);
        double A[][][]=new double[n][n][3];

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                for (int k=0;k<3;k++) {
                    A[i][j][k] = rand.nextDouble();
                }
            }
        }

        // System.out.println("Copy Matrix: "+n);

        startTime = System.currentTimeMillis();

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                A[i][j][0] = A[i][j][1];
                A[i][j][2] = A[i][j][0];
                A[i][j][1] = A[i][j][2];
            }
        }

        estimatedTime = System.currentTimeMillis() - startTime;
        NumberFormat formatter = new DecimalFormat("#00000.00000000");
        // System.out.println("    Time for matrix copy: " + formatter.format(estimatedTime  / 1000d) + " seconds");
        System.out.println("CopyMatrix7000 " + formatter.format(estimatedTime  / 1000d));

        try {
            File resultsLog = new File("java-results-log.txt");

            if(!resultsLog.exists()) resultsLog.createNewFile();

            FileWriter fw = new FileWriter(resultsLog.getName(), true);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write("CopyMatrix7000 " + formatter.format(estimatedTime  / 1000d));
            bw.newLine();

            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}

