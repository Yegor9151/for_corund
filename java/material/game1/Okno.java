import java.awt.event.*;
import javax.swing.*;

public class Okno extends JFrame {
	
	private Pole gameP;
	
	private class myKey implements KeyListener{
		
		public void keyPressed(KeyEvent e) {
			int key = e.getKeyCode();
			
			// управление
			if (key == 27) System.exit(0);
			else if (key == 37) {
				if(gameP.x - 30 > -50) gameP.x -= 30;
				else gameP.x = 750;
			}
			else if (key == 39) {
				if(gameP.x + 30 < 750) gameP.x += 30;
				else gameP.x = -50;
			}
		}
		
		public void keyTyped(KeyEvent e) {}

		public void keyReleased(KeyEvent e) {}
		
	}
	
	public Okno() {
		addKeyListener(new myKey());
		setFocusable(true);
		
		setTitle("Игра \"Новогодний дождь\"");
		setBounds(0,0,800,600);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		gameP = new Pole();
		add(gameP);
		
		setVisible(true);
	}
	
}
