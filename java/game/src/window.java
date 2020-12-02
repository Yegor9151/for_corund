import javax.swing.*;
import java.awt.event.*;

public class window extends JFrame {
	private space game_space;
	
	private class myKey implements KeyListener{

		public void keyTyped(KeyEvent e) {}

		public void keyPressed(KeyEvent e) {
//			System.out.println(e.getKeyCode());
			int key = e.getKeyCode();
			int speed = 5;
			
			if(key == 27) System.exit(0); //exit
			
			else if(key == 37) {
				game_space.x_rocket -= speed; //left
				if (game_space.x_rocket < -20) game_space.x_rocket += speed;
			}
			else if(key == 39) {
				game_space.x_rocket += speed; //right
				if (game_space.x_rocket > 710) game_space.x_rocket -= speed;
			}
			else if(key == 38) {
				game_space.y_rocket -= speed; //up
				if (game_space.y_rocket < 0) game_space.y_rocket += speed;
			}
			else if(key == 40) {
				game_space.y_rocket += speed; //down
				if (game_space.y_rocket > 460) game_space.y_rocket -= speed;
			}
			
		}//keyPressed

		public void keyReleased(KeyEvent e) {}
		
	}//class myKey
	
	public window(int hard) {
		addKeyListener(new myKey());
		setFocusable(true);
		
		setTitle("Игра - \"новогодний дождь\" - " + hard + " level");
		setBounds(0,0,800,600);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		game_space = new space(hard);
		add(game_space);
		
		setVisible(true);
		
	}//window
	
}//class window
