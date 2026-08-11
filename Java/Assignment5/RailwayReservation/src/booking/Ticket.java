package booking;

import java.util.Scanner;

public class Ticket extends Booking {
    private Integer trainChoice, numberOfPassengers;
    private Character selectQuota;
    private String from, to, trainName;
    private Scanner sc = new Scanner(System.in);

    @Override
    public void destination() {
        System.out.print("Departure: ");
        from = sc.nextLine();
        System.out.print("Arrival: ");
        to = sc.nextLine();
        System.out.println("Getting results for " + from + " to " + to + "...");
    }

    @Override
    public void selectTrain() {
        System.out.println("Available Trains to " + to);
        System.out.println("1. Rajdhani Express");
        System.out.println("2. Shatabdi Express");
        System.out.println("3. Duronto Express");
        System.out.println("4. Garib Rath Express");
        System.out.println("5. Humsafar Express");
        System.out.print("Enter Train number (1 to 5): ");
        trainChoice = sc.nextInt();
        sc.nextLine();

        if (trainChoice < 1 || trainChoice > 5) {
            System.out.println("Invalid train choice. Program will now exit.");
            System.exit(0);
        }

        switch (trainChoice) {
            case 1:
                trainName = "Rajdhani Express";
                break;
            case 2:
                trainName = "Shatabdi Express";
                break;
            case 3:
                trainName = "Duronto Express";
                break;
            case 4:
                trainName = "Garib Rath Express";
                break;
            case 5:
                trainName = "Humsafar Express";
                break;
        }
        System.out.println("Selected: " + trainName);
    }

    @Override
    public void selectQuota() {
        System.out.println("Available quota:");
        System.out.println("a. Reservation");
        System.out.println("b. General");
        System.out.println("c. Tatkaal");
        System.out.println("d. Ladies");
        System.out.print("Enter Quota choice (a to d): ");
        selectQuota = sc.next().charAt(0);
        sc.nextLine();

        if (selectQuota != 'a' && selectQuota != 'b' && selectQuota != 'c' && selectQuota != 'd') {
            System.out.println("Invalid quota choice. Program will now exit.");
            System.exit(0);
        }

        switch (selectQuota) {
            case 'a':
                System.out.println("Reservation");
                break;
            case 'b':
                System.out.println("General");
                break;
            case 'c':
                System.out.println("Tatkaal");
                break;
            case 'd':
                System.out.println("Ladies");
                break;
        }
    }

    @Override
    public void numberOfPassengers() {
        System.out.print("Enter number of passengers: ");
        numberOfPassengers = sc.nextInt();
        sc.nextLine();

        if (numberOfPassengers <= 0) {
            System.out.println("Invalid number of passengers. Program will now exit.");
            System.exit(0);
        }
    }

    @Override
    public void bookingConfirmation() {
        System.out.println("\n------ Booking confirmation --------");
        System.out.println("Your Booking Has Been Confirmed!");
        System.out.println(from.toUpperCase() + " to " + to.toUpperCase());
        System.out.println("Train: " + trainName.toUpperCase());
        System.out.println("Quota: " + selectQuota);
        System.out.println("Number of passengers: " + numberOfPassengers);
    }
}