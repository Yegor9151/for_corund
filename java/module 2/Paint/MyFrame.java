import javax.swing.JFrame;

class MyFrame extends JFrame {

    public MyFrame() {

        add(new MyPanel());

        setBounds(0, 0, 800, 600);
        setTitle("Управление приложением с помошью мыши");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setFocusable(true);
        setVisible(true);
    }
}