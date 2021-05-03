import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

// класс для управления подарками
public class Podar {
	public Image img;
	private int x, y;
	public boolean act;
	private Timer timerUpdate;
	
	// метод - конструктор класса
	public Podar(Image img) {
		// создание таймера в котором будет происходить падение подарка 
		timerUpdate = new Timer(500, new ActionListener() {
			// метод для отслеживание событий и выполнения действий
			public void actionPerformed(ActionEvent e) {
				vniz(); // падение
			}
		});
		this.img = img; // путь до изображения подарка
		act = false; // деактивация подарка при его инициализации
	}
	// метод для запуска таймера
	public void start() {
		timerUpdate.start(); // запуск таймера
		y = 0; // запуск с верхнего края
		x = (int)(Math.random() * 700); // запуск с рандомной позиции по x
		act = true; // активация подарка
	}
	// метод оисывающий падение
	public void vniz() {
		// при активации подарка он начинает падать на 6 пикселей
		if (act) y += 6;
		// если положение подарка + его высота превышает высоты шапки, 
		// то падение оканчивается
		if (y + img.getHeight(null) > 470) timerUpdate.stop(); 
	}
	// метод описывающий отрисовку подарка
	public void draw(Graphics gr) {
		// если податок активен, то он отрисовывается на экране по его текущим координатам
		if (act) gr.drawImage(img, x, y, null);
	}
}
