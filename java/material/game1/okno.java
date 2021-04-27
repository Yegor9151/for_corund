// Указываем имя пакета, если необходимо!
// package game1;


// Подключения необходимых библиотек
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

// Класс окна, в котором размещено игровое поле
class okno extends JFrame
{	
    private pole gameP; // Закрытая Переменная класса - игровое поле
    
    // Обработчик событий нажатий на клавиши
	private class myKey implements KeyListener  
	{
		    // Метод, который срабатывает при нажатии
	   	    public void keyPressed(KeyEvent e)
	   	    {
	   	    	// Получение кода нажатой клавиши
	   	    	int key_ = e.getKeyCode();
	   	    		   	    	
	   	    }
	   	    public void keyReleased(KeyEvent e) {}
	   	    public void keyTyped(KeyEvent e) {}
	   }            	
	
    // Конструктор класса
    public okno()
    {
    	// Подключение обработчика события для клавиатуры к окну
 	    addKeyListener(new myKey());
 	    // Установка активности окна
    	setFocusable(true);
    	
    	// Задание размеров и положения окна
        setBounds(0,0,800,600);
        // Задание заголовка окна
        setTitle("Игра: Новогодний дождь");
        // Запрет изменения размеров окна
        setResizable(false);
        
        // Создание объекта - игрового поля
        gameP = new pole();
        // Прикрепление (вложение) панели - игрового поля в окно
        Container con = getContentPane();
        con.add(gameP);

        // Завершение работы приложения при закртытии окна
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Сделать окно видимым 
    	setVisible(true);
    }
}

