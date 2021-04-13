// https://metanit.com/java/tutorial/3.14.php

package study;

import javax.swing.*;
import java.awt.*;
import java.io.*;
import javax.imageio.*;

public class LoadImage {

	public static void main(String[] args) {

		new MyFrame();

	} // main

} // Program

class MyFrame extends JFrame {

	public MyFrame() {
		setBounds(0,0,800,600);
		setTitle("My first anuimation");

		add(new MyPannel());

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	} // Constructor

} // MyFrame

class MyPannel extends JPanel {

	private Image img;
	
	public MyPannel() {
		try {
			img = ImageIO.read(new File("./earth.png"));
		} 
		catch (IOException exp) {}
	} // Constructor

	public void paint(Graphics gr) {
		gr.drawImage(img, 0, 0, null);
	} // paint

} // MyPannel
