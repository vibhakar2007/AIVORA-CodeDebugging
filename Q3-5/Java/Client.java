import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String host = ""; //Find the IP
        int port = 5002;

        try (Socket socket = new Socket(host, port);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            String message = "Top Secret Message!";
            out.println(message);
            System.out.println("Message sent to server.");

        } catch (IOException) {
            e.printStackTrace();
        }
    }
}