package gui;

class Sprite 
{
	public String character;
	public String face;
	public String arm;
	public String outfit;
	public String pos;
	public boolean fade;


public Sprite(String character, String face, String arm, String outfit, String pos, Boolean fade)
{
	this.character=character;
	this.face=face;
	this.arm=arm;
	this.outfit=outfit;
	this.pos=pos;
	this.fade=fade;
}

public String getCharacter()
{
	return character;
}
public String getFace()
{
	return face;
}
public String getArm()
{
	return arm;
}
public String getOutfit()
{
	return outfit;
}
public String getPos()
{
	return pos;
}
public Boolean getFade()
{
	return fade;
}

}
