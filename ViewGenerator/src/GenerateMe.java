import java.awt.Canvas;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.DefaultComboBoxModel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.border.TitledBorder;
import javax.swing.JToggleButton;
import javax.swing.JSeparator;
import javax.swing.JCheckBox;

public class GenerateMe {

	private JFrame frame;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GenerateMe window = new GenerateMe();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}


	public GenerateMe() {
		initialize();
	}

	private void initialize() {
		Util util = new Util();
		frame = new JFrame();
		frame.setResizable(false);
		frame.setBounds(100, 100, 730, 441);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		String sampleImageLocation = "C:\\Users\\user\\Desktop\\pad\\Game\\assets\\oso_naked_full.png"; //change to path of the image
		
		JLabel charSelect = new JLabel("");
		charSelect.setBounds(19, 26, 168, 209);
		charSelect.setHorizontalAlignment(SwingConstants.CENTER);
		ImageIcon charaAsset = new ImageIcon(sampleImageLocation);
		ImageIcon resizedCharacter  = util.scaleImage(charaAsset, 200, 200);
		frame.getContentPane().setLayout(null);


		charSelect.setIcon(resizedCharacter);
		frame.getContentPane().add(charSelect);

		Canvas fakeScreen = new Canvas();
		fakeScreen.setBackground(new Color(204, 255, 204));
		fakeScreen.setBounds(253, 10, 444, 249);
		frame.getContentPane().add(fakeScreen);

		JPanel charDetailsSelect = new JPanel();
		charDetailsSelect.setBorder(new TitledBorder(null,"Character Details", TitledBorder.LEADING, TitledBorder.TOP, null, null));
		charDetailsSelect.setBounds(19, 277, 472, 118);
		frame.getContentPane().add(charDetailsSelect);
		charDetailsSelect.setLayout(null);
		

		JLabel outlabl = new JLabel("Select character");
		outlabl.setBounds(6, 16, 171, 14);
		charDetailsSelect.add(outlabl);
		
		JComboBox faceCbox = new JComboBox();
		faceCbox.setBounds(65, 40, 99, 20);
		charDetailsSelect.add(faceCbox);
		
		JLabel lblFace = new JLabel("Face:");
		lblFace.setBounds(9, 43, 46, 14);
		charDetailsSelect.add(lblFace);
		
		JLabel lblOutfit = new JLabel("Outfit");
		lblOutfit.setBounds(6, 80, 46, 14);
		charDetailsSelect.add(lblOutfit);
		
		JComboBox clothesCbox = new JComboBox();
		clothesCbox.setBounds(65, 77, 99, 20);
		charDetailsSelect.add(clothesCbox);
		
		JLabel lblArm = new JLabel("Arm:");
		lblArm.setBounds(204, 43, 46, 14);
		charDetailsSelect.add(lblArm);
		
		JComboBox armCbox = new JComboBox();
		armCbox.setBounds(250, 40, 99, 20);
		charDetailsSelect.add(armCbox);
		
		JCheckBox fadeChcbx = new JCheckBox("Fade On");
		fadeChcbx.setBounds(204, 76, 97, 23);
		charDetailsSelect.add(fadeChcbx);
		
		JButton showChara = new JButton("GO");
		showChara.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		showChara.setBounds(360, 43, 89, 51);
		charDetailsSelect.add(showChara);

		JLabel lblCharacter = new JLabel("Character:");
		lblCharacter.setBounds(29, 246, 63, 14);
		frame.getContentPane().add(lblCharacter);

		
		JComboBox charaCbox = new JComboBox();
		charaCbox.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String charaSelected = charaCbox.getSelectedItem().toString();
				outlabl.setText(charaSelected);
				
				
			}
		});
		
		lblCharacter.setLabelFor(charaCbox);

		charaCbox.setModel(new DefaultComboBoxModel(Character.values()));
		charaCbox.setSelectedIndex(0);
		charaCbox.setBounds(94, 246, 105, 20);
		frame.getContentPane().add(charaCbox);

		JButton btnNewButton = new JButton("ADD >>");
		
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				//some action
			}
		});
		btnNewButton.setBounds(158, 99, 89, 54);
		frame.getContentPane().add(btnNewButton);
		
		JButton btnClear = new JButton("Clear");
		btnClear.setBounds(555, 277, 96, 35);
		frame.getContentPane().add(btnClear);
		
		JButton btnGenerate = new JButton("Generate");
		btnGenerate.setBounds(555, 323, 105, 59);
		frame.getContentPane().add(btnGenerate);

		

	}
}
