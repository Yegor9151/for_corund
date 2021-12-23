import javax.swing.*;


public class MyFrame extends JFrame {

    MyFrame() {

        add(new MyPanel());

        setTitle("Управлепние приложением с помошью мыши");
        setBounds(0, 0, 900, 700);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
}
