package main;

import java.util.Scanner;
import login.*;
import booking.*;

public class RailwayReservationSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Login step
        Login log = new UserLogin();
        log.message();

        System.out.print("\nEnter Username: ");
        String username = sc.nextLine();
        System.out.print("Enter Password: ");
        String password = sc.nextLine();

        if (log.login(username, password)) {
            System.out.println("Signed in Successfully!");

            // Booking flow
            Ticket t = new Ticket();
            t.destination();
            System.out.println();
            t.selectTrain();
            t.selectQuota();
            t.numberOfPassengers();
            t.bookingConfirmation();

        } else {
            System.out.println("Login failed!");
        }

        sc.close();
    }
}
