import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class MyPanel extends JPanel {

    Color[] colors = {Color.BLACK, Color.GREEN, Color.BLUE, Color.RED, Color.YELLOW, Color.WHITE, Color.ORANGE};
    int tCol = 0;

    int mX, mY;
    int w = 3, h = 3;
    boolean dragged = false;

    class MyMouse implements MouseListener {

        public void mouseClicked(MouseEvent e) {
        }

        public void mousePressed(MouseEvent e) {
            int tX = e.getX();
            int tY = e.getY();

            if (tX > 0 && tX < 100 * colors.length && tY > 0 && tY < 50) {
                tCol = tX / 100;
                repaint();
            }
        }

        public void mouseReleased(MouseEvent e) {
        }

        public void mouseEntered(MouseEvent e) {
        }

        public void mouseExited(MouseEvent e) {
        }
    }

    class MyMouseWheel implements MouseWheelListener {

        public void mouseWheelMoved(MouseWheelEvent e) {

            w += e.getWheelRotation();
            h += e.getWheelRotation();

            if (w < 2) {
                w = 2;
                h = 2;
            } else if (w > 50) {
                w = 50;
                h = 50;
            }
            repaint();
        }
    }

    class MyMouseMotion implements MouseMotionListener {

        public void mouseDragged(MouseEvent e) {
            mX = e.getX();
            mY = e.getY();
            dragged = true;
            repaint();
        }

        public void mouseMoved(MouseEvent e) {
            int tX = e.getX();
            int tY = e.getY();

            if (tX > 0 && tX < 100 * colors.length && tY > 0 && tY < 50)
                setCursor(new Cursor(Cursor.HAND_CURSOR));
            else setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
        }
    }

    MyPanel() {
        addMouseListener(new MyMouse());
        addMouseMotionListener(new MyMouseMotion());
        addMouseWheelListener(new MyMouseWheel());

        setFocusable(true);
    }

    public void paint(Graphics g) {

        for (int i = 0; i < colors.length; i++) {
            g.setColor(colors[i]);
            g.fillRect(100 * i, 0, 100, 50);
        }

        g.setColor(Color.WHITE);
        g.fillRect(700, 0, 100, 50);
        g.setColor(colors[tCol]);
        g.fillOval(700 + (100 / 2 - w / 2), 50 / 2 - h / 2, w, h);

        if (dragged) {
            g.setColor(colors[tCol]);
            g.fillOval(mX, mY, w, h);
        }
    }
}
