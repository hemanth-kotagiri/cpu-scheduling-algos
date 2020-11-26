import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class FCFS {

    int n;
    int[][] times;

    public FCFS() {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter number of processess: ");
        n = scn.nextInt();
        times = new int[n][2];
        System.out.println("Arrival Time | Burst Time");
        for(int i = 0; i < this.n; i++){
            times[i][0] = scn.nextInt();
            times[i][1] = scn.nextInt();
        }

        scn.close();
    }

    public void show_processess() {

        for(int i = 0; i < this.n; i++){
            System.out.println(times[i][0] + "  " + times[i][1]);
        }
    }

    public void first_come_first_serve() {

        int temp[][] = this.times;

        Arrays.sort(temp, Comparator.comparingDouble(element -> element[0]));

        for(int i=0; i<this.n; i++) {
            System.out.print(temp[i][0] + " " + temp[i][1]);
            System.out.println();
        }
    }



    public static void main(String[] args) {
        FCFS demo = new FCFS();
        // demo.show_processess();
        demo.first_come_first_serve();
    }
}