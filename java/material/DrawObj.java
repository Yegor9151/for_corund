// https://metanit.com/java/tutorial/3.14.php

package study;

import javax.swing.*;
import java.awt.*;

public class DrawObj {
	
	public static void main(String[] args) {
		
		new MyFrame(100, 100);
		
	} // main

} // Programm

class MyFrame extends JFrame {
	
	public MyFrame(int x, int y) {
		setBounds(x, y, 800, 600);
		setTitle("Графика");
		setVisible(true);
		
		add(new MyPannel());
	}
	
}

class MyPannel extends JPanel {
	
	public void paint(Graphics gr) {
		gr.setColor(new Color(0, 0, 255));
		gr.fillRect(10, 10, 500, 300);
		
		gr.setColor(new Color(255, 0, 0));
		gr.fillOval(100, 100, 400, 400);
	}
	
}
