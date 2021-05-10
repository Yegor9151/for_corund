import java.io.*;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.imageio.*;

public class Pole extends JPanel {
	private Image shapka;
	private Image fon;
	public int x = 350;
	private int slogn; // объявим переменную сложности
	private Podar[] gamePodar; // объявляем массив подарков
	
	public Pole(int slogn) { // добавим аргумент сложности в поле
		this.slogn = slogn; // будем записывать сложность в переменную класса
		
		gamePodar = new Podar[7]; // объявляем в массиве 7 ячеек
		
		try { // пытаемся загрузить подарки
			for(int i = 0; i < gamePodar.length; i++) { // перебираем подарки по сложности
				// заполняем выделенные ячейки массива картинками подарков
				gamePodar[i] = new Podar(ImageIO.read(new File("./p" + i + ".png")));
			}
		} catch (Exception e) {}
		try {
			fon = ImageIO.read(new File("./fon.png"));
		} catch(Exception e) {}
		try {
			shapka = ImageIO.read(new File("./shapka.png"));
		} catch(Exception e) {}
		
		Timer timerDraw = new Timer(50, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				repaint();
			}
		});
		timerDraw.start();
		
		Timer timerUpdate = new Timer(3000, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				updateStart();
			}
		});
		timerUpdate.start();
	}
	public void updateStart() { // метод для управления подарками
		int kol = 0; // переменная для подсчета числа подарков
		for(int i = 0; i < gamePodar.length; i++) { // перебираем подарки
			if(!gamePodar[i].act && kol < slogn) { // если подарок не активен и ихчисло меньше сложности
				gamePodar[i].start(); // тогда активируем подарок
				break; // и прерываем перебор подарков
			}
			else kol++; // иначе прибавляем подарок к общему числу
		}
	}
	public void paint(Graphics gr) {
		super.paint(gr);
		
		gr.drawImage(fon, 0, 0, null);
		gr.drawImage(shapka, x, 465, null);
		
		// отрисовываем каждый подарок
		for(int i = 0; i < gamePodar.length; i++) gamePodar[i].draw(gr);
	}
}