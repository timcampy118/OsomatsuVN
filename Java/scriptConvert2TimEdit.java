package script;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class scriptConvert2TimEdit
{
  static ArrayList<String> script;
  static ArrayList<String> character;
  static ArrayList<String> list;
  static ArrayList<String> bugList;
  static Integer rowCount;
  static Integer currentCol;
  static Scanner scan;
  static Boolean check1;
  static Boolean check2;
  static String listName;
  
  public static File getFile()
  {
    File file = null;
    try {
      String current = new File(".").getCanonicalPath();
      file = new File(current + "/script.xlsx");
    }
    catch (Exception e) {
      System.out.println("ERROR: " + e.getMessage());
    }

    return file;
  }

  public static void readThisShit(File file)
  {
    bugList = new ArrayList<String>();
    try
    {
    	
  
      XSSFWorkbook workbook = new XSSFWorkbook(file);

      XSSFSheet sheet = workbook.getSheetAt(0);
      Boolean bad = Boolean.valueOf(false);
      rowCount = Integer.valueOf(0);

      String inputFile = JOptionPane.showInputDialog(null, "type in name of the position file (Include the .txt)");
      scan= new Scanner(new File(inputFile));
      
      Iterator<Row> rowIterator = sheet.iterator();
      while (rowIterator.hasNext())
      {
        Row row = (Row)rowIterator.next();

        Iterator<Cell> cellIterator = row.cellIterator();

        String thisRow = "";

        check1=false;
        check2=false;
        
        while (cellIterator.hasNext()) 
        {
          Cell cell = (Cell)cellIterator.next();
          String thisCell;
     
          try
          {
            thisCell = cell.getStringCellValue();
          }
          catch (Exception e)
          {
            thisCell = Double.toString(cell.getNumericCellValue());
          }
          int currentColNumber = cell.getColumnIndex();

          //person who is talking
          if (currentColNumber == 0)
          {
            if ((thisCell.equals("")) || (thisCell.toLowerCase().equals("everyone")))
            {
              bad = true;
              check1=true;
            }
            else if (((thisCell.length() >= 9) || (thisCell.charAt(0) < 'A') || (thisCell.charAt(0) > 'Z')) && ((thisCell.charAt(0) < 'a') || (thisCell.charAt(0) > 'z')))
            {
              bad = true;
              check1=true;
            }
            else
            {
            	check1=true;
            }

            thisCell = thisCell.toLowerCase();
          }
          //dialogue
          else if (currentColNumber == 1)
          {
            if ((thisCell.equals("")) || (thisRow.equals("")))
            {
              thisCell = "";
              bad = true;
            }
            else {
              thisCell = "\"" + thisCell + "\"";
              check2=true;
            }
          }
          
          
          else
          {
        	  //bugList.add(thisCell + " Row " + rowCount); //should never happen
          }
          
          
           if ((thisCell != "") && (currentColNumber < 2))
            thisRow = thisRow + " " + thisCell;
          rowCount = Integer.valueOf(cell.getRowIndex());
       
        }

        
        
        if (!bad)
        {
        	getFromList();
        	while(!listName.contains("done"))
            {
        		list.add(listName);
        		getFromList();
            }
          list.add(thisRow.trim());
        
        }
        else if (thisRow.trim() != "") 
        {
        	System.out.println(check1+""+check2);
          if(check1&&check2)
          {
        	  getFromList();
          		while(!listName.contains("done"))
          		{
	          		bugList.add(listName);
	          		getFromList();
          		}
          }
          bugList.add(thisRow.trim() + " Row " + rowCount);
        }

        bad = false;
      }
    }
    catch (InvalidFormatException e)
    {
      e.printStackTrace();
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }
/*
  public static String imageLocation(String inputNum)
  {
    String imageName = "";
    String charName = "";
    String outfit = "";
    String expression = "";
    String flip = "";
    String fade = "";
    String pos = "";

    System.out.println(inputNum);
    if(inputNum.length()<2)
    {
    	
    }
    else if (inputNum.charAt(0) == '1')
    {
      imageName = imageName + "show";

      switch (inputNum.charAt(1)) {
      case '1':
        charName = " oso";
        break;
      case '2':
        charName = " kara";
        break;
      case '3':
        charName = " choro";
        break;
      case '4':
        charName = " ichi";
        break;
      case '5':
        charName = " jyushi";
        break;
      case '6':
        charName = " todo";
        break;
      default:
        charName = " oso";
      }

      switch (inputNum.charAt(2)) {
      case '1':
        outfit = " SchoolS";
        break;
      case '2':
        outfit = " SchoolW";
        break;
      case '3':
        outfit = " Naked";
        break;
      case '4':
        outfit = " Maintee";
        break;
      case '5':
        outfit = " Pj";
        break;
      case '6':
        outfit = " Bathtowel";
        break;
      case '7':
        outfit = " Sera";
        break;
      case '8':
        outfit = " Casual";
        break;
      case '9':
        outfit = " Bathrobe";
        break;
      case '0':
        outfit = " Naked";
        break;
      case '-':
        outfit = " Mainpark";
        break;
      case '.':
      case '/':
      default:
        outfit = " SchoolS";
      }

      switch (inputNum.charAt(3)) {
      case '1':
        expression = " Neutral";
        break;
      case '2':
        expression = " Happy1";
        break;
      case '3':
        expression = " Happy2";
        break;
      case '4':
        expression = " Angry1";
        break;
      case '5':
        expression = " Angry2";
        break;
      case '6':
        expression = " Blank";
        break;
      case '7':
        expression = " Dark";
        break;
      case '8':
        expression = " Surprised";
        break;
      case '9':
        expression = " Shocked";
        break;
      case '0':
        expression = " Nervous";
        break;
      case '-':
        expression = " Thinking";
        break;
      case '=':
        expression = " Blushing";
        break;
      case '+':
        expression = " Perverted";
        break;
      case '*':
    	expression = " Displeased";
        break;
      default:
        expression = " Neutral";
      }

      switch (inputNum.charAt(4)) {
      case '1':
        pos = " pos1";
        flip = " Flip";
        break;
      case '2':
        pos = " pos2";
        flip = " Flip";
        break;
      case '3':
        pos = " pos3";
        flip = " Flip";
        break;
      case '4':
        pos = " pos4";
        break;
      case '5':
        pos = " pos5";
        break;
      case '6':
        pos = " pos6";
        break;
      case '7':
        pos = " pos7";
        break;
      default:
        pos = " pos1";
      }
//System.out.println(inputNum);
      if (inputNum.length()>5 && inputNum.charAt(5) == '1')
      {
        fade = " Fade";
      }

    }
    else
    {
      imageName = imageName + "hide";
      switch (inputNum.charAt(1)) {
      case '1':
        charName = " oso";
        break;
      case '2':
        charName = " kara";
        break;
      case '3':
        charName = " choro";
        break;
      case '4':
        charName = " ichi";
        break;
      case '5':
        charName = " jyushi";
        break;
      case '6':
        charName = " todo";
        break;
      default:
        charName = " oso";
      }
    }

    if(inputNum.length()<2)
    {
    	bugList.add(inputNum);
    }
    else if (inputNum.charAt(0) == '1')
      imageName = imageName + charName + outfit + expression + fade + flip + " at" + pos;
    else {
      imageName = imageName + charName;
    }

    return imageName;
  }
*/
  public static void main(String[] args)
    throws IOException
  {
    String testString = "";
    testString = testString + "run";
    testString = testString + " hide";
    try
    {
      list = new ArrayList<String>();
      File inputFile = getFile();
      System.out.println("FILE TO PARSE: " + inputFile.getName());

      readThisShit(inputFile);

      
      
      

      Path file = Paths.get("convertedScript.txt", new String[0]);
      Files.write(file, list, Charset.forName("UTF-8"), new OpenOption[0]);

      Path file2 = Paths.get("ignoredScript.txt", new String[0]);
      Files.write(file2, bugList, Charset.forName("UTF-8"), new OpenOption[0]);
      JOptionPane.showMessageDialog(null, "Done");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
  
  public static void getFromList()
  {
	  if(scan.hasNextLine())
	  listName=scan.nextLine();
	  else
		  System.out.println("No more");
  }
}

/* Location:           /home/eds/Downloads/scriptConverterV1.2/
 * Qualified Name:     scriptConvert2TimEdit
 * JD-Core Version:    0.6.2
 */
