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

    public double compute_average(int[] arr) {
        double avg = 0;
        for(int element : arr) {
            avg += element;
        }
        return avg/arr.length;
    }

    public void first_come_first_serve() {

        int temp[][] = this.times;

        Arrays.sort(temp, Comparator.comparingDouble(element -> element[0]));

        int[] completion_times = new int[n];
        int[] turn_around_times = new int[n];
        int[] waiting_times = new int[n];


        for(int i = 0; i < n; i++) {
            int[] current_process = temp[i];

            if(i == 0) {
                completion_times[i] = Math.addExact(current_process[0], current_process[1]);
            }
            else {
                int current_completion_time = completion_times[i - 1] + current_process[1];

                // Handling the case when the cpu is idle
                int idle_period = current_process[0] - completion_times[i - 1];
                if (idle_period > 0) {
                    current_completion_time += idle_period;
                }

                completion_times[i] = current_completion_time;
            }

            turn_around_times[i] = completion_times[i] - current_process[0];
            waiting_times[i] = turn_around_times[i] - current_process[1];
        }

        System.out.println("CT | TAT | WT");
        for(int i=0; i<this.n; i++) {
            System.out.print(completion_times[i] + " | " + turn_around_times[i] + " | " + waiting_times[i]);
            System.out.println();
        }
        System.out.println("Average Turn Around Time: " + this.compute_average(turn_around_times));
        System.out.println("Average Waiting Time: " + this.compute_average(waiting_times));
    }



    public static void main(String[] args) {
        FCFS demo = new FCFS();
        demo.first_come_first_serve();
    }
}