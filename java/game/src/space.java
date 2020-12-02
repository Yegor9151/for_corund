import javax.swing.*;
import javax.imageio.*;

import java.io.*;

import java.awt.*;
import java.awt.event.*;


public class space extends JPanel {
	private Image rocket;
	private Image moon;
	private Image game_over;
	public int x_rocket = 350, y_rocket = 460;
	private int hard, point, HP = 3;
	private present[] game_present;
	private Timer timerUpdate, timerDraw;
	
	public space(int hard) {
		String[] image_names = new String[] {
				"asteroid", "meteor", "UFO"
		};
		game_present = new present[3];
		
		try {
			for(int i = 0; i < game_present.length; i++) {
				game_present[i] = new present(ImageIO.read(new File("./" + image_names[i] + ".png")));
			}
		}
		catch (Exception e) {}
		
		this.hard = hard;
		
		///////////////////////Excepts//////////////////////////////
		try {
			moon = ImageIO.read(new File("./galaxy.png"));
		}//try
		catch (Exception e) {}
		
		try {
			rocket = ImageIO.read(new File("./rocket.png"));
		}//try
		catch (Exception e) {}
		
		try {
			game_over = ImageIO.read(new File("./game_over.png"));
		}//try
		catch (Exception e) {}
		
		////////////////////////////Timers////////////////////////////
		timerDraw = new Timer(10, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				repaint();
			}//actionPerformed
		});//timerDraw
		timerDraw.start();
		
		timerUpdate = new Timer(1500, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				updateStart();
			}//actionPerformed
		});//timerUpdate
		timerUpdate.start();
		
	}//space
	
	public void updateStart() {
		int count = 0;
		
		for(int i = 0; i < game_present.length; i++) {
			if(!game_present[i].act) {
				if(count < hard) {
					game_present[i].start();
					break;
				}
			}
			else count++;
		}
	}//updateStart
	
	public void paint(Graphics gr) {
		super.paint(gr);//метод дл€ очистки панели
		gr.drawImage(moon, 0, 0, 800, 600, null);
		gr.drawImage(rocket, x_rocket, y_rocket, 100, 100, null);
		gr.setColor(Color.WHITE);
		gr.drawString("—чет: " + point, 700, 550);
		
		for(int i = 0; i < HP; i++) {
			gr.drawImage(rocket, 680 + i*30, 20, 30, 30, null);
		}
		
		for(int i=0; i < game_present.length; i++) {
			game_present[i].draw(gr);
			if(game_present[i].act) {
				if(y_rocket == game_present[i].y+80) {
					if (Math.abs(game_present[i].x - x_rocket) < 40) {
						HP --;
						if(HP == 0) {
							gr.drawImage(game_over, 150, 50, 500, 500, null);
							timerDraw.stop();
							timerUpdate.stop();
						}// Game Over
					}//HP drop x
				}//HP drop y
				if(game_present[i].y > 600) {
					game_present[i].act = false;
					point ++;
				}
			}//if present act
		}//for present chose
		
	}//paint
	
}//class space
