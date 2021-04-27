// Указываем имя пакета, если необходимо!
// package game1;

// Подключения необходимых библиотек
import javax.imageio.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

// Класс панели, которая является игровым полем
class pole extends JPanel
{
       // Таймер для перерисовки игрового поля
       public Timer timerDraw;
	  	  
	   // Конструктор класса 
	   public pole()
	   {		   
		   // Создание таймера, который будет перерисовывать игровое поле 20 раз в секунду 	   
		   timerDraw = new Timer(50,new ActionListener() {				
				public void actionPerformed(ActionEvent e) {
		           repaint(); // Запуск метода перерисовки поля (public void paintComponent(Graphics gr))
				}
			});		    
		   timerDraw.start(); // Запуск таймера для перерисовки
		    			    		    		    		    		    
	   }
	   	   
	   // Метод, который отрисовывает графические объекты на панели
	   public void paintComponent(Graphics gr)
	   {
		   // Выполнить отрисовку сначала самого окна
		   // (полное очищение)
		   super.paintComponent(gr);

	   }	   
}