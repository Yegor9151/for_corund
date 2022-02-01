import javax.swing.*;
import java.awt.*;


class Frame extends JFrame {

    JTextArea text = new JTextArea();
    double result;
    String operation;

    Frame() {
        text.setText("0.0");
    }

    void actionButton(String value) {
        result = Double.parseDouble(text.getText());
        text.setText("");
        operation = value;
    }

    void buttonClick(JButton button) {
        String value = button.getText();
        System.out.println(value);

        switch (value) {
            case "Выход" -> System.exit(0);
            case "C" -> text.setText("0.0");
            case "+", "-", "*", "/" -> actionButton(value);
            case "=" -> {
                double operand = Double.parseDouble(text.getText());
                switch (operation) {
                    case "+" -> text.setText("" + (result + operand));
                    case "-" -> text.setText("" + (result - operand));
                    case "*" -> text.setText("" + (result * operand));
                    case "/" -> text.setText("" + (result / operand));
                }
            }
            default -> text.setText("" + text.getText() + value);
        }
    }

    void run() {
        JPanel panel = new JPanel();
        panel.setLayout(null);

        String[] buttonText = {"+", "-", "*", "/", "=", "C", "Выход"};
        for (int i = 0; i < 17; i++) {
            JButton button = new JButton();
            button.setBounds(30, 50 + i * 30, 100, 25);
            if (i < 10) button.setText("" + i);
            else button.setText(buttonText[i - 10]);
            button.addActionListener(e -> buttonClick(button));
            panel.add(button);
        }

        JLabel result = new JLabel("Результат: ");
        result.setBounds(130, 0, 300, 50);
        result.setFont(new Font("arial", 1, 30));
        panel.add(result);

        text.setBounds(300, 10, 300, 35);
        text.setFont(new Font("arial", 2, 30));
        panel.add(text);

        getContentPane().add(panel);

        setTitle("Калькулятор");
        setBounds(100, 100, 700, 700);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
}