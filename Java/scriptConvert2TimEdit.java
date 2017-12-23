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
          list.add(thisRow.trim()); //+ listName + " "+(rowCount+1)); need to change back
        
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
          bugList.add(thisRow.trim() + " Row " + rowCount+1 + " " + listName);
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
