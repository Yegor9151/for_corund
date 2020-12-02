import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class present {
	public Image img;
	public int x, y;
	public boolean act;
	private Timer timerUpdate;
	
	public present(Image img) {
		timerUpdate = new Timer(20, new ActionListener() {
			
			public void actionPerformed(ActionEvent e) {
				drop();
				
			}//actionPerformed
		});
		
		this.img = img;
		act = false;
	}//present
	
	public void start() {
		timerUpdate.start();
		y = -100;
		x = (int)(Math.random()*700);
		act = true;
	}//start
	
	public void drop() {
		if(act == true) y+=5;
		if(y > 600) timerUpdate.stop();
		
	}//drop
	
	public void draw(Graphics gr) {
		if(act) gr.drawImage(img, x, y, 100, 100, null);
	}//draw
	
}//class present








