import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.imageio.*;

public class LoadAndMove { // Класс загрузки и управления

	public static void main(String[] args) { // главный метод

		new MyFrame(); // вызов класса

	} // main

} // Program

class MyFrame extends JFrame { // наш класс на основе предка

	public MyFrame() { // конструктор класса
		setBounds(0,0,800,600);
		setTitle("My first anuimation");

		add(new MyPanel()); // добавление вызванного класса

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // закрытие созданного окна
		setVisible(true);
	} // Constructor

} // MyFrame

class MyPanel extends JPanel {

	private Image img;
	
	private int x = 0, y = 0;
	public int direction = 2;
	int speed = 1;

	private class myKey implements KeyListener { // implements - в нашем классе используем эллементы интерфейса 
		public void keyPressed(KeyEvent e) { // используем метод класса и дополняем его
			int key = e.getKeyCode(); // отслеживаем события
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

	public MyPanel() {
		addKeyListener(new myKey()); // добавление отслеживания событий
		setFocusable(true);
		
		try { // попытка загрузить картинку
			img = ImageIO.read(new File("./earth.png"));
		} 
		catch (IOException exp) {
			System.out.println("картинка отсутствует");
		}

		Timer FPS = new Timer(1, new ActionListener() { // создание таймера
			public void actionPerformed(ActionEvent e) { // изменяем представление
				if(direction == 0) x-= speed; //left
				if(direction == 1) y-= speed; //up
				if(direction == 2) x+= speed; //right
				if(direction == 3) y+= speed; //down
				repaint(); // заливаем окно
			} // actionPerformed
		}); // FPS
		FPS.start(); // запускаем таймер

	} // Constructor

	public void paint(Graphics gr) {
		super.paint(gr);
		gr.drawImage(img, x, y, 200, 200, null);
	} // paint

} // MyPannel