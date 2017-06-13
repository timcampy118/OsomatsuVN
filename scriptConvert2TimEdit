

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

import javax.swing.JOptionPane;

import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class scriptConvert2TimEdit {

	static ArrayList <String> script;
	static ArrayList <String> character;
	static ArrayList<String> list;
	static ArrayList<String> bugList;
	static Scanner reader;
	static Integer rowCount;
	static Integer currentCol;



	public static File getFile()
	{
		File file = null;
		try {
			String current = new java.io.File( "." ).getCanonicalPath();
			file = new File(current+"/script.xlsx");

		} catch (Exception e) {
			System.out.println("ERROR: "+e.getMessage());
		}

		return file;
	}





	

	public static void readThisShit(File file){
		bugList=new ArrayList<String>();

		try {
			XSSFWorkbook workbook = new XSSFWorkbook(file);

			XSSFSheet sheet = workbook.getSheetAt(0);
			Boolean bad=false;
			rowCount=0;
			//Iterate through each rows one by one
			Iterator<Row> rowIterator = sheet.iterator();
			while (rowIterator.hasNext()){

				Row row = rowIterator.next();
				//For each row, iterate through all the columns
				Iterator<Cell> cellIterator = row.cellIterator();

				String thisRow = "";

				while (cellIterator.hasNext()){
					Cell cell = cellIterator.next();
					String thisCell;
					//Check the cell type and format accordingly
					try
					{
						thisCell = cell.getStringCellValue();
					}
					catch (Exception e) 
					{
						thisCell = Double.toString(cell.getNumericCellValue());
					}
					int currentColNumber = cell.getColumnIndex();

					if(currentColNumber==0)
					{
						if(thisCell.equals("") || thisCell.toLowerCase().equals("everyone"))
						{
							bad=true;
						}
						else if(thisCell.length()<9 && (thisCell.charAt(0)>=65 && thisCell.charAt(0)<= 90) || (thisCell.charAt(0)>=97 && thisCell.charAt(0)<=122))
						{
							
						}
						else
						{
							bad=true;
							
						}
						thisCell = thisCell.toLowerCase();
					}
					else if(currentColNumber==1)
					{
						if(thisCell.equals("") || thisRow.equals(""))
						{
							thisCell="";
							bad=true;
						}
						else
							thisCell = "\""+thisCell+"\"";
					}
					else
					{
						list.add(imageLocation(thisCell));
					}
					if(thisCell!="" && currentColNumber<2)
						thisRow = thisRow+" "+thisCell;
					rowCount=cell.getRowIndex();

				}
				//System.out.println(thisRow);
				
				if(!bad)
					list.add(thisRow.trim());
				else if(thisRow.trim()!="")
					bugList.add(thisRow.trim()+" Row "+rowCount);
				else
				{
					
				}
				bad=false;
					
			}
		} catch (InvalidFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		
	}
				//System.out.println(thisRow);
				
				
					
			
		
		

	public static String imageLocation(String inputNum)
	{
		String imageName="";
		String charName="";
		String outfit="";
		String expression="";
		String flip="";
		String fade="";
		String pos="";
		
		System.out.println(inputNum);
			if(inputNum.charAt(0)=='1')
				{
					imageName=imageName+"show";
					//System.out.println(inputNum.charAt(1));
					switch (inputNum.charAt(1)) 
					{
					case '1':	charName=" oso";
								break;
					case '2':	charName=" kara";
								break;
					case '3':	charName=" choro";
								break;
					case '4':	charName=" ichi";
								break;
					case '5':	charName=" jyushi";
								break;
					case '6':	charName=" todo";
								break;
					case '7':	charName=" chibita";
								break;
					default:
								charName=" oso";
								break;
					}
					
					switch (inputNum.charAt(2)) 
					{
					case '1':	outfit=" SchoolS";
								break;
					case '2':	outfit=" SchoolW";
								break;
					case '3':	outfit=" Naked";
								break;
					case '4':	outfit=" Maintee";
								break;
					case '5':	outfit=" Pj";
								break;
					case '6':	outfit=" Bathtowel";
								break;
					case '7':	outfit=" Sera";
								break;
					case '8':	outfit=" Casual";
								break;
					case '9':	outfit=" Bathrobe";
								break;
					case '0':	outfit=" Naked";
								break;
					case '-':	outfit=" Mainpark";
								break;
					default:
								outfit=" SchoolS";
								break;
					}
				
					
					switch (inputNum.charAt(3)) 
					{
					case '1':	expression=" Neutral";
								break;
					case '2':	expression=" Happy1";
								break;
					case '3':	expression=" Happy2";
								break;
					case '4':	expression=" Angry1";
								break;
					case '5':	expression=" Angry2";
								break;
					case '6':	expression=" Blank";
								break;
					case '7':	expression=" Dark";
								break;
					case '8':	expression=" Surprised";
								break;
					case '9':	expression=" Shocked";
								break;
					case '0':	expression=" Nervous";
								break;
					case '-':	expression=" Thinking";
								break;
					case '=':	expression=" Blushing";
								break;
					case '+':	expression=" Perverted";
								break;
					default:
								expression=" Neutral";
								break;
					}
					
					
						switch (inputNum.charAt(4)) 
						{
						case '1':	pos=" pos1";
									flip=" Flip";
									break;
						case '2':	pos=" pos2";
									flip=" Flip";
									break;
						case '3':	pos=" pos3";
									flip=" Flip";
									break;
						case '4':	pos=" pos4";
									break;
						case '5':	pos=" pos5";
									break;
						case '6':	pos=" pos6";
									break;
						case '7':	pos=" pos7";
									break;
						default:
									pos=" pos1";
									break;
						}
						if(charName.equals(" chibita"))
							pos=pos+"c";
						
						if(inputNum.charAt(5)=='1')
						{
							fade=" Fade";
						}
						
					
			}
			else
			{
				imageName=imageName+"hide";
				switch (inputNum.charAt(1)) 
				{
				case '1':	charName=" oso";
							break;
				case '2':	charName=" kara";
							break;
				case '3':	charName=" choro";
							break;
				case '4':	charName=" ichi";
							break;
				case '5':	charName=" jyushi";
							break;
				case '6':	charName=" todo";
							break;
				default:
							charName=" oso";
							break;
				} 
			}
			if(inputNum.charAt(0)=='1')
			imageName=imageName+charName+outfit+expression+fade+flip+" at"+pos;
			else
			imageName=imageName+charName;
			
				
			return imageName;
		}
		
	
	

	public static void main(String[] args) throws IOException {

		String testString="";
		testString=testString+"run";
		testString=testString+" hide";
		//System.out.println(testString);
		try{
			
			list = new ArrayList<String>();
			File inputFile = getFile();
			System.out.println("FILE TO PARSE: "+inputFile.getName());

			//file checking here?

			readThisShit(inputFile);

			int run=0;
			
			while(run<list.size())
			{
				//System.out.println(list.get(run));
				run++;
			}
			
			Path file = Paths.get("convertedScript.txt");
			Files.write(file, list, Charset.forName("UTF-8"));
			
			
			
			Path file2 = Paths.get("ignoredScript.txt");
			Files.write(file2, bugList, Charset.forName("UTF-8"));
			JOptionPane.showMessageDialog(null, "Done");
			

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}


/*

if(inputNum.charAt(7)=='1')
{
	imageName=imageName+" behind";
	switch (inputNum.charAt(8)) 
	{
	case '1':	imageName=imageName+" oso";
				break;
	case '2':	imageName=imageName+" kara";
				break;
	case '3':	imageName=imageName+" choro";
				break;
	case '4':	imageName=imageName+" ichi";
				break;
	case '5':	imageName=imageName+" jyushi";
				break;
	case '6':	imageName=imageName+" todo";
				break;
	default:
				imageName=imageName+" oso";
				break;
	}
	
	
}
else

*/
