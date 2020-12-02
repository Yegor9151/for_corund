import javax.swing.*;

public class game {

	public static void main(String[] args) {
		String chose = JOptionPane.showInputDialog(null, "Ââåäèòå ñëîæíîñòü èãğû îò 1 äî 3", "Ñëîæíîñòü", 1);
		int hard = Integer.parseInt(chose);
		
		if(hard > 0 && hard < 4) {
			window win = new window(hard);
		}
		else {
			JOptionPane.showMessageDialog(null, "İıı... íåò, òîâàğèøü, òîëüêî îò 1 äî 3, áûâàé! XD");
		}

	}//main

}//class game
