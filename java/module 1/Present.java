import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Present {
    public Image img;
    public int x, y;
    public boolean act;
    private Timer timerUpdate;

    public Present(Image img) {
        timerUpdate = new Timer(100, new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                drop();
            }
        });
        this.img = img;
        act = false;
    }
    public void start() {
        timerUpdate.start();
        y = 0;
        x = (int)(Math.random() * 700);
        act = true;
    }
    public void drop() {
        if(act) y += 6;
        if(y + img.getHeight(null) > 470) timerUpdate.stop();
    }
    public void draw(Graphics gr) {
        if(act) gr.drawImage(img, x, y, null);
    }
}