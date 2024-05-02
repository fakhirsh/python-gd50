using Godot;
using System;

public partial class Slime : Node2D
{
	int Speed = 20;
	int direction = 1;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		var rayRight = GetNode<RayCast2D>("RayCastRight");
		var rayLeft = GetNode<RayCast2D>("RayCastLeft");
		var animSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");

		if (rayRight.IsColliding())
		{
			direction = -1;
			animSprite.FlipH = true;
		}
		else if (rayLeft.IsColliding())
		{
			direction = 1;
			animSprite.FlipH = false;
		}

		Position += new Vector2((float)(Speed * delta) * direction, 0);
	}
}
