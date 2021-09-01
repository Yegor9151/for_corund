import java.io.*;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.imageio.*;

public class Field extends JPanel {
    private Image background;
    private Image hat;
    private Image endGame;

    public int x = 350;
    private int point = 0;

    private Present[] presents;

    private Timer timerUpdate, timerDraw; // Объявляем таймеры

    public Field() {
        presents = new Present[7];

        try {
            for(int i = 0; i < presents.length; i++) {
                presents[i] = new Present(ImageIO.read(new File("./p" + i + ".png")));
            }
        } catch (Exception ignored) {}
        try {
            background = ImageIO.read(new File("./fon.png"));
        } catch(Exception ignored) {}
        try {
            hat = ImageIO.read(new File("./shapka.png"));
        } catch(Exception ignored) {}
        try { // Загружаем конец игры
            endGame = ImageIO.read(new File("./end_game.png"));
        } catch (Exception ignored) {}

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
        for (Present present : presents) {
            if (!present.act) {
                present.start();
                break;
            }
        }
    }
    public void paint(Graphics gr) {
        super.paint(gr);

        gr.drawImage(background, 0, 0, null);
        gr.drawImage(hat, x, 465, null);
        gr.setColor(Color.WHITE); // добавляем цвет
        gr.drawString("Счет: " + point, 50, 50); // отрисовываем счет

        for (Present present : presents) {
            present.draw(gr);
            if (present.act && (present.y + present.img.getHeight(null) >= 470)) {
                if (Math.abs(present.x - x) > 75) {
                    gr.drawImage(endGame, 300, 300, null);
                    timerDraw.stop();
                    timerUpdate.stop();
                } else {
                    present.act = false;
                    point++;
                }
            }
        }
    }
}