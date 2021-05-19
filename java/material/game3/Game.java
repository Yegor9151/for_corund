import javax.swing.*;

public class Game {
	public static void main(String[] args) {
		// добавим выбор сложности
		String rez = JOptionPane.showInputDialog(null, "¬ведите сложность игры от 1 до 7", "—ложность", 2);
		int slogn = Integer.parseInt(rez);
		
		// сделаем проверку на сложность, которую будем передовать в окно
		if (slogn > 0 && slogn < 8) new Okno(slogn);
		else JOptionPane.showMessageDialog(null, "Ќеверна€ сложность");
	}
}
