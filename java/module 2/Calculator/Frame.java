import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class Frame extends JFrame {
    int x = 100;
    int y = 100;
    int w = 700;
    int h = 700;

    String title = "Untitled";

    double p1 = 0;
    double p2 = 0;
    int operation = 0;

    JButton[] buttons = new JButton[17];
    String[] buttonsText = {"+", "-", "*", "/", "=", "C", "Выход"};

    Frame() {
    }

    Frame(String title) {
        this.title = title;
    }

    void buttonClick(){
        JOptionPane.showMessageDialog(null, "!");
    }

    void run() {
        JPanel panel = new JPanel();
        panel.setLayout(null);

        Font buttonFont = new Font("serif", 0, 20);
        Font resultFont = new Font("arial", 1, 30);
        Font textFont = new Font("arial", 2, 30);

        for (int i = 0; i < buttons.length; i++) {
            buttons[i] = new JButton();
            buttons[i].setFont(buttonFont);
            buttons[i].setBounds(30, 50 + i * 30, 100, 25);

            if (i < 10) buttons[i].setText("" + i);
            else buttons[i].setText(buttonsText[i-10]);

            buttons[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    buttonClick();
                }
            });
            panel.add(buttons[i]);
        } //размещение кнопок

        JLabel result = new JLabel("Результат: ");
        result.setFont(resultFont);
        result.setBounds(130, 0 , 300, 50);
        panel.add(result);

        JTextArea text = new JTextArea();
        text.setFont(textFont);
        text.setBounds(300, 10, 300, 35);
        text.setForeground(new Color(0,0,100));
        panel.add(text);

        Container container = getContentPane();
        container.add(panel);

        setBounds(x, y, w, h);
        setTitle(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
}
