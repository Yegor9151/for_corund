import java.io.*;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.imageio.*;

public class Pole extends JPanel {
	private Image shapka;
	private Image fon;
	private Image end_game;
	
	public int x = 350;
	private int point = 0;
	
	private int slogn;
	private Podar[] gamePodar;
	
	private Timer timerUpdate, timerDraw; // Объявляем таймеры
	
	public Pole(int slogn) {
		this.slogn = slogn;
		
		gamePodar = new Podar[7];
		
		try {
			for(int i = 0; i < gamePodar.length; i++) {
				gamePodar[i] = new Podar(ImageIO.read(new File("./p" + i + ".png")));
			}
		} catch (Exception e) {}
		try {
			fon = ImageIO.read(new File("./fon.png"));
		} catch(Exception e) {}
		try {
			shapka = ImageIO.read(new File("./shapka.png"));
		} catch(Exception e) {}
		try { // Загружаем конец игры
			end_game = ImageIO.read(new File("./end_game.png"));
		} catch (Exception e) {}
		
		timerDraw = new Timer(50, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				repaint();
			}
		});
		timerDraw.start();
		timerUpdate = new Timer(1500, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				updateStart();
			}
		});
		timerUpdate.start();
	}
	public void updateStart() {
		int kol = 0;
		for(int i = 0; i < gamePodar.length; i++) {
			if(!gamePodar[i].act && kol < slogn) {
				gamePodar[i].start();
				kol++;
				break;
			}
		}
	}
	public void paint(Graphics gr) {
		super.paint(gr);
		
		gr.drawImage(fon, 0, 0, null);
		gr.drawImage(shapka, x, 465, null);
		gr.setColor(Color.WHITE); // добавляем цвет 
		gr.drawString("Счет: " + point, 50, 50); // отрисовываем счет
		
		for(int i = 0; i < gamePodar.length; i++) {
			gamePodar[i].draw(gr);
			// если подарок активен и нижняя граница подарка больше или равна уровня шапки
			if(gamePodar[i].act && (gamePodar[i].y + gamePodar[i].img.getHeight(null) >= 470)) {
				// тогда проверяем координаты шапки и подарка
				if(Math.abs(gamePodar[i].x - x) > 75) {
					gr.drawImage(end_game, 300, 300, null); // отрисовываем конец игры
					timerDraw.stop(); // останавливаем таймеры
					timerUpdate.stop();
				}
				else {
					gamePodar[i].act = false; // отключаем подарок
					point++;
				}
			}
		}
	}
}