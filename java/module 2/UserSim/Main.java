import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;


public class Main {

    private static Robot robot;

    public static void main(String[] args) {

        try {
            robot = new Robot();
        } catch (Exception e) {
            System.out.println("Robot is not created");
        }

        JFrame window = new JFrame();
        window.setUndecorated(true);
        window.setAlwaysOnTop(true);
        window.setLocation(0, 0);
        window.setLayout(new FlowLayout());

        JButton[] buttons = new JButton[5];
        for (int i = 0; i < buttons.length; i++) {
            buttons[i] = new JButton();
            buttons[i].setName("b" + i);
            buttons[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
//                    System.out.println(e.getSource());
                    JButton b = (JButton) e.getSource();
                    String name = b.getName();

                    switch (name) {
                        case "b0":
                            String path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe";
                            String url = "https://github.com/Yegor9151";
                            ProcessBuilder process1 = new ProcessBuilder(path, url);

                            try {
                                process1.start();
                            } catch (IOException ioException) {
                                System.out.println(path + " process in not started");
                                ioException.printStackTrace();
                            }
                            break;
                        case "b1":
                            for (int i = 500; i >= 0; i--){
                                robot.mouseMove(i, i);
                                robot.delay(5);
                            }
                            robot.mouseMove(50, 30);
                            robot.mousePress(MouseEvent.BUTTON1_MASK);
                            robot.delay(200);
                            robot.mouseRelease(MouseEvent.BUTTON1_MASK);
                            break;
                        case "b2":
                            ProcessBuilder process2 = new ProcessBuilder("calc");

                            try {
                                process2.start();
                            } catch (IOException ioException){
                                System.out.println("calc process in not started");
                                ioException.printStackTrace();
                            }
                            robot.delay(5000);
                            robot.keyPress(KeyEvent.VK_ALT);
                            robot.delay(200);
                            robot.keyPress(KeyEvent.VK_F4);
                            robot.keyRelease(KeyEvent.VK_F4);
                            robot.keyRelease(KeyEvent.VK_ALT);
                            break;
                        case "b3":
                            for(int i = 0; i < 10; i++){
                                robot.keyPress(KeyEvent.VK_CAPS_LOCK);
                                robot.delay(500);
                                robot.keyRelease(KeyEvent.VK_CAPS_LOCK);
                                robot.delay(500);

                                robot.keyPress(KeyEvent.VK_SCROLL_LOCK);
                                robot.delay(500);
                                robot.keyRelease(KeyEvent.VK_SCROLL_LOCK);
                                robot.delay(500);
                            }
                            break;
                        case "b4":
                            System.exit(0);
                    }
                }
            });
            window.add(buttons[i]);
        }
        buttons[0].setText("Браузер");
        buttons[1].setText("Мышь");
        buttons[2].setText("Калькулятор");
        buttons[3].setText("Мигание");
        buttons[4].setText("Выход");

        window.pack();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setVisible(true);
    }
}
