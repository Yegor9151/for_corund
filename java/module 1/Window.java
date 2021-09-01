import java.awt.event.*;
import javax.swing.*;

public class Window extends JFrame {
    private Field field;

    private class myKey implements KeyListener{
        public void keyPressed(KeyEvent e) {
            int key = e.getKeyCode();

            if (key == 27) System.exit(0);
            else if (key == 37) {
                if(field.x - 30 > -50) field.x -= 30;
                else field.x = 750;
            }
            else if (key == 39) {
                if(field.x + 30 < 750) field.x += 30;
                else field.x = -50;
            }
        }
        public void keyTyped(KeyEvent e) {}
        public void keyReleased(KeyEvent e) {}
    }

    public Window() { // добавим аргумент сложность в окно
        addKeyListener(new myKey());

        setFocusable(true);
        setTitle("Игра \"Новогодний дождь\" "); // добавим показатель сложности
        setBounds(0,0,800,600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        field = new Field();
        add(field);

        setVisible(true);
    }
}