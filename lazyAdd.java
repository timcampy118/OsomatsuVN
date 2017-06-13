import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class lazyAdd {
	
	
static String name;
static ArrayList <String> body;
static ArrayList <String> faces;
static ArrayList <String> list;
static Scanner scan;
static Integer response;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		response=0;
		
		name = JOptionPane.showInputDialog("type in the Matsu's name"); 
		response=JOptionPane.showConfirmDialog(null,"Do you have a bodies text file in same location as program with one body per line. \nEx) \nschoolS\nschoolW\nnaked");
		
		if(response==1)
			System.exit(1);
		
		response=JOptionPane.showConfirmDialog(null,"Do you have a faces text file in same location with one face per line. \nEx) \nshocked\nhappy1");
		
		if(response==1)
			System.exit(1);
		
		
		try
		{
		scan= new Scanner(new File("bodies.txt"));
		body= new ArrayList <String>();
		}
		catch(FileNotFoundException e)
		{
			JOptionPane.showMessageDialog(null, "Bodies file not found" + e);
			System.exit(1);
		}
		
		while (scan.hasNext())
		{
			body.add(scan.nextLine());
		}

		try
    	{
			scan= new Scanner(new File("faces.txt"));
			faces = new ArrayList <String>();
    	}
		catch(FileNotFoundException e)
		{
			JOptionPane.showMessageDialog(null, "Face file not found" + e);
			System.exit(1);
		}
		
		while (scan.hasNext())
		{
			faces.add(scan.nextLine());
		}
		
		//body.add("Casual");
		//body.add("SchoolS");
		//body.add("SchoolW");
		//body.add("Bathrobe");
		//body.add("Bathtowel");
		//body.add("Mainpark");
		//body.add("Maintee");
		//body.add("Naked");
		//body.add("Pj");
		//body.add("Sera");
	
		
		//faces.add("Angry3");
		//faces.add("Angry4");
		//faces.add("Neutral");
		//faces.add("Angry1");
		//faces.add("Angry2");
		//faces.add("Blank");
		//faces.add("Dark");
		//faces.add("Displeased");
		//faces.add("Happy");
		//faces.add("Shocked");
		//faces.add("Surprised");
		//faces.add("Nervous");
		//faces.add("Thinking");
		
		
		
		list=new ArrayList<String>();
	

		for (int x=0; x<body.size(); x++)
		{
			for (int y=0; y<faces.size();y++)
			{
				if(faces.get(y)=="dark")
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y) +"\",\"\",\"\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");	
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='4')
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y) +"\",\"07\",\"08\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='3')
				list.add("image "+ name +" "+body.get(x)+" " +faces.get(y)+" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+faces.get(y).toLowerCase()+"\",\"05\",\"06\",\""+body.get(x).toLowerCase()+"\",\"false\",800,950))");
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='2')
				list.add("image "+ name +" "+body.get(x)+" " +faces.get(y)+" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+faces.get(y).toLowerCase()+"\",\"03\",\"04\",\""+body.get(x).toLowerCase()+"\",\"false\",800,950))");
				else
				list.add("image "+ name +" "+body.get(x)+" " +faces.get(y)+" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+faces.get(y).toLowerCase()+"\",\"01\",\"02\",\""+body.get(x).toLowerCase()+"\",\"false\",800,950))");
				
				
				
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Flip= Transform(\""+ name +" "+ body.get(x) +" "+ faces.get(y) +"\",xzoom=-1.0)");
				

				if(faces.get(y)=="dark")
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y) +"\",\"\",\"\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");	
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='4')
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"07\",\"08\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='3')
					list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"05\",\"06\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");
				else if((faces.get(y)).charAt((faces.get(y).length()-1))=='2')
					list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"03\",\"04\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");
				else
					list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"01\",\"02\",\""+ body.get(x).toLowerCase() +"\",\"true\",800,950))");
						
				list.add("image "+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade Flip= Transform(\""+ name +" "+ body.get(x) +" "+ faces.get(y) +" Fade\",xzoom=-1.0)");
				
							}
		}
		
		Path file = Paths.get("imageList.txt");
		Files.write(file, list, Charset.forName("UTF-8"));
		JOptionPane.showMessageDialog(null, "Done, look for a imageList in the same folder as program");
		
		
	}


	}




