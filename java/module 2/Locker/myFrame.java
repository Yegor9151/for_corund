import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class myFrame extends JFrame {

    private Robot robot;
    private Timer timer;
    private int count = 0;
    private Frame window;

    public myFrame() {
        try {
            robot = new Robot();
        } catch (Exception ignore) {
        }

        timer = new Timer(1_000, new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                saveScreen();
            }
        });
        timer.start();

        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
        setVisible(true);
        setVisible(false);
    }

    private void saveScreen() {
        count ++;

        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        int w = dimension.width;
        int h = dimension.height;

        try {
            BufferedImage img = robot.createScreenCapture(new Rectangle(0, 0, w, h));
            ImageIO.write(img, "png", new File("D:\\screen\\img" + count + ".png"));
        } catch (Exception ignore) {}

        if(count > 6) {
            timer.start();

            window = new Frame();
            window.setResizable(false);
            window.setBounds(0, 0, w, h);
            window.setBackground(Color.RED);
            window.setAlwaysOnTop(true);
            window.setUndecorated(true);
            window.setOpacity(0.5f);
            window.setVisible(true);
        }
    }
}
