package gui;

//all the imports, oh so many immports, should just imported everything why not
import java.awt.Canvas;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.TitledBorder;
@SuppressWarnings("rawtypes")
public class PositionScreen implements ActionListener { 

	//define Frames
	JFrame frame;
	
	//These are variables we need throughout the program and I was lazy so they're static. Live with it.
	static Sprite arraySprite[];
	static Sprite isThere[];
	static ArrayList<String> codeText;
	
	static String fadeText;
	static String flipText;
	static int counterNum;
	static int errorNum;
	static int backupCount;
	
	//define canvas
	Canvas fakeScreen;
	
	//define Jpanels
	JPanel mainPanel;
	JPanel charDetailsSelect;
	JPanel clickPanel;

	//define JLabel
	JLabel lblpos;
	JLabel outJLabel;
	JLabel lblFace;
	JLabel lblOutfit;
	JLabel lblArm;
	JLabel lblCharacter;
	JLabel outlabl;
	JLabel charSelect;
	JLabel labelPos;
	
	JLabel clickFace;
	JLabel clickArm;
	JLabel clickOutfit;
	JLabel clickFade;
	JLabel clickCharacter;
	JLabel clickpos;
	static JLabel counter;

	//define JCheckBox
	JCheckBox fadeChcbx;
	JCheckBox hideChcnx;


	//define ComboBox
	JComboBox armCbox;
	JComboBox charaCbox;
	JComboBox clothesCbox;
	JComboBox faceCbox;
	JComboBox posCbox;

	//define Jbuttons
	JButton btnClear;
	JButton btnGenerate;
	JButton showChara;
	
	
	//define Jmenu + JmenuStuff
	JMenu     fileMenu;
	JMenu	  iMessedUpMenu;
	JMenuItem deleteEntryMenuItem;
	JMenuItem genTextFileMenuItem;
	JMenuItem setCounter;
	JMenuItem exitMenuItem;
	JMenuItem clearListMenuItem;
	JMenuBar menuBar;
	
	
	
	
	public static void main(String[] args) 
	{
		//not really sure what it does, delay calling this code?
		EventQueue.invokeLater(new Runnable() 
		{
			public void run() 
			{
				try {
						//creates a new Position Object called window
						PositionScreen window = new PositionScreen();
						window.frame.setVisible(true);
					} 
				catch (Exception e) 
					{
						//shit stuff broke
						e.printStackTrace();
					}
			}
		}
		);
	}


	public PositionScreen() {
		try{
			//unneeded but oh well
			 initialize();
			}
		catch(Exception e)
		{
			//whoops stuff broke again
			System.out.println("ERROR" + e);
		}
		
	}

	@SuppressWarnings("unchecked")
	private void initialize()  {
		
		//ignore generic stuff im getting lazy
		menuBar            = new JMenuBar();
	    fileMenu           = new JMenu("File");
	    iMessedUpMenu	   = new JMenu("I messed up");
	    deleteEntryMenuItem= new JMenuItem("Delete Scene");
	    genTextFileMenuItem= new JMenuItem("Generate Code File");
	    setCounter 		   = new JMenuItem("Set Counter");
	    exitMenuItem	   = new JMenuItem("Exit");
	    clearListMenuItem  = new JMenuItem("Clear all Scene");
	    
	 
	    genTextFileMenuItem.addActionListener(this);
	    setCounter.addActionListener(this);
	    deleteEntryMenuItem.addActionListener(this);
	    exitMenuItem.addActionListener(this);
	    clearListMenuItem.addActionListener(this);
	    
	    menuBar.add(fileMenu);
	    fileMenu.add(genTextFileMenuItem);
	    fileMenu.add(setCounter);
	    fileMenu.add(exitMenuItem);
	    counterNum=0;
	    menuBar.add(iMessedUpMenu);
	    iMessedUpMenu.add(deleteEntryMenuItem);
	    iMessedUpMenu.add(clearListMenuItem);
	    
	  
		
		arraySprite = new Sprite[7]; 
		isThere = new Sprite [7];
		codeText = new ArrayList<String>();
		
		//creating frame
		frame = new JFrame();
		frame.setResizable(false);
		frame.setBounds(100, 100, 730, 441);
		frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		frame.setJMenuBar(menuBar);
		
		
		//adding charSelect
		charSelect = new JLabel("");
		charSelect.setBounds(19, 26, 168, 209);
		charSelect.setHorizontalAlignment(SwingConstants.CENTER);
		frame.getContentPane().setLayout(null);
		frame.getContentPane().add(charSelect);

		
		
		//adding fakeScreen
		fakeScreen = new Canvas();
		fakeScreen.setBackground(new Color(204, 255, 204));
		fakeScreen.setBounds(200, 10, 550, 249);
		
		//for detect when they click on the fake screen -> display char info on side
		fakeScreen.addMouseListener(new MouseAdapter() 
		{
			
			//-50-150, 60-260, 0-200, 250-450, 375-575, 325-525, 165-365
			//-50-100, 110-260, 100-135, 300-400, 425-575, 425-475,
			
			public void mousePressed(MouseEvent me)
			{
				System.out.println(me.getX() + " " +me.getY());
				//range of pos 1 spot
				if(me.getX()<62 && me.getY()<250)
				{
					//if there's a char there
					if(arraySprite[0]!=null)
					{
					//pulls information off of the Sprite object and display on side
					clickArm.setText("Arm: "+ arraySprite[0].getArm());
					clickCharacter.setText("Character: "+ arraySprite[0].getCharacter());
					clickFace.setText("Face: "+ arraySprite[0].getFace());
					clickFade.setText("Fade: "+ arraySprite[0].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[0].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[0].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[0].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[0].getFacePos());
					armCbox.setSelectedIndex(arraySprite[0].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[0].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[0].getPosPos());
					fadeChcbx.setSelected(arraySprite[0].getFade());
					}
					//System.out.println(1);
				}
				else if(me.getX()<200 && me.getX()>120 && me.getY()<250)
				{
					if(arraySprite[1]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[1].getArm());
					clickCharacter.setText("Character: "+ arraySprite[1].getCharacter());
					clickFace.setText("Face: "+ arraySprite[1].getFace());
					clickFade.setText("Fade: "+ arraySprite[1].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[1].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[1].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[1].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[1].getFacePos());
					armCbox.setSelectedIndex(arraySprite[1].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[1].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[1].getPosPos());
					fadeChcbx.setSelected(arraySprite[1].getFade());
					}
					//System.out.println(2);
				}
				else if(me.getX()<125 && me.getX()>62 && me.getY()<250)
				{
					if(arraySprite[2]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[2].getArm());
					clickCharacter.setText("Character: "+ arraySprite[2].getCharacter());
					clickFace.setText("Face: "+ arraySprite[2].getFace());
					clickFade.setText("Fade: "+ arraySprite[2].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[2].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[2].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[2].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[2].getFacePos());
					armCbox.setSelectedIndex(arraySprite[2].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[2].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[2].getPosPos());
					fadeChcbx.setSelected(arraySprite[2].getFade());
					}
					//System.out.println(3);
				}
				else if(me.getX()<380 && me.getX()>306 && me.getY()<250)
				{
					if(arraySprite[3]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[3].getArm());
					clickCharacter.setText("Character: "+ arraySprite[3].getCharacter());
					clickFace.setText("Face: "+ arraySprite[3].getFace());
					clickFade.setText("Fade: "+ arraySprite[3].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[3].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[3].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[3].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[3].getFacePos());
					armCbox.setSelectedIndex(arraySprite[3].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[3].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[3].getPosPos());
					fadeChcbx.setSelected(arraySprite[3].getFade());
					}
					//System.out.println(4);
				}
				else if(me.getX()>445 && me.getY()<250)
				{
					if(arraySprite[4]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[4].getArm());
					clickCharacter.setText("Character: "+ arraySprite[4].getCharacter());
					clickFace.setText("Face: "+ arraySprite[4].getFace());
					clickFade.setText("Fade: "+ arraySprite[4].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[4].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[4].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[4].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[4].getFacePos());
					armCbox.setSelectedIndex(arraySprite[4].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[4].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[4].getPosPos());
					fadeChcbx.setSelected(arraySprite[4].getFade());
					}
					//System.out.println(5);
				}
				else if(me.getX()>375 && me.getX()<441 && me.getY()<380)
				{
					if(arraySprite[5]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[5].getArm());
					clickCharacter.setText("Character: "+ arraySprite[5].getCharacter());
					clickFace.setText("Face: "+ arraySprite[5].getFace());
					clickFade.setText("Fade: "+ arraySprite[5].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[5].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[5].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[5].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[5].getFacePos());
					armCbox.setSelectedIndex(arraySprite[5].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[5].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[5].getPosPos());
					fadeChcbx.setSelected(arraySprite[5].getFade());
					}
					//System.out.println(6);
				}
				else if(me.getX()<306 && me.getX()>214 && me.getY()<216)
				{
					if(arraySprite[6]!=null)
					{
					clickArm.setText("Arm: "+ arraySprite[6].getArm());
					clickCharacter.setText("Character: "+ arraySprite[6].getCharacter());
					clickFace.setText("Face: "+ arraySprite[6].getFace());
					clickFade.setText("Fade: "+ arraySprite[6].getFade());
					clickOutfit.setText("Outfit: "+ arraySprite[6].getOutfit());
					clickpos.setText("Pos: "+ arraySprite[6].getPos());
					
					charaCbox.setSelectedIndex(arraySprite[6].getCharPos());
					faceCbox.setSelectedIndex(arraySprite[6].getFacePos());
					armCbox.setSelectedIndex(arraySprite[6].getArmPos());
					clothesCbox.setSelectedIndex(arraySprite[6].getOutfitPos());
					posCbox.setSelectedIndex(arraySprite[6].getPosPos());
					fadeChcbx.setSelected(arraySprite[6].getFade());
					}
					//System.out.println(7);
				}
				//0-75 75-125 125-175   236-286     350-400 400-425 425-525 
				//System.out.println(me.getX() + " " + me.getY()); //0-50 50-150 100-200 212-312 350-400 400-425 425-525 
				//50 50-100 100-200 212-312 325-425
			/*case "pos1": fakeScreen.getGraphics().drawImage(image, 0, 50, 100,200 ,null);
			break;
			case "pos2": fakeScreen.getGraphics().drawImage(image, 100, 50, 100,200 ,null);
			break;
			case "pos3": fakeScreen.getGraphics().drawImage(image, 50, 50, 100,200 ,null);
			break;
			case "pos4": fakeScreen.getGraphics().drawImage(image, 325, 50, 100,200 ,null);
			break;
			case "pos5": fakeScreen.getGraphics().drawImage(image, 425, 50, 100,200 ,null);
			break;
			case "pos6": fakeScreen.getGraphics().drawImage(image, 375, 50, 100,200 ,null);
			break;
			case "pos7": fakeScreen.getGraphics().drawImage(image, 212, 50, 100,200 ,null);
			*/	
				
			}
			});
		
		frame.getContentPane().add(fakeScreen);
		
		//making Char detail panel
		charDetailsSelect = new JPanel();
		charDetailsSelect.setBorder(new TitledBorder(null,"Character Details", TitledBorder.LEADING, TitledBorder.TOP, null, null));
		charDetailsSelect.setBounds(19, 277, 472, 118);
		frame.getContentPane().add(charDetailsSelect);
		charDetailsSelect.setLayout(null);
		
		
		outlabl = new JLabel("Select character");
		outlabl.setBounds(6, 16, 171, 14);
		charDetailsSelect.add(outlabl);
		
		//making face drop down
		faceCbox = new JComboBox();
		faceCbox.setModel(new DefaultComboBoxModel(Face.values()));
		faceCbox.setSelectedIndex(0);
		faceCbox.setBounds(65, 40, 99, 20);
		charDetailsSelect.add(faceCbox);
		
		lblFace = new JLabel("Face:");
		lblFace.setBounds(9, 43, 46, 14);
		charDetailsSelect.add(lblFace);
		
		
		//making outfit drop down
		lblOutfit = new JLabel("Outfit");
		lblOutfit.setBounds(6, 80, 46, 14);
		charDetailsSelect.add(lblOutfit);
		
		clothesCbox = new JComboBox();
		clothesCbox.setModel(new DefaultComboBoxModel(Outfit.values()));
		clothesCbox.setSelectedIndex(0);
		clothesCbox.setBounds(65, 77, 99, 20);
		charDetailsSelect.add(clothesCbox);
		
		
		//making arm drop down
		lblArm = new JLabel("Arm:");
		lblArm.setBounds(204, 43, 46, 14);
		charDetailsSelect.add(lblArm);
		
		armCbox = new JComboBox();
		armCbox.setModel(new DefaultComboBoxModel(Arm.values()));
		armCbox.setSelectedIndex(0);
		armCbox.setBounds(250, 40, 99, 20);
		
		charDetailsSelect.add(armCbox);
		
		//making fade drop down
		fadeChcbx = new JCheckBox("Fade On");
		fadeChcbx.setBounds(370, 60, 97, 23);
		charDetailsSelect.add(fadeChcbx);
		
		counter = new JLabel("Line: " + counterNum);
		counter.setBounds(370, 30, 97, 23);
		charDetailsSelect.add(counter);
		
		
		//ignore not needed anymore
		//hideChcnx = new JCheckBox("Hide Pos");
		//hideChcnx.setBounds(370, 30, 97, 23);
		//charDetailsSelect.add(hideChcnx);
		
		//making pos drop down
		labelPos = new JLabel("Pos:");
		labelPos.setBounds(204, 75, 97, 20);
		charDetailsSelect.add(labelPos);
		
		posCbox = new JComboBox();
		posCbox.setModel(new DefaultComboBoxModel(position.values()));
		posCbox.setSelectedIndex(0);
		posCbox.setBounds(250, 75, 89, 23);
		charDetailsSelect.add(posCbox);
		
		//add button
		showChara = new JButton("Add");
		showChara.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					//THIS SECTION WILL NEED TO BE REDONE WHEN WE ADD THE INDIVIDUAL ASSETS ONTO THE GAME
					
					//create Sprite object
					createSprite(charaCbox.getSelectedItem().toString(),(String)faceCbox.getSelectedItem().toString(),(String)armCbox.getSelectedItem().toString(),(String)clothesCbox.getSelectedItem().toString(),(String)posCbox.getSelectedItem().toString(),fadeChcbx.isSelected(),charaCbox.getSelectedIndex(),faceCbox.getSelectedIndex(),armCbox.getSelectedIndex(),clothesCbox.getSelectedIndex(),posCbox.getSelectedIndex());
					@SuppressWarnings("unused")
					
					//find image file
					String shortCharName = "";
					String revisedExpressionName = "";
					String tmpFace="";
					
					switch(charaCbox.getSelectedItem().toString())
					{
					case "Osomatsu": shortCharName="oso";
					break;
					case "Karamatsu": shortCharName="kara";
					break;
					case "Choromatsu": shortCharName="choro";
					break;
					case "Ichimatsu": shortCharName="ichi";
					break;
					case "Jyushimatsu": shortCharName="jyushi";
					break;
					case "Todomatsu": shortCharName="todo";
					break;
					default: shortCharName=charaCbox.getSelectedItem().toString();
					break;
					}
					
					if(shortCharName!=charaCbox.getSelectedItem().toString())
					{
					tmpFace=faceCbox.getSelectedItem().toString();
					revisedExpressionName=tmpFace.substring(0, tmpFace.length()-1)+"0";
					int meme =(int)((tmpFace.charAt(tmpFace.length()-1)-48))*2-1;
					
					
					
					File baseFile = new File("image\\"+charaCbox.getSelectedItem().toString()+".jpg");
					
					
					File outfitFile = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\"+shortCharName+"_"+clothesCbox.getSelectedItem().toString()+".png");
					
					System.out.println(tmpFace);
					File faceFile = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\head\\"+shortCharName+"_"+revisedExpressionName+meme+".png");
					File faceFile2 = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\head\\"+shortCharName+"_"+tmpFace+"01.png");	
					File faceFile3 = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\head\\"+shortCharName+"_"+tmpFace+".png");	
					File faceFile4 = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\head\\"+shortCharName+"_"+tmpFace.substring(0,tmpFace.length()-1)+"0"+tmpFace.charAt(tmpFace.length()-1)+".png");
					
					
					File armFile = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\"+shortCharName+"_"+clothesCbox.getSelectedItem().toString()+"_"+armCbox.getSelectedItem().toString().substring(0, armCbox.getSelectedItem().toString().length()-1)+"s0"+armCbox.getSelectedItem().toString().charAt(armCbox.getSelectedItem().toString().length()-1)+".png");
					File armFile2 = new File("image\\"+charaCbox.getSelectedItem().toString()+"\\"+shortCharName+"_"+clothesCbox.getSelectedItem().toString()+"_"+armCbox.getSelectedItem().toString().substring(0, armCbox.getSelectedItem().toString().length()-1)+"s.png");
						
					
					
					
					File file = new File("image\\none.jpg");
				
					BufferedImage none = ImageIO.read(file);
					
					
					
					BufferedImage armImage;
			
					
					System.out.println(outfitFile);
					System.out.println(faceFile);
					
					
					errorNum=0;
					BufferedImage outfitImage = ImageIO.read(outfitFile);
					BufferedImage faceImage;
					System.out.println(armFile);
					
					errorNum=1;
					try
					{
						 System.out.println(armFile);
						 armImage = ImageIO.read(armFile);
						 
					}
					catch (Exception b)
					{
						 System.out.println(armFile2);
						 armImage = ImageIO.read(armFile2);
						
					}
					errorNum=2;
					try
					{
						 System.out.println(faceFile);
						 faceImage= ImageIO.read(faceFile);;
						 
					}
					catch (Exception c)
					{
						try
						{
						 System.out.println(faceFile2);
						 faceImage= ImageIO.read(faceFile2);
						}
						catch (Exception d)
						{
							 try
							 {
							 System.out.println(faceFile3);
							 faceImage= ImageIO.read(faceFile3);
							 }
							 catch (Exception f)
							 {
								 System.out.println(faceFile4);
								 faceImage= ImageIO.read(faceFile4);
							 }
						}
					}
					
					if(fadeChcbx.isSelected())
					{
						
						//armImage = new BufferedImage(armImage.getWidth(null), armImage.getHeight(null), BufferedImage.TYPE_INT_RGB);
						
						//outfitImage = op.filter(outfitImage, null);
						//faceImage = op.filter(faceImage, null);
						Color myWhite = new Color(0,0,0);
						int rgb = myWhite.getRGB();
						for (int i = 0; i < 150; i++) {
					        for (int j = 0; j < 150; j++) {
					        	outfitImage.setRGB(i+300,j+500,rgb);
					        }
					    }
						
						
						
					}
					//System.out.println(armImage.toString());
					
					
					//will add image of char in spot depending on pos chosen, prob shouldve made a method oh well
					switch(posCbox.getSelectedItem().toString())
					{
					
					case "pos1": fakeScreen.getGraphics().drawImage(none, -50, 50, 150,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, -50, 50, 200,200,null);
								 fakeScreen.getGraphics().drawImage(faceImage, -50, 50, 200,200,null);
								 fakeScreen.getGraphics().drawImage(armImage, -50, 50, 200,200,null);
					break;
					case "pos2": fakeScreen.getGraphics().drawImage(none, 110, 50, 150,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 60, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 60, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 60, 50, 200,200 ,null);
					break;
					case "pos3": fakeScreen.getGraphics().drawImage(none, 100, 50, 35,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 0, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 0, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 0, 50, 200,200 ,null);
					break;
					case "pos4": //fakeScreen.getGraphics().drawImage(nakedImage, 325, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(none, 300, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 250, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 250, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 250, 50, 200,200 ,null);
					break;
					case "pos5": //fakeScreen.getGraphics().drawImage(nakedImage, 425, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(none, 425, 50, 150,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 375, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 375, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 375, 50, 200,200 ,null);
					break;
					case "pos6": //fakeScreen.getGraphics().drawImage(nakedImage, 375, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(none, 425, 50, 50,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 325, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 325, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 325, 50, 200,200 ,null);
					break;
					case "pos7": //fakeScreen.getGraphics().drawImage(nakedImage, 212, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(none, 265, 50, 50,200 ,null);
								 fakeScreen.getGraphics().drawImage(outfitImage, 165, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(faceImage, 165, 50, 200,200 ,null);
								 fakeScreen.getGraphics().drawImage(armImage, 165, 50, 200,200 ,null);
					break;
					default: System.out.println("ERROR");
					break;
					}	
					
					
			        System.out.println("works");

					}
					//if we're putting blank in the slot
					else
					{
						
						File file = new File("image\\none.jpg");
						
						Image none = ImageIO.read(file);
						
						switch(posCbox.getSelectedItem().toString())
						{
						case "pos1": fakeScreen.getGraphics().drawImage(none, -50, 50, 200,200 ,null);

						break;
						case "pos2": fakeScreen.getGraphics().drawImage(none, 60, 50, 200,200 ,null);

						break;
						case "pos3": fakeScreen.getGraphics().drawImage(none, 0, 50, 200,200 ,null);

						break;
						case "pos4": //fakeScreen.getGraphics().drawImage(nakedImage, 325, 50, 100,200 ,null);
									 fakeScreen.getGraphics().drawImage(none, 250, 50, 200,200 ,null);

						break;
						case "pos5": //fakeScreen.getGraphics().drawImage(nakedImage, 425, 50, 100,200 ,null);
									 fakeScreen.getGraphics().drawImage(none, 375, 50, 200,200 ,null);
	
						break;
						case "pos6": //fakeScreen.getGraphics().drawImage(nakedImage, 375, 50, 100,200 ,null);
									 fakeScreen.getGraphics().drawImage(none, 325, 50, 200,200 ,null);
		
						break;
						case "pos7": //fakeScreen.getGraphics().drawImage(nakedImage, 212, 50, 100,200 ,null);
									 fakeScreen.getGraphics().drawImage(none, 165, 50, 150,200 ,null);
									
						break;
						default: System.out.println("ERROR");
						break;
						}	
						
					}
					//so if some reason some of the assets isnt there -> defaults to naked 
				} catch (IOException e1) 
				
				{
					
					if(errorNum==0)
					{
						 JOptionPane.showMessageDialog(null, "Missing Body asset");
					}
					else if (errorNum==1)
					{
						 JOptionPane.showMessageDialog(null, "Missing Arm asset");
					}
					else if(errorNum==2)
					{
						 JOptionPane.showMessageDialog(null, "Missing Face asset");
					}
					
					
					File baseFile = new File("image\\"+charaCbox.getSelectedItem().toString()+".jpg");
					Image nakedImage=null;
					try {
						 nakedImage = ImageIO.read(baseFile);
					} catch (IOException e2) {
						// TODO Auto-generated catch block
						e2.printStackTrace();
					}
					
					switch(posCbox.getSelectedItem().toString())
					{
					case "pos1": fakeScreen.getGraphics().drawImage(nakedImage, 0, 50, 100,200 ,null);

					break;
					case "pos2": fakeScreen.getGraphics().drawImage(nakedImage, 100, 50, 100,200 ,null);

					break;
					case "pos3": fakeScreen.getGraphics().drawImage(nakedImage, 50, 50, 100,200 ,null);

					break;
					case "pos4": //fakeScreen.getGraphics().drawImage(nakedImage, 325, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(nakedImage, 320, 50, 100,200 ,null);

					break;
					case "pos5": //fakeScreen.getGraphics().drawImage(nakedImage, 425, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(nakedImage, 420, 50, 100,200 ,null);

					break;
					case "pos6": //fakeScreen.getGraphics().drawImage(nakedImage, 375, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(nakedImage, 370, 50, 100,200 ,null);
	
					break;
					case "pos7": //fakeScreen.getGraphics().drawImage(nakedImage, 212, 50, 100,200 ,null);
								 fakeScreen.getGraphics().drawImage(nakedImage, 210, 50, 100,200 ,null);
								
					break;
					default: System.out.println("ERROR");
					break;
					}	
					
					
					
					
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			
				
				
			}
		});
		
		
		showChara.setBounds(360, 85, 89, 23);
		//showChara.setBounds(x, y, width, height);
		charDetailsSelect.add(showChara);

		lblCharacter = new JLabel("Character:");
		lblCharacter.setBounds(29, 246, 63, 14);
		frame.getContentPane().add(lblCharacter);

		//making chara drop down
		charaCbox = new JComboBox();
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

		
		
		//character detail layout setup 
		clickPanel = new JPanel();
		clickPanel.setBorder(new TitledBorder(null,"Character Details", TitledBorder.LEADING, TitledBorder.TOP, null, null));
		clickPanel.setBounds(6, 16, 150, 200);
		frame.getContentPane().add(clickPanel);
		clickPanel.setLayout(null);
		
		
		clickCharacter = new JLabel("Character:");
		clickCharacter.setBounds(6, 16, 150, 14);
		clickPanel.add(clickCharacter);
		
		clickArm = new JLabel("Arm:");
		clickArm.setBounds(6, 35, 150, 14);
		clickPanel.add(clickArm);
		
		clickFace = new JLabel("Face:");
		clickFace.setBounds(6, 54, 150, 14);
		clickPanel.add(clickFace);
		
		clickFade = new JLabel("Fade:");
		clickFade.setBounds(6, 73, 150, 14);
		clickPanel.add(clickFade);
		
		clickOutfit = new JLabel("Outfit:");
		clickOutfit.setBounds(6, 92, 150, 14);
		clickPanel.add(clickOutfit);
		
		clickpos = new JLabel("Pos:");
		clickpos.setBounds(6, 111, 150, 14);
		clickPanel.add(clickpos);
		
	
		
		
		
		
		
		//clear the array of Sprites and clear screen
		JButton btnClear = new JButton("Clear");
		btnClear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				
				
				Image image = null;
				for(int x=0; x<7; x++)
				{
					arraySprite[x]=null;
				}
				
				File file = new File("image\\none.jpg");
				try {
					 image = ImageIO.read(file);
				}
				catch (Exception e)
				{
					
				}
				
			fakeScreen.getGraphics().drawImage(image, 0, 50, 900,200 ,null);		
			
				
			}
		});
		
		btnClear.setBounds(555, 277, 96, 35);
		frame.getContentPane().add(btnClear);
		
		
		//generate code for game
		JButton btnGenerate = new JButton("Generate Scene");
		btnGenerate.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				GenerateScene();
			}
		});
		btnGenerate.setBounds(555, 323, 150, 59);
		frame.getContentPane().add(btnGenerate);

		

	}
	
	//this is where it makes the game code 
	public static void GenerateScene ()
	{
		for(int x=0; x<7; x++)
		{

			//int tmpInt= arraySprite[x].getPosPos();
			
			if(arraySprite[x]==null)
			{
				if(isThere[x]!=null)
					{
						codeText.add("hide "+isThere[x].getCharacter());
						isThere[x]=null;
					}
			}
			else if (arraySprite[x]!=null && isThere[x]!=null && isThere[x].getCharacter()!=arraySprite[x].getCharacter())
				codeText.add("hide " + isThere[x].getCharacter());
		}
		for(int x=0; x<7; x++)
		{
			
				fadeText="";
				flipText="";
				
				if(arraySprite[x]!=null)
				{
					if(((int)(arraySprite[x].getPos().charAt(arraySprite[x].getPos().length()-1))-48 ) <4)
						flipText= " Flip";
					if(arraySprite[x].getFade())
						fadeText= " Fade";
					System.out.println(arraySprite[x].getPos().charAt(arraySprite[x].getPos().length()-1) +" " +  ((int)(arraySprite[x].getPos().charAt(arraySprite[x].getPos().length()-1))-48 ));	
					//THIS IS THE IMPORTANT PART, MAKE SURE THIS IS RIGHT
					
					codeText.add("show "+arraySprite[x].getCharacter() + " "+ arraySprite[x].getOutfit() +" " + "0"+ arraySprite[x].getArm().charAt(arraySprite[x].getArm().length()-1)+ " "+ arraySprite[x].getFace() + fadeText + flipText +" at " + arraySprite[x].getPos());
					isThere[x]=arraySprite[x];	
				}
			}				
		
		JOptionPane.showMessageDialog(null, "Scene Generated");
		counterNum++;
		counter.setText("Line: "+counterNum);
		codeText.add("done");
		
		for(int y=0; y<codeText.size(); y++)
		{
			System.out.println(codeText.get(y));
		}
		
		backupCount++;
		if(backupCount==10)
		{
			String path = "backup.txt";
	    	Path file = Paths.get(path);
			try {
				Files.write(file, codeText, Charset.forName("UTF-8"));
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			backupCount=0;
		}
	}
	
	
	//Creates a new Sprite object
	public static void createSprite (String tmpChar, String tmpFace, String tmpArm, String tmpOutfit, String tmpPos, boolean isFade, int tmpCharPos, int tmpFacePos, int tmpArmPos, int tmpOutfitPos, int tmpPosPos) throws IOException
	{
		int pos= (char)(tmpPos.charAt(tmpPos.length()-1))-49;
		
		if(tmpChar=="None")
		{
			arraySprite[pos]=null;
		}
		else
		{
		Sprite person = new Sprite(tmpChar, tmpFace, tmpArm, tmpOutfit, tmpPos, isFade,tmpCharPos,tmpFacePos,tmpArmPos,tmpOutfitPos,tmpPosPos);
		arraySprite[pos]=person;
		}
		//System.out.println(arraySprite[pos]);
		
	}
	
	
	//ignore this
	/*
	public void paint (Graphics g, Image img) {
	    g.drawImage(img, 0,0, null);
	}
	

	public void mouseClicked(MouseEvent e) {
	  if (e.getButton() == 1)
			  {
		  		if (e.getX() >= 70 && e.getX() <= 170 && e.getY() >= 70 && e.getY() <= 170)
	  			{

	  			}
	  			
			  }
	  
	  System.out.println(e.getX()+ " " + e.getY());
	  JOptionPane.showMessageDialog(null,e.getX()+ "\n" + e.getY());

	 }
	*/
	
	//didnt want to make a new button, got lazy sue me. Menu item to create file of code
	 public void actionPerformed(ActionEvent e) {
		    Object source = e.getSource();
		    
		    
		    if (source == genTextFileMenuItem) 
		    {
		    	String path = JOptionPane.showInputDialog("Name your file (dont forget the .txt");
		    	Path file = Paths.get(path);
				try {
					Files.write(file, codeText, Charset.forName("UTF-8"));
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				JOptionPane.showMessageDialog(null, "Done, look for a "+ path+" in the same folder as program");
		    
				
				
				String path2 = "backup.txt";
		    	Path file2 = Paths.get(path2);
		    	
				try {
					Files.delete(file2);
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
		    }
		    else if(source == setCounter)
		    {
		    	counterNum= Integer.parseInt( JOptionPane.showInputDialog("Type in your starting line"));
		    	counter.setText("Line: "+counterNum);
		    }
		    else if(source == deleteEntryMenuItem)
		    {
		    	
		    	
		    	int check= JOptionPane.showConfirmDialog(null, "This will delete the last generated scene are you ok with this?");
		    	System.out.println("check" + check);
		    	
		    	if(check==0)
		    	{
			    	int x=codeText.size();
					if(x==0)
					{
						JOptionPane.showMessageDialog(null, "No code found");
					}
					else
					{
					codeText.remove(x-1);
					x--;
					try
					{
						while(codeText.get(x-1)!="done")
						{
							if(x==0)
								break;
							else
							{
								
									codeText.remove(x-1);
								
							
								x--;
								System.out.println("remove");
							}
						}
					}
					catch (Exception z)
					{
						System.out.println(e);
						//JOptionPane.showMessageDialog(null, "No code left to delete");
					}
					counterNum--;
					counter.setText("Line: "+counterNum);
					JOptionPane.showMessageDialog(null, "Removed Entry");
					}
		    	}
		 }
		    else if(source==exitMenuItem)
		    {
		    	int check= JOptionPane.showConfirmDialog(null, "Did you export your code already?");
		    	System.out.println("check" + check);
		    	
		    	if(check==0)
		    	{
		    		System.exit(0);
		    	}
		    }
		    else if(source==clearListMenuItem)
		    {
		    	int check= JOptionPane.showConfirmDialog(null, "This will delete all generated Scenes are you ok with this?");
		    	System.out.println("check" + check);
		    	
		    	if(check==0)
		    	{
			    	int x=codeText.size();
					if(x==0)
					{
						JOptionPane.showMessageDialog(null, "No code found");
					}
					else
					{
						while(codeText.size()!=0)
						{
							codeText.remove(0);
						}
						JOptionPane.showMessageDialog(null, "All scenes removed");
						
						try
						{
						String path2 = "backup.txt";
				    	Path file2 = Paths.get(path2);
				    	Files.delete(file2);
						}
						catch(Exception z)
						{
							
						}
					}
		    	}					
		    }
	 }



	
	
	
}
