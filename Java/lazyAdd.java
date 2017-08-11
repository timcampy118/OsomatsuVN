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

		list=new ArrayList<String>();
	
		

		for (int x=0; x<body.size(); x++)
		{
			for (int y=0; y<faces.size();y++)
			{
				for(int z=1; z<4; z++)
				{
				
				int num=1;
				if(z==3 && name.equals("oso"))
				{
					num=0;
				}
			
				if(faces.get(y)=="dark")
				//special case 
				{
					//nothing
					list.add("image "+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"\",\"\",\""+ body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"false\",800,950))");	
					//fade
					list.add("image "+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase() +"\",\"\",\"\",\""+ body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"true\",800,950))");
					
				}
				
				else if((faces.get(y)).charAt((faces.get(y).length()-1))>'0' && ((faces.get(y)).charAt((faces.get(y).length()-1))<':'))
				{
					list.add("image "+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ (faces.get(y).substring(0,faces.get(y).length()-1)).toLowerCase() +"\",\"0" + ((((int) (faces.get(y).charAt((faces.get(y).length()-1)))-48))*2-1) + "\",\"0" + ((((int) (faces.get(y).charAt((faces.get(y).length()-1)))-48))*2) + "\",\""+ body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"false\",800,950))");
					list.add("image "+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ (faces.get(y).substring(0,faces.get(y).length()-1)).toLowerCase() +"\",\"0" + ((((int) (faces.get(y).charAt((faces.get(y).length()-1)))-48))*2-1) + "\",\"0" + ((((int) (faces.get(y).charAt((faces.get(y).length()-1)))-48))*2) + "\",\""+ body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"true\",800,950))");
					
				}
				else
				{
					list.add("image "+ name +" "+ body.get(x) +" 0" + z +" "+ faces.get(y) +" = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase()+"\",\"01\",\"02\",\""+body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"false\",800,950))");
					list.add("image "+ name +" "+ body.get(x) +" 0" + z +" "+ faces.get(y) +" Fade = DynamicDisplayable(renpy.curry(charComposite)(\""+ name +"\",\""+ faces.get(y).toLowerCase()+"\",\"01\",\"02\",\""+body.get(x).toLowerCase() +"\",\"\","+num+",\"0"+z+"\",\"true\",800,950))");
				}
				
				
				//flip only
				list.add("image "+ name +" "+ body.get(x) +" 0" + z +" "+ faces.get(y) +" Flip= Transform(\""+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +"\",xzoom=-1.0)");
					
				//fade + flip
				list.add("image "+ name +" "+ body.get(x) +" 0" + z +" "+ faces.get(y) +" Fade Flip= Transform(\""+ name +" "+ body.get(x) +" 0"+ z +" "+ faces.get(y) +" Fade\",xzoom=-1.0)");
				
			}
					}
		}
		
		Path file = Paths.get("imageList.txt");
		Files.write(file, list, Charset.forName("UTF-8"));
		JOptionPane.showMessageDialog(null, "Done, look for a imageList in the same folder as program");
		
		
	}


	}



