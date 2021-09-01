import javax.swing.JPanel;
import java.awt.*;
import java.awt.event.*;

class MyPanel extends JPanel {
    Color[] colors = {Color.BLACK, Color.GREEN, Color.BLUE, Color.RED, Color.YELLOW, Color.WHITE, Color.ORANGE};

    int nowColor = 0;
    int mouseX, mouseY;

    boolean flag = false;

    class MyMouse1 implements MouseListener {
        public void mousePressed(MouseEvent e) {
            int tX = e.getX();
            int tY = e.getY();
            int numClick = e.getClickCount();
            int button = e.getButton();

            if ((tX > 0) && (tX < 700) && (tY > 0) && (tY < 50)) {
                if (numClick == 1) {
                    if (button == 1) nowColor = tX / 100;
                }
            }
        }
        public void mouseReleased(MouseEvent e) {
            flag = false;
        }
        public void mouseClicked(MouseEvent e) {}
        public void mouseEntered(MouseEvent e) {}
        public void mouseExited(MouseEvent e) {}
    }
    class MyMouse2 implements MouseMotionListener {
        public void mouseDragged(MouseEvent e) {
            int tX = e.getX();
            int tY = e.getY();

            if (tY > 50){
                mouseX = tX;
                mouseY = tY;
                flag = true;

                repaint();
            }
        }
        public void mouseMoved(MouseEvent e) {
            int tX = e.getX();
            int tY = e.getY();

            if ((tX > 0) && (tX < 700) && (tY > 0) && (tY < 50)) setCursor(new Cursor(Cursor.HAND_CURSOR));
            else setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
        }
    }

    public MyPanel() {
        addMouseListener(new MyMouse1());
        addMouseMotionListener(new MyMouse2());

        setFocusable(true);
    }

    public void paintComponent(Graphics gr) {

        for (int i = 0; i < colors.length; i++) {
            gr.setColor(colors[i]);
            gr.fillRect(i * 100, 0, 100, 50);
        }

        if (flag) {
            gr.setColor(colors[nowColor]);
            gr.fillRect(mouseX, mouseY, 3, 3);
        }
    }
}
