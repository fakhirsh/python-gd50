using Godot;
using System;

public partial class Enemy : Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		uint randomNumber = GD.Randi() % 4;
		float AMOUNT = 5;
		if(randomNumber == 0)
		{
			this.Position += new Vector2(0, -AMOUNT);
		}
		else if(randomNumber == 1)
		{
			this.Position += new Vector2(0, AMOUNT);
		}
		else if(randomNumber == 2)
		{
			this.Position += new Vector2(-AMOUNT, 0);
		}
		else if(randomNumber == 3)
		{
			this.Position += new Vector2(AMOUNT, 0);
		}
	}
}
