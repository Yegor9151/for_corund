// https://metanit.com/java/tutorial/3.14.php

package study;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.imageio.*;

public class LoadAndMove {

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
	private int x = 0, y = 0;
	public int direction = 2;
	int speed = 1;

	private class myKey implements KeyListener {
		public void keyPressed(KeyEvent e) {
			int key = e.getKeyCode();
//			System.out.println(key);
			if(key == 87) direction = 1; //w
			if(key == 65) direction = 0; //a
			if(key == 83) direction = 3; //s
			if(key == 68) direction = 2; //d
		}
		public void keyReleased(KeyEvent e) {

		}
		public void keyTyped(KeyEvent e) {

		}
	}

	public MyPannel() {
		addKeyListener(new myKey());
		setFocusable(true);
		
		try {
			img = ImageIO.read(new File("./earth.png"));
		} 
		catch (IOException exp) {
			System.out.println("изображение не найдено");
		}

		Timer FPS = new Timer(1, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(direction == 0) x-=speed; //left
				if(direction == 1) y-=speed; //up
				if(direction == 2) x+=speed; //right
				if(direction == 3) y+=speed; //down
				repaint();
			} // actionPerformed
		}); // FPS
		FPS.start();

	} // Constructor

	public void paint(Graphics gr) {
		super.paint(gr);
		gr.drawImage(img, x, y, 200, 200, null);
	} // paint

} // MyPannel
